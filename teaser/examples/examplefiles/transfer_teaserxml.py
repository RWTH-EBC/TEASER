import teaser.data.input.teaserxml_input as t_input_old
from teaser.project import Project
import os
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
#     "ASHRAE140.mos"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "ASHRAE140_600.teaserXML"), prj)
# prj.save_project(
#     file_name="ASHRAE140_600.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
#     "ASHRAE140.mos"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "ASHRAE140_620.teaserXML"), prj)
# prj.save_project(
#     file_name="ASHRAE140_620.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
#     "ASHRAE140.mos"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "ASHRAE140_900.teaserXML"), prj)
# prj.save_project(
#     file_name="ASHRAE140_900.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
#     "ASHRAE140.mos"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "ASHRAE140_920.teaserXML"), prj)
# prj.save_project(
#     file_name="ASHRAE140_920.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "VDI6007_Room1.teaserXML"), prj)
# prj.save_project(
#     file_name="VDI6007_Room1.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "VDI6007_Room3.teaserXML"), prj)
# prj.save_project(
#     file_name="VDI6007_Room3.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "VDI6007_Room8.teaserXML"), prj)
# prj.save_project(
#     file_name="VDI6007_Room8.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))
#
# prj = Project(load_data=False)
# prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/"
# t_input_old.load_teaser_xml(os.path.join(
#     os.path.dirname(
#         os.path.realpath(__file__)), "VDI6007_Room10.teaserXML"), prj)
# prj.save_project(
#     file_name="VDI6007_Room10.json",
#     path=os.path.dirname(
#         os.path.realpath(__file__)))

prj = Project(load_data=False)
prj.weather_file_path = "modelica://AixLib/Resources/WeatherData/"
t_input_old.load_teaser_xml(os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)), "old.teaserXML"), prj)
prj.save_project(
    file_name="unitTestCalc.json",
    path=os.path.dirname(
        os.path.realpath(__file__)))
