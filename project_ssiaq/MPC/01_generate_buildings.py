from project_ssiaq.simulate_scenarios import *

def export_fmu(cd,model_name,aixlib_mo,teaser_mo):

    # change license files
    os.rename(r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\dymola.lic",
              r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\academy.lic")
    os.rename(r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\industry.lic",
              r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\dymola.lic")

    dym_api = DymolaAPI(model_name=model_name,
            working_directory=cd,
            n_cpu=1,
            packages=[aixlib_mo, teaser_mo],
            show_window=True,
            n_restart=-1,
            equidistant_output=False,
            extract_variables=True,
            dymola_version='Dymola 2023'
        )

    print("Number of variables:", len(dym_api.variables))
    print("Number of outputs:", len(dym_api.outputs))
    print("Number of inputs:", len(dym_api.inputs))
    print("Number of parameters:", len(dym_api.parameters))
    print("Number of states:", len(dym_api.states))

    dym_api.dymola.ExecuteCommand("Advanced.GenerateBinaryExportDymosim = true")
    dym_api.dymola.ExecuteCommand("Advanced.EnableCodeExport = true")
    dym_api.dymola.ExecuteCommand('Advanced.FMI.xmlIgnoreLocal = false')  # For generating FMUs from (non-residential) models with xml errors!
    binary_valid = dym_api.dymola.RequestOption("BinaryModelExport")
    if not binary_valid:
        print("Could not check out binary licence!")
        dym_api.dymola.ExecuteCommand("Advanced.GenerateBinaryExportDymosim = false")
        dym_api.dymola.ExecuteCommand("Advanced.EnableCodeExport = false")
    dym_api.set_cd(cd)
    #dym_api.dymola.ExecuteCommand('translateModelFMU("'+str(model_name)+'", false, "", "2", "all", false, 0, fill("", 0));')
    dym_api.dymola.translateModelFMU(
        modelToOpen=model_name,
        modelName=model_name,
        storeResult=False,
        fmiVersion='2',
        fmiType='all',
        includeSource=False,
        includeImage=0)
    dym_api.close()  # important to completely switch to academic's license!

    os.rename(r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\dymola.lic",
              r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\industry.lic")
    os.rename(r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\academy.lic",
              r"C:\Users\pse\AppData\Roaming\DassaultSystemes\Dymola\dymola.lic")

if __name__ == "__main__":
        setup_name = "20240304_mpc_test2"
        #basepath = pathlib.Path('R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten/03_Modellpraediktive_Regelung').joinpath(
        #        setup_name)
        basepath = pathlib.Path(r'D:\pse\temp_SSIAQ').joinpath(setup_name)
        scenarios = load_scenarios(basepath.joinpath("scenarios_test.xlsx"))
        model_export_path = basepath.joinpath("models")
        fmu_export_path = basepath.joinpath("fmus")
        if not os.path.exists(basepath.joinpath("schedules")):
            os.mkdir(basepath.joinpath("schedules"))

        start_scenario = 1 # row index of excel sheet != actual scenario number
        for index, scenario in scenarios.iterrows():
                if index + 1 < start_scenario:
                        continue  # skip scenarios until start_scenario is reached
                scenario_name = "S" + str(scenario['Scenario_number']) + "_" + str(scenario['Building_type'])
                prj = generate_project(name=scenario_name)
                prj = generate_bldg(prj, scenario)
                export_aixlib_model(prj, model_export_path.joinpath(scenario_name), scenario['Location'], scenario['Control_strategy'])
                export_schedules(prj, basepath.joinpath("schedules",scenario_name))

                export_fmu(
                    cd=fmu_export_path.joinpath(scenario_name),
                    aixlib_mo=r"D:\pse\GIT\AixLib\AixLib\package.mo",
                    teaser_mo=model_export_path.joinpath(scenario_name, prj.name, "package.mo"),
                    model_name=prj.name + "." + prj.buildings[0].name + "." + prj.buildings[0].name
                )

