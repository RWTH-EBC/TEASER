# Created January 2017
# TEASER Development Team

"""This module contains an example how to export buildings from a TEASER
project to ready-to-run simulation models for Modelica library Annex60. These
models simulate in Dymola, OpenModelica and JModelica.
"""

import teaser.examples.e1_generate_archetype as e1


def example_export_annex():
    """"This function demonstrates the export to Modelica library Annex60 using
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
    # For more information on models we'd like to refer you to the docs.

    prj.used_library_calc = 'Annex60'
    prj.number_of_elements_calc = 4
    prj.merge_windows_calc = False

    # To make sure the parameters are calculated correctly we recommend to
    # run calc_all_buildings() function

    prj.calc_all_buildings()

    # To export the ready-to-run models simply call Project.export_annex().
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. If you only want to export one specific building, you can
    # pass over the internal_id of that building and only this model will be
    # exported. In this case we want to export all buildings to our home
    # directory, thus we are passing over None for both parameters.

    prj.export_annex(
        internal_id=None,
        path=None)

if __name__ == '__main__':

    example_export_annex()

    print("Example 3: That's it! :)")
