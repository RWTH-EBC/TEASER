# Created January 2017
# TEASER Development Team

"""This module contains an example how to export buildings from a TEASER
project to ready-to-run simulation models for Modelica library IBPSA. These
models simulate in Dymola, OpenModelica and JModelica.
"""

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os


def example_export_ibpsa():
    """"This function demonstrates the export to Modelica library IBPSA using
    the API function of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # To make sure the export is using the desired parameters you should
    # always set model settings in the Project.
    # Project().used_library_calc specifies the used Modelica library
    # Project().number_of_elements_calc sets the models order
    # Project().merge_windows_calc specifies if thermal conduction through
    # windows is lumped into outer walls or not.
    # For more information on models we'd like to refer you to the docs. By
    # default TEASER uses a weather file provided in
    # teaser.data.input.inputdata.weatherdata. You can use your own weather
    # file by setting Project().weather_file_path. However we will use default
    # weather file.

    prj.used_library_calc = 'IBPSA'
    prj.number_of_elements_calc = 4
    prj.merge_windows_calc = False
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    # To make sure the parameters are calculated correctly we recommend to
    # run calc_all_buildings() function

    prj.calc_all_buildings()

    # To export the ready-to-run models simply call Project.export_ibpsa().
    # First specify the IBPSA related library you want to export the models
    # for. The models are identical in each library, but IBPSA Modelica
    # library is  just a core set of models and should not be used
    # standalone. Valid values are 'AixLib' (default), 'Buildings',
    # 'BuildingSystems' and 'IDEAS'. We chose AixLib
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. If you only want to export one specific building, you can
    # pass over the internal_id of that building and only this model will be
    # exported. In this case we want to export all buildings to our home
    # directory, thus we are passing over None for both parameters.

    prj.export_ibpsa(
        library='AixLib',
        internal_id=None,
        path=None)


if __name__ == '__main__':

    example_export_ibpsa()

    print("Example 3: That's it! :)")
