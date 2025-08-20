import json
import os

from pathlib import Path

import matplotlib.pyplot as plt


def perform_simulations(
        path_aixlib: Path
):
    from teaser.examples.e2_export_aixlib_models import example_export_aixlib
    path_export = example_export_aixlib()
    path_export = Path(path_export)

    with open(path_export.joinpath("simulation_information.json"), "r") as file:
        relevant_information = json.load(file)

    # Extract models to simulate, in this case they are "IdealHeatDemand" simulations
    models_to_simulate = [bui["IdealHeatDemand"] for bui in relevant_information["buildings"].values()]
    # Specify that the result files should be named the same as the buildings
    result_file_names = list(relevant_information["buildings"].keys())

    # Let's create a simulation result folder side by side to the project export
    save_path = path_export.parent.joinpath(path_export.name + "_SimulationResults")

    # Start the Dymola-API. For more information, see the example e2, e3 and e5 in ebcpy.
    from ebcpy import DymolaAPI

    dym_api = DymolaAPI(
        working_directory=save_path.joinpath("DymolaWorkingDirectory"),
        model_name=None,  # Keep empty for now
        packages=[path_aixlib, relevant_information["package_path"]],
        show_window=True,
        equidistant_output=True,
        n_cpu=2,  # Increase this number if you want to run more simulations in parallel.
        time_delay_between_starts=1
    )
    simulation_setup = {
        "start_time": 0,
        "stop_time": 86400 * 120,  # First 120 days
        "output_interval": 3600
    }
    dym_api.set_sim_setup(sim_setup=simulation_setup)

    # Perform the simulation storing the results as .mat files.
    # This is the most robust option with multiprocessing. Further options
    # exist in ebcpy, see their docs.
    simulation_result_files = dym_api.simulate(
        return_option="savepath",
        model_names=models_to_simulate,
        savepath=save_path,
        result_file_name=result_file_names
    )

    # ebcpy has a nice feature to store the simulation settings for later reproduction.
    dym_api.save_for_reproduction(
        title=relevant_information["project"],
        log_message=f"Simulation study of TEASER project",
        export_fmu=False
    )
    dym_api.close()

    # Extract relevant results by loading mat and storing some variables as parquet,
    # which is a pandas default and efficient format.
    # Furthermore, create a plot for each building of outdoor and indoor air temperatures,
    # as well as heat demand
    from ebcpy import TimeSeriesData
    variable_names_to_store = [
        "multizone.PHeater[*]",  # Wildcards store all zones
        "multizone.TAir[*]",
        "weaDat.weaBus.TDryBul"
    ]
    for mat_result_file in simulation_result_files:
        df = TimeSeriesData(mat_result_file, variable_names=variable_names_to_store).to_df()
        df_path = Path(mat_result_file).with_suffix(".parquet")
        df.to_parquet(
            df_path,
            engine="fastparquet",
            compression=None,
            index=True
        )
        os.remove(mat_result_file)
        df.index /= 86400  # To days
        fig, ax = plt.subplots(3, 1, sharex=True)
        ax[0].set_ylabel("$T_\mathrm{Oda}$ in °C")
        ax[0].plot(df.index, df.loc[:, "weaDat.weaBus.TDryBul"] - 273.15)
        ax[1].set_ylabel("$T_\mathrm{Zone}$ in °C")
        ax[2].set_ylabel("$P_\mathrm{Hea}$ in kW")
        for col in df.columns:
            if col.startswith("weaBus"):
                continue
            zone_number = col.split("[")[-1].split("]")[0]
            if col.startswith("multizone.TAir"):
                ax[1].plot(df.index, df.loc[:, col] / 1000, label=f"Zone {zone_number}")
            if col.startswith("multizone.PHeater"):
                ax[2].plot(df.index, df.loc[:, col] / 1000, label=f"Zone {zone_number}")
        ax[1].legend()
        ax[2].legend()
        ax[2].set_xlabel("Time in d")
        fig.suptitle(Path(mat_result_file).stem)
    plt.show()


if __name__ == '__main__':
    perform_simulations(path_aixlib=Path(r"D:\04_git\AixLib\AixLib\package.mo"))
