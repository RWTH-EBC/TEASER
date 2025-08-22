# # Example 13: Direct simulation of Modelica with TEASER, ebcpy, and AixLib
# This example demonstrates how to export building models using TEASER and simulate them with Dymola.
# You can not run this example using the online [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks),
# as you need Dymola installed on your device.

# ## Prerequisites
# To use this example, you need to install several packages:
# 1. ebcpy - For Dymola API interaction (`pip install ebcpy`)
# 2. AixLib - A Modelica library for building simulation (https://github.com/RWTH-EBC/AixLib).
#   If not provided, this example will try to clone AixLib using git.
#
# You also need Dymola installed on your system to run the simulations.


def perform_simulations():
    # First, we export the same archetypes as in `e2_export_aixlib_models`
    from teaser.examples.e2_export_aixlib_models import example_export_aixlib
    path_export = example_export_aixlib()

    # ## Loading simulation information
    # The TEASER export creates a JSON file with information about the models
    import json
    from pathlib import Path  # For easier path handling
    path_export = Path(path_export)
    with open(path_export.joinpath("simulation_information.json"), "r") as file:
        relevant_information = json.load(file)
    print(relevant_information)

    # ## Preparing simulation parameters
    # Extract the IdealDemands models for each building and set up result file names
    models_to_simulate = [bui["IdealDemands"] for bui in relevant_information["buildings"].values()]
    result_file_names = list(relevant_information["buildings"].keys())

    # ## Setting up simulation directory
    # Create a folder for simulation results next to the export folder
    save_path = path_export.parent.joinpath(path_export.name + "_SimulationResults")

    # ## Handle AixLib dependency
    # If AixLib path is not provided, clone it from GitHub.

    path_aixlib = None  # If you have AixLib locally, set the path here.

    if path_aixlib is None:
        import subprocess
        import os

        save_path.parent.mkdir(exist_ok=True)
        aixlib_dir = save_path.parent.joinpath("AixLib")
        if not aixlib_dir.exists():
            print(f"Cloning AixLib repository to {aixlib_dir}...")
            subprocess.run(
                ["git", "clone", "https://github.com/RWTH-EBC/AixLib", str(aixlib_dir)],
                check=True
            )
        path_aixlib = aixlib_dir.joinpath("AixLib/package.mo")
        print(f"Using AixLib from: {path_aixlib}")

    # ## Initialize Dymola API
    # This provides an interface to the Dymola simulation environment
    # Import and initialize the API with simulation parameters and package paths
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

    # ## Define simulation timeframe
    # Set up the simulation period (120 days) and output interval (hourly)
    simulation_setup = {
        "start_time": 0,
        "stop_time": 86400 * 120,  # First 120 days
        "output_interval": 3600
    }
    dym_api.set_sim_setup(sim_setup=simulation_setup)

    # ## Run the simulations
    # Perform the simulations and store results as .mat files
    # Using multiprocessing capabilities of ebcpy
    simulation_result_files = dym_api.simulate(
        return_option="savepath",
        model_names=models_to_simulate,
        savepath=save_path,
        result_file_name=result_file_names
    )

    # ## Save simulation settings for reproducibility
    # Optionally, you can store all simulation parameters for later reference
    # This feature does not work in jupyter notebooks, as it saves the current script.
    # Still, we highly encourage you to add it to your work locally, so
    # that you always know which settings were used to perform the simulations.

    # ```python
    # dym_api.save_for_reproduction(
    #     title=relevant_information["project"],
    #     log_message=f"Simulation study of TEASER project",
    #     export_fmu=False,
    # )
    # ```
    # Afterwards, we close Dymola:
    dym_api.close()

    # ## Analyze each simulation result
    # For each building,
    # - Load simulation data into a pandas DataFrame
    # - convert results to parquet (more efficient than .mat for pandas operations) (Only supported with python >=3.9)
    # - Remove original .mat file to save space
    # - Plot outdoor temperature, zone temperatures, and heating power

    # Set variable_names_to_store to None to load all variables

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
        import os
        os.remove(mat_result_file)

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(3, 1, sharex=True)

        df.index /= 86400  # Convert seconds to days for better readability

        ax[0].set_ylabel("$T_\mathrm{Oda}$ in °C")
        ax[0].plot(df.index, df.loc[:, "weaDat.weaBus.TDryBul"] - 273.15)
        ax[1].set_ylabel("$T_\mathrm{Zone}$ in °C")
        ax[2].set_ylabel("$P_\mathrm{Hea}$ in kW")

        for col in df.columns:  # Plot each zone's temperature and heating power
            if col.startswith("weaBus"):
                continue
            zone_number = col.split("[")[-1].split("]")[0]
            if col.startswith("multizone.TAir"):
                ax[1].plot(df.index, df.loc[:, col] - 273.15, label=f"Zone {zone_number}")
            if col.startswith("multizone.PHeater"):
                ax[2].plot(df.index, df.loc[:, col] / 1000, label=f"Zone {zone_number}")
        ax[1].legend()
        ax[2].legend()
        ax[2].set_xlabel("Time in d")
        fig.suptitle(df_path.stem)
        fig.savefig(df_path.with_suffix(".png"))
    plt.show()


if __name__ == '__main__':
    perform_simulations()
