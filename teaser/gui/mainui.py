# -*- coding: utf-8 -*-
# created June 2015
# by TEASER4 Development Team

import inspect
import os
import platform
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QDialog, QStandardItemModel
from PyQt4.Qt import Qt
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QStandardItem, QTabWidget, QPixmap
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from numpy.distutils.pathccompiler import PathScaleCCompiler
from scipy._lib.six import xrange

import matplotlib.pyplot as plt
from teaser.gui.controller.controller import Controller
from teaser.gui.guihelp.guiinfo import GUIInfo
from teaser.gui.guihelp.listviewzonesfiller import ListViewZonesFiller
from teaser.gui.guihelp.picturebutton import PictureButton
from teaser.gui.guihelp.trackableitem import TrackableItem
from teaser.logic.simulation.modelicainfo import ModelicaInfo
import teaser.logic.utilities as utilitis
from teaser.project import Project
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.archetypebuildings.residential import Residential
from teaser.logic.archetypebuildings.nonresidential import NonResidential


try:
    _fromUtf8 = Qt.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MainUI(QDialog):
    '''GUI Class

    This class represents the GUI

    Parameters
    -----------

    Note: the listed attributes are the ones that are need to show
          the GUI

    Attributes
    ----------

    '''

    # Constructor defines all elements in the GUI and sets the listModels for
    # the listViews
    def __init__(self, parent=None, gui=True, dir=None, file=None):
        super(MainUI, self).__init__(parent)

        """ General layout and gui-global variables """

        # Used to display the console inside the program.
        sys.stdout = EmittingStream(textWritten=self.normal_output_written)
        sys.stdin = EmittingStream(textWritten=self.normal_output_written)
        sys.stderr = EmittingStream(textWritten=self.normal_output_written)

        self.setWindowFlags(self.windowFlags() | Qt.WindowMinMaxButtonsHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dailyHoursRange = range(0, 23)
        self.current_building = 0
        self.current_zone = 0
        self.current_element = 0
        self.current_layer = 0
        self.current_transformation = "standard"
        self.current_type_building = "Office"
        self.is_switchable = False
        self.construction_type_switched = False
        self.type_building_ind_att = dict(layout_area=0.0,
                                          layout_window_area=0.0,
                                          layout_attic=0.0,
                                          layout_cellar=0.0,
                                          construction_type=0.0,
                                          neighbour_building=0.0,
                                          dormer=0.0)
        self.saved_values_for_edit = {"year": "", "height": "", "name": "",
                                      "location": "", "area": "", "number": "",
                                      "street": ""}
        self.temp_zones = {}
        self.all_constr_layer_list = []
        self.xml_layer_list = []
        self.xml_element_list = []
        self.zone_model = QStandardItemModel()
        self.outer_elements_model = QStandardItemModel()
        self.element_model = QStandardItemModel()
        self.layer_model = QStandardItemModel()
        self.element_layer_model = QStandardItemModel()
        self.element_layer_model_set_all_constr = QStandardItemModel()
        self.element_layer_model_update_xml = QStandardItemModel()
        self.element_model_update_xml = QStandardItemModel()
        self.wall_layer_model = QStandardItemModel()
        self.project = Project()
        self.project.modelica_info = ModelicaInfo()
        self.guiinfo = GUIInfo()
        self.lVZF = ListViewZonesFiller()
        self.is_empty_building_button = False
        self.file_path = ""
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(900, 800)
        self.setMinimumSize(QtCore.QSize(900, 800))
        self.setMaximumSize(QtCore.QSize(900, 800))
        self.teaser_icon = QtGui.QIcon()
        self.teaser_icon.addFile(utilitis.get_full_path(
                    'gui/guiimages/Teaser_logo.png'), QtCore.QSize(16, 16))
        self.setWindowIcon(self.teaser_icon)
        teaserVersion = "0.3.6 beta"
        self.setWindowTitle("TEASER Version %s" % teaserVersion)
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))
        self.ribbon_widget = QtGui.QTabWidget(self.central_widget)
        self.ribbon_widget.setGeometry(QtCore.QRect(1, 1, 899, 109))
        self.side_bar_widget = QtGui.QTabWidget(self.central_widget)
        self.side_bar_widget.setGeometry(QtCore.QRect(1, 110, 210, 590))
        self.main_widget = QtGui.QTabWidget(self.central_widget)
        self.main_widget.setGeometry(QtCore.QRect(211, 110, 689, 590))
        self.standard_view_group_box = QtGui.QGroupBox(self.main_widget)
        self.standard_view_group_box.setGeometry(QtCore.QRect(0, 0, 689, 590))
        self.standard_view_group_box.setVisible(True)
        self.standard_view_group_box.setAutoFillBackground(True)
        palette = self.standard_view_group_box.palette()
        palette.setColor(self.standard_view_group_box.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.standard_view_group_box.setPalette(palette)
        self.side_bar_group_box = QtGui.QGroupBox(self.side_bar_widget)
        self.side_bar_group_box.setGeometry(QtCore.QRect(0, 0, 210, 590))
        self.side_bar_group_box.setVisible(True)
        self.side_bar_group_box.setAutoFillBackground(True)
        palette = self.side_bar_group_box.palette()
        palette.setColor(self.side_bar_group_box.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.side_bar_group_box.setPalette(palette)
        self.ribbon_group_box = QtGui.QGroupBox(self.ribbon_widget)
        self.ribbon_group_box.setGeometry(QtCore.QRect(0, 0, 899, 109))
        self.ribbon_group_box.setVisible(True)
        self.ribbon_group_box.setAutoFillBackground(True)
        palette = self.ribbon_group_box.palette()
        palette.setColor(self.ribbon_group_box.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.ribbon_group_box.setPalette(palette)
        self.bottom_group_box = QtGui.QGroupBox(self)
        self.bottom_group_box.setGeometry(QtCore.QRect(0, 700, 900, 100))
        self.text_edit = QtGui.QTextEdit(self.bottom_group_box)
        self.text_edit.setGeometry(QtCore.QRect(0, 0, 900, 100))

        """ All controls in the main frame """

        self.mask_label_0 = QtGui.QLabel(self.main_widget)
        self.mask_label_0.setGeometry(QtCore.QRect(240, 100, 250, 100))
        self.mask_label_0.setVisible(False)
        self.mask_label_0.setStyleSheet("background-color:\
                                        rgba(255,255,255,255)")
        self.mask_label_5 = QtGui.QLabel(self.main_widget)
        self.mask_label_5.setGeometry(QtCore.QRect(0, 0, 900, 100))
        self.mask_label_5.setVisible(False)
        self.mask_label_5.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_6 = QtGui.QLabel(self.main_widget)
        self.mask_label_6.setGeometry(QtCore.QRect(0, 100, 240, 490))
        self.mask_label_6.setVisible(False)
        self.mask_label_6.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_7 = QtGui.QLabel(self.main_widget)
        self.mask_label_7.setGeometry(QtCore.QRect(490, 100, 410, 490))
        self.mask_label_7.setVisible(False)
        self.mask_label_7.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_8 = QtGui.QLabel(self.main_widget)
        self.mask_label_8.setGeometry(QtCore.QRect(240, 200, 250, 390))
        self.mask_label_8.setVisible(False)
        self.mask_label_8.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_9 = QtGui.QLabel(self.main_widget)
        self.mask_label_9.setGeometry(QtCore.QRect(255, 105, 220, 35))
        self.mask_label_9.setVisible(False)
        self.mask_label_9.setText("Press Save to exit edit-mode with\nchanges"
                                  "or Cancel to exit without:")
        self.mask_label_9.setStyleSheet("background-color:"
                                        "rgba(255,255,255,255)")
        f = QtGui.QFont("Arial", 11)
        self.mask_label_9.setFont(f)
        self.zones_list_label = QtGui.QLabel(self.standard_view_group_box)
        self.zones_list_label.setGeometry(QtCore.QRect(165, 5, 50, 20))
        self.zones_list_label.setText("Zones")
        self.zones_list_view = QtGui.QListView(self.standard_view_group_box)
        self.zones_list_view.setGeometry(QtCore.QRect(35, 30, 311, 558))
        self.zones_list_view.setObjectName(_fromUtf8("zones_list_view"))
        self.zones_list_view.setModel(self.zone_model)
        self.zones_list_view.setItemDelegate(self.lVZF)
        self.zones_list_view.doubleClicked.connect(self.change_zone_values_ui)
        self.zones_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.envelopes_list_label = QtGui.QLabel(self.standard_view_group_box)
        self.envelopes_list_label.setGeometry(QtCore.QRect(480, 5, 50, 20))
        self.envelopes_list_label.setText("Envelopes")
        self.envelopes_list_view = QtGui.QListView(
            self.standard_view_group_box)
        self.envelopes_list_view.setGeometry(QtCore.QRect(350, 30, 311, 558))
        self.envelopes_list_view.setObjectName(
            _fromUtf8("envelopes_list_view"))
        self.envelopes_list_view.setModel(self.outer_elements_model)
        self.envelopes_list_view.setItemDelegate(self.lVZF)
        self.envelopes_list_view.doubleClicked.connect(
            self.change_envelopes_values_ui)
        self.envelopes_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        """ All controls for creating a new thermal zone """

        self.create_new_zone_groupbox = QtGui.QGroupBox(self.main_widget)
        self.create_new_zone_groupbox.setGeometry(QtCore.QRect(0, 0, 900, 590))
        self.create_new_zone_groupbox.setVisible(False)
        self.create_new_zone_groupbox.setAutoFillBackground(True)
        palette = self.create_new_zone_groupbox.palette()
        palette.setColor(self.create_new_zone_groupbox.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.create_new_zone_groupbox.setPalette(palette)
        self.new_zone_gen_inf_groupbox = QtGui.QGroupBox(
            self.create_new_zone_groupbox)
        self.new_zone_gen_inf_groupbox.setGeometry(
            QtCore.QRect(5, 1, 210, 584))
        self.new_zone_gen_inf_groupbox.setTitle("General Zone Information")
        self.new_zone_gen_inf_groupbox.setAutoFillBackground(True)
        palette = self.new_zone_gen_inf_groupbox.palette()
        palette.setColor(self.new_zone_gen_inf_groupbox.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.new_zone_gen_inf_groupbox.setPalette(palette)
        self.new_zone_name_label = QtGui.QLabel(self.new_zone_gen_inf_groupbox)
        self.new_zone_name_label.setGeometry(QtCore.QRect(10, 60, 90, 25))
        self.new_zone_name_label.setText("Name:")
        self.new_zone_name_line_edit = QtGui.QLineEdit(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_name_line_edit.setGeometry(QtCore.QRect(110, 60, 90, 25))
        self.new_zone_area_label = QtGui.QLabel(self.new_zone_gen_inf_groupbox)
        self.new_zone_area_label.setGeometry(QtCore.QRect(10, 95, 90, 25))
        self.new_zone_area_label.setText("Area:")
        self.new_zone_area_line_edit = QtGui.QLineEdit(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_area_line_edit.setGeometry(QtCore.QRect(110, 95, 90, 25))
        self.new_zone_usage_label = QtGui.QLabel(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_usage_label.setGeometry(QtCore.QRect(10, 130, 90, 25))
        self.new_zone_usage_label.setText("Usage type:")
        self.new_zone_usage_line_edit = QtGui.QLineEdit(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_usage_line_edit.setGeometry(
            QtCore.QRect(110, 130, 90, 25))
        self.new_zone_save_button = QtGui.QPushButton(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_save_button.setGeometry(QtCore.QRect(10, 305, 90, 25))
        self.new_zone_save_button.setText("Save")
        self.new_zone_save_button.clicked.connect(self.check_inputs_new_zone)
        self.new_zone_cancel_button = QtGui.QPushButton(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_cancel_button.setGeometry(QtCore.QRect(110, 305, 90, 25))
        self.new_zone_cancel_button.setText("Cancel")
        self.new_zone_failed_label = QtGui.QLabel(
            self.new_zone_gen_inf_groupbox)
        self.new_zone_failed_label.setGeometry(QtCore.QRect(10, 340, 180, 50))
        self.new_zone_failed_label.setText(
            "Please insert values for Name, \nnet leased area and usage.")
        self.new_zone_failed_label.setVisible(False)

        """ All controls for editing a thermal zone """

        self.edit_zone_groupbox = QtGui.QGroupBox(self.main_widget)
        self.edit_zone_groupbox.setGeometry(QtCore.QRect(0, 0, 900, 590))
        self.edit_zone_groupbox.setVisible(False)
        self.edit_zone_groupbox.setAutoFillBackground(True)
        palette = self.edit_zone_groupbox.palette()
        palette.setColor(self.edit_zone_groupbox.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.edit_zone_groupbox.setPalette(palette)
        self.edit_gen_inf_groupbox = QtGui.QGroupBox(self.edit_zone_groupbox)
        self.edit_gen_inf_groupbox.setGeometry(QtCore.QRect(5, 1, 210, 584))
        self.edit_gen_inf_groupbox.setTitle("General Zone Information")
        self.edit_gen_inf_groupbox.setVisible(False)
        self.edit_gen_inf_tab_widget = QtGui.QTabWidget(
            self.edit_gen_inf_groupbox)
        self.edit_gen_inf_tab_widget.setGeometry(QtCore.QRect(0, 20, 210, 484))
        self.edit_gen_inf_tab_widget.setTabShape(QtGui.QTabWidget.Rounded)
        self.edit_gen_inf_tab = QtGui.QWidget()
        self.edit_usage_tab = QtGui.QWidget()
        self.edit_gen_inf_tab_widget.addTab(
            self.edit_gen_inf_tab, _fromUtf8(""))
        self.edit_gen_inf_tab_widget.addTab(self.edit_usage_tab, _fromUtf8(""))
        self.edit_gen_inf_tab_widget.setTabText(
            self.edit_gen_inf_tab_widget.indexOf(
                self.edit_gen_inf_tab), QtGui.QApplication.translate(
                "MainWindow", "General Info", None))
        self.edit_gen_inf_tab_widget.setTabText(
            self.edit_gen_inf_tab_widget.indexOf(self.edit_usage_tab),
            _translate("MainWindow", "Usage", None))
        self.edit_zone_name_label = QtGui.QLabel(self.edit_gen_inf_tab)
        self.edit_zone_name_label.setGeometry(QtCore.QRect(10, 30, 90, 25))
        self.edit_zone_name_label.setText("Name:")
        self.edit_zone_name_line_edit = QtGui.QLineEdit(self.edit_gen_inf_tab)
        self.edit_zone_name_line_edit.setGeometry(
            QtCore.QRect(110, 30, 90, 25))
        self.edit_zone_area_label = QtGui.QLabel(self.edit_gen_inf_tab)
        self.edit_zone_area_label.setGeometry(QtCore.QRect(10, 65, 90, 25))
        self.edit_zone_area_label.setText("Area:")
        self.edit_zone_area_line_edit = QtGui.QLineEdit(self.edit_gen_inf_tab)
        self.edit_zone_area_line_edit.setGeometry(
            QtCore.QRect(110, 65, 90, 25))
        self.edit_zone_area_inner_wall_label = QtGui.QLabel(
            self.edit_gen_inf_tab)
        self.edit_zone_area_inner_wall_label.setGeometry(
            QtCore.QRect(10, 100, 90, 25))
        self.edit_zone_area_inner_wall_label.setText("Inner Wall Area:")
        self.edit_zone_area_inner_wall_line_edit = QtGui.QLineEdit(
            self.edit_gen_inf_tab)
        self.edit_zone_area_inner_wall_line_edit.setGeometry(
            QtCore.QRect(110, 100, 90, 25))
        self.edit_zone_area_ceiling_label = QtGui.QLabel(self.edit_gen_inf_tab)
        self.edit_zone_area_ceiling_label.setGeometry(
            QtCore.QRect(10, 135, 90, 25))
        self.edit_zone_area_ceiling_label.setText("Ceiling Area:")
        self.edit_zone_area_ceiling_line_edit = QtGui.QLineEdit(
            self.edit_gen_inf_tab)
        self.edit_zone_area_ceiling_line_edit.setGeometry(
            QtCore.QRect(110, 135, 90, 25))
        self.edit_zone_area_floor_label = QtGui.QLabel(self.edit_gen_inf_tab)
        self.edit_zone_area_floor_label.setGeometry(
            QtCore.QRect(10, 170, 90, 25))
        self.edit_zone_area_floor_label.setText("Floor Area:")
        self.edit_zone_area_floor_line_edit = QtGui.QLineEdit(
            self.edit_gen_inf_tab)
        self.edit_zone_area_floor_line_edit.setGeometry(
            QtCore.QRect(110, 170, 90, 25))
        self.edit_zone_volume_label = QtGui.QLabel(self.edit_gen_inf_tab)
        self.edit_zone_volume_label.setGeometry(QtCore.QRect(10, 205, 90, 25))
        self.edit_zone_volume_label.setText("Volume:")
        self.edit_zone_volume_line_edit = QtGui.QLineEdit(
            self.edit_gen_inf_tab)
        self.edit_zone_volume_line_edit.setGeometry(
            QtCore.QRect(110, 205, 90, 25))

        self.edit_usage_infiltration_rate_label = QtGui.QLabel(
            self.edit_usage_tab)
        self.edit_usage_infiltration_rate_label.setGeometry(
            QtCore.QRect(10, 20, 90, 25))
        self.edit_usage_infiltration_rate_label.setText("Infiltration Rate:")
        self.edit_usage_infiltration_rate_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_infiltration_rate_line_edit.setGeometry(
            QtCore.QRect(110, 20, 90, 25))
        self.edit_usage_cooling_time_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_cooling_time_label.setGeometry(
            QtCore.QRect(5, 55, 50, 25))
        self.edit_usage_cooling_time_label.setText("Cooling:")
        self.edit_usage_cooling_time_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_cooling_time_line_edit.setGeometry(
            QtCore.QRect(65, 55, 40, 25))
        self.edit_usage_heating_time_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_heating_time_label.setGeometry(
            QtCore.QRect(110, 55, 50, 25))
        self.edit_usage_heating_time_label.setText("Heating:")
        self.edit_usage_heating_time_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_heating_time_line_edit.setGeometry(
            QtCore.QRect(165, 55, 40, 25))
        self.edit_usage_set_temp_heat_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_set_temp_heat_label.setGeometry(
            QtCore.QRect(5, 90, 50, 25))
        self.edit_usage_set_temp_heat_label.setText("TempHeat:")
        self.edit_usage_set_temp_heat_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_set_temp_heat_line_edit.setGeometry(
            QtCore.QRect(65, 90, 40, 25))
        self.edit_usage_set_temp_cool_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_set_temp_cool_label.setGeometry(
            QtCore.QRect(110, 90, 50, 25))
        self.edit_usage_set_temp_cool_label.setText("TempCool:")
        self.edit_usage_set_temp_cool_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_set_temp_cool_line_edit.setGeometry(
            QtCore.QRect(165, 90, 40, 25))
        self.edit_usage_temp_set_back_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_temp_set_back_label.setGeometry(
            QtCore.QRect(10, 125, 90, 25))
        self.edit_usage_temp_set_back_label.setText("Temp set back:")
        self.edit_usage_temp_set_back_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_temp_set_back_line_edit.setGeometry(
            QtCore.QRect(110, 125, 90, 25))
        self.edit_usage_min_air_exchange_label = QtGui.QLabel(
            self.edit_usage_tab)
        self.edit_usage_min_air_exchange_label.setGeometry(
            QtCore.QRect(10, 160, 90, 25))
        self.edit_usage_min_air_exchange_label.setText("Min Air Exchange:")
        self.edit_usage_min_air_exchange_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_min_air_exchange_line_edit.setGeometry(
            QtCore.QRect(110, 160, 90, 25))
        self.edit_usage_min_ahu_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_min_ahu_label.setGeometry(QtCore.QRect(5, 195, 50, 25))
        self.edit_usage_min_ahu_label.setText("Min AHU:")
        self.edit_usage_min_ahu_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_min_ahu_line_edit.setGeometry(
            QtCore.QRect(65, 195, 40, 25))
        self.edit_usage_max_ahu_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_max_ahu_label.setGeometry(
            QtCore.QRect(110, 195, 50, 25))
        self.edit_usage_max_ahu_label.setText("Max AHU:")
        self.edit_usage_max_ahu_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_max_ahu_line_edit.setGeometry(
            QtCore.QRect(165, 195, 40, 25))
        self.edit_usage_with_ahu_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_with_ahu_label.setGeometry(
            QtCore.QRect(10, 230, 90, 25))
        self.edit_usage_with_ahu_label.setText("With AHU:")
        self.edit_usage_with_ahu_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_with_ahu_line_edit.setGeometry(
            QtCore.QRect(110, 230, 90, 25))
        self.edit_usage_rel_humidity_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_rel_humidity_label.setGeometry(
            QtCore.QRect(10, 265, 90, 25))
        self.edit_usage_rel_humidity_label.setText("Rel Humidity:")
        self.edit_usage_rel_humidity_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_rel_humidity_line_edit.setGeometry(
            QtCore.QRect(110, 265, 90, 25))
        self.edit_usage_persons_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_persons_label.setGeometry(
            QtCore.QRect(10, 300, 90, 25))
        self.edit_usage_persons_label.setText("Persons:")
        self.edit_usage_persons_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_persons_line_edit.setGeometry(
            QtCore.QRect(110, 300, 90, 25))
        self.edit_usage_machines_label = QtGui.QLabel(self.edit_usage_tab)
        self.edit_usage_machines_label.setGeometry(
            QtCore.QRect(10, 335, 90, 25))
        self.edit_usage_machines_label.setText("Machines:")
        self.edit_usage_machines_line_edit = QtGui.QLineEdit(
            self.edit_usage_tab)
        self.edit_usage_machines_line_edit.setGeometry(
            QtCore.QRect(110, 335, 90, 25))

        self.edit_zone_save_button = QtGui.QPushButton(
            self.edit_gen_inf_groupbox)
        self.edit_zone_save_button.setGeometry(QtCore.QRect(10, 509, 90, 25))
        self.edit_zone_save_button.setText("Save")
        self.edit_zone_save_button.clicked.connect(self.check_inputs_edit_zone)
        self.edit_zone_cancel_button = QtGui.QPushButton(
            self.edit_gen_inf_groupbox)
        self.edit_zone_cancel_button.setGeometry(
            QtCore.QRect(110, 509, 90, 25))
        self.edit_zone_cancel_button.setText("Cancel")
        self.edit_zone_failed_label = QtGui.QLabel(self.edit_gen_inf_groupbox)
        self.edit_zone_failed_label.setGeometry(QtCore.QRect(40, 524, 180, 50))
        self.edit_zone_failed_label.setText(
            "Please insert values for Name, \nnet leased area and usage.")
        self.edit_zone_failed_label.setVisible(False)
        self.edit_zone_list_label = QtGui.QLabel(self.edit_zone_groupbox)
        self.edit_zone_list_label.setGeometry(QtCore.QRect(350, 5, 50, 20))
        self.edit_zone_list_label.setText("Zones")
        self.edit_zone_list = QtGui.QListView(self.edit_zone_groupbox)
        self.edit_zone_list.setGeometry(QtCore.QRect(220, 30, 311, 558))
        self.edit_zone_list.setObjectName(_fromUtf8("zones_list_view"))
        self.edit_zone_list.setModel(self.zone_model)
        self.edit_zone_list.setItemDelegate(self.lVZF)
        self.edit_zone_list.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.edit_zone_list.clicked.connect(self.switch_current_zone)
        self.edit_zone_objects_list_label = QtGui.QLabel(
            self.edit_zone_groupbox)
        self.edit_zone_objects_list_label.setGeometry(
            QtCore.QRect(671, 5, 50, 20))
        self.edit_zone_objects_list_label.setText("Elements")
        self.edit_zone_objects_list = QtGui.QListView(self.edit_zone_groupbox)
        self.edit_zone_objects_list.setGeometry(
            QtCore.QRect(541, 30, 311, 558))
        self.edit_zone_objects_list.setObjectName(
            _fromUtf8("objects_list_view"))
        self.edit_zone_objects_list.setModel(self.element_model)
        self.edit_zone_objects_list.setItemDelegate(self.lVZF)
        self.edit_zone_objects_list.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        """ All controls to edit a layer """

        self.edit_layer_group_box = QtGui.QGroupBox(self.main_widget)
        self.edit_layer_group_box.setGeometry(QtCore.QRect(0, 0, 900, 590))
        self.edit_layer_group_box.setVisible(False)
        self.edit_layer_group_box.setAutoFillBackground(True)
        palette = self.edit_layer_group_box.palette()
        palette.setColor(self.edit_layer_group_box.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.edit_layer_group_box.setPalette(palette)
        self.edit_current_layer_list_label = QtGui.QLabel(
            self.edit_layer_group_box)
        self.edit_current_layer_list_label.setGeometry(
            QtCore.QRect(350, 5, 50, 20))
        self.edit_current_layer_list_label.setText("Layer")

        self.edit_current_layer_list = QtGui.QListView(
            self.edit_layer_group_box)
        self.edit_current_layer_list.setGeometry(
            QtCore.QRect(220, 30, 311, 558))
        self.edit_current_layer_list.setObjectName(
            _fromUtf8("layer_list_view"))
        self.edit_current_layer_list.setModel(self.layer_model)
        self.edit_current_layer_list.setItemDelegate(self.lVZF)
        self.edit_current_layer_list.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.edit_current_layer_list.clicked.connect(self.switch_current_layer)

        self.edit_layer_general_information_group_box = QtGui.QGroupBox(
            self.edit_layer_group_box)
        self.edit_layer_general_information_group_box.setGeometry(
            QtCore.QRect(5, 1, 210, 584))
        self.edit_layer_general_information_group_box.setTitle(
            "General Layer Information")
        self.edit_layer_general_information_group_box.setAutoFillBackground(
            True)
        palette = self.edit_layer_general_information_group_box.palette()
        palette.setColor(
            self.edit_layer_general_information_group_box.backgroundRole(),
            QtGui.QColor(100, 100, 100, 20))
        self.edit_layer_general_information_group_box.setPalette(palette)
        self.edit_layer_name_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_name_label.setGeometry(QtCore.QRect(10, 60, 90, 25))
        self.edit_layer_name_label.setText("Name:")
        self.edit_layer_name_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_name_line_edit.setGeometry(
            QtCore.QRect(110, 60, 90, 25))
        self.edit_layer_thickness_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_thickness_label.setGeometry(
            QtCore.QRect(10, 95, 90, 25))
        self.edit_layer_thickness_label.setText("Thickness:")
        self.edit_layer_thickness_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_thickness_line_edit.setGeometry(
            QtCore.QRect(110, 95, 90, 25))
        self.horizontal_line = QtGui.QFrame(
            self.edit_layer_general_information_group_box)
        self.horizontal_line.setFrameShape(QtGui.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizontal_line.setGeometry(QtCore.QRect(10, 125, 180, 5))
        self.edit_layer_material_name_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_material_name_label.setGeometry(
            QtCore.QRect(10, 135, 90, 25))
        self.edit_layer_material_name_label.setText("Material:")
        self.edit_layer_material_name_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_material_name_line_edit.setGeometry(
            QtCore.QRect(110, 135, 90, 25))
        self.edit_layer_density_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_density_label.setGeometry(
            QtCore.QRect(10, 170, 90, 25))
        self.edit_layer_density_label.setText("Density:")
        self.edit_layer_density_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_density_line_edit.setGeometry(
            QtCore.QRect(110, 170, 90, 25))
        self.edit_layer_thermal_conduct_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_thermal_conduct_label.setGeometry(
            QtCore.QRect(10, 205, 90, 25))
        self.edit_layer_thermal_conduct_label.setText("Thermal Conduct:")
        self.edit_layer_thermal_conduct_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_thermal_conduct_line_edit.setGeometry(
            QtCore.QRect(110, 205, 90, 25))
        self.edit_layer_heat_capacity_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_heat_capacity_label.setGeometry(
            QtCore.QRect(10, 240, 90, 25))
        self.edit_layer_heat_capacity_label.setText("Heat Capacity:")
        self.edit_layer_heat_capacity_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_heat_capacity_line_edit.setGeometry(
            QtCore.QRect(110, 240, 90, 25))
        self.edit_layer_solar_absorp_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_solar_absorp_label.setGeometry(
            QtCore.QRect(10, 275, 90, 25))
        self.edit_layer_solar_absorp_label.setText("Solar Absorption:")
        self.edit_layer_solar_absorp_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_solar_absorp_line_edit.setGeometry(
            QtCore.QRect(110, 275, 90, 25))
        self.edit_layer_ir_emissivity_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_ir_emissivity_label.setGeometry(
            QtCore.QRect(10, 310, 90, 25))
        self.edit_layer_ir_emissivity_label.setText("IR Emissivity:")
        self.edit_layer_ir_emissivity_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_ir_emissivity_line_edit.setGeometry(
            QtCore.QRect(110, 310, 90, 25))
        self.edit_layer_transmittance_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_transmittance_label.setGeometry(
            QtCore.QRect(10, 345, 90, 25))
        self.edit_layer_transmittance_label.setText("Transmittance:")
        self.edit_layer_transmittance_line_edit = QtGui.QLineEdit(
            self.edit_layer_general_information_group_box)
        self.edit_layer_transmittance_line_edit.setGeometry(
            QtCore.QRect(110, 345, 90, 25))
        self.edit_layer_save_button = QtGui.QPushButton(
            self.edit_layer_general_information_group_box)
        self.edit_layer_save_button.setGeometry(QtCore.QRect(10, 380, 90, 25))
        self.edit_layer_save_button.setText("Save")
        self.edit_layer_save_button.clicked.connect(self.check_inputs_new_zone)
        self.edit_layer_cancel_button = QtGui.QPushButton(
            self.edit_layer_general_information_group_box)
        self.edit_layer_cancel_button.setGeometry(
            QtCore.QRect(110, 380, 90, 25))
        self.edit_layer_cancel_button.setText("Cancel")
        self.edit_layer_failed_label = QtGui.QLabel(
            self.edit_layer_general_information_group_box)
        self.edit_layer_failed_label.setGeometry(
            QtCore.QRect(10, 415, 180, 50))
        self.edit_layer_failed_label.setText(
            "Please insert values for Name, \nnet leased area and usage.")
        self.edit_layer_failed_label.setVisible(False)

        """ All controls for editing a zone element """

        self.edit_element_groupbox = QtGui.QGroupBox(self.main_widget)
        self.edit_element_groupbox.setGeometry(QtCore.QRect(0, 0, 900, 590))
        self.edit_element_groupbox.setVisible(False)
        self.edit_element_groupbox.setAutoFillBackground(True)
        palette = self.edit_element_groupbox.palette()
        palette.setColor(self.edit_element_groupbox.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.edit_element_groupbox.setPalette(palette)
        self.edit_element_gen_inf_groupbox = QtGui.QGroupBox(
            self.edit_element_groupbox)
        self.edit_element_gen_inf_groupbox.setGeometry(
            QtCore.QRect(5, 1, 210, 584))
        self.edit_element_gen_inf_groupbox.setTitle(
            "General Element Information")
        self.edit_element_gen_inf_groupbox.setVisible(False)
        self.edit_element_gen_inf_groupbox.setAutoFillBackground(True)
        palette = self.edit_element_gen_inf_groupbox.palette()
        palette.setColor(self.edit_element_gen_inf_groupbox.backgroundRole(),
                         QtGui.QColor(100, 100, 100, 20))
        self.edit_element_gen_inf_groupbox.setPalette(palette)
        self.edit_element_name_label = QtGui.QLabel(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_name_label.setGeometry(QtCore.QRect(10, 60, 90, 25))
        self.edit_element_name_label.setText("Name:")
        self.edit_element_name_line_edit = QtGui.QLineEdit(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_name_line_edit.setGeometry(
            QtCore.QRect(110, 60, 90, 25))
        self.edit_element_type_label = QtGui.QLabel(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_type_label.setGeometry(QtCore.QRect(10, 95, 90, 25))
        self.edit_element_type_label.setText("Construction Type:")
        self.edit_element_type_line_edit = QtGui.QLineEdit(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_type_line_edit.setGeometry(
            QtCore.QRect(110, 95, 90, 25))
        self.edit_element_area_label = QtGui.QLabel(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_area_label.setGeometry(QtCore.QRect(10, 130, 90, 25))
        self.edit_element_area_label.setText("Area:")
        self.edit_element_area_line_edit = QtGui.QLineEdit(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_area_line_edit.setGeometry(
            QtCore.QRect(110, 130, 90, 25))
        self.edit_element_save_button = QtGui.QPushButton(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_save_button.setGeometry(
            QtCore.QRect(10, 305, 90, 25))
        self.edit_element_save_button.setText("Save")
        self.edit_element_save_button.clicked.connect(
            self.check_inputs_edit_element)
        self.edit_element_cancel_button = QtGui.QPushButton(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_cancel_button.setGeometry(
            QtCore.QRect(110, 305, 90, 25))
        self.edit_element_cancel_button.setText("Cancel")
        self.edit_element_failed_label = QtGui.QLabel(
            self.edit_element_gen_inf_groupbox)
        self.edit_element_failed_label.setGeometry(
            QtCore.QRect(10, 340, 180, 50))
        self.edit_element_failed_label.setText(
            "Please insert a value for Name.")
        self.edit_element_failed_label.setVisible(False)
        self.edit_element_list_label = QtGui.QLabel(self.edit_element_groupbox)
        self.edit_element_list_label.setGeometry(QtCore.QRect(350, 5, 50, 20))
        self.edit_element_list_label.setText("Elements")
        self.edit_element_list = QtGui.QListView(self.edit_element_groupbox)
        self.edit_element_list.setGeometry(QtCore.QRect(220, 30, 311, 558))
        self.edit_element_list.setObjectName(_fromUtf8("zones_list_view"))
        self.edit_element_list.setModel(self.element_model)
        self.edit_element_list.setItemDelegate(self.lVZF)
        self.edit_element_list.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.edit_element_list.clicked.connect(self.switch_current_element)
        self.edit_layer_list_label = QtGui.QLabel(self.edit_element_groupbox)
        self.edit_layer_list_label.setGeometry(QtCore.QRect(671, 5, 50, 20))
        self.edit_layer_list_label.setText("Layer")
        self.edit_layer_list = QtGui.QListView(self.edit_element_groupbox)
        self.edit_layer_list.setGeometry(QtCore.QRect(541, 30, 311, 558))
        self.edit_layer_list.setObjectName(_fromUtf8("objects_list_view"))
        self.edit_layer_list.setModel(self.layer_model)
        self.edit_layer_list.setItemDelegate(self.lVZF)
        self.edit_layer_list.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)

        """ All controls in the sidebar """

        self.mask_label_1 = QtGui.QLabel(self.side_bar_group_box)
        self.mask_label_1.setGeometry(QtCore.QRect(0, 0, 210, 55))
        self.mask_label_1.setVisible(False)
        self.mask_label_1.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_2 = QtGui.QLabel(self.side_bar_group_box)
        self.mask_label_2.setGeometry(QtCore.QRect(200, 55, 10, 245))
        self.mask_label_2.setVisible(False)
        self.mask_label_2.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.mask_label_3 = QtGui.QLabel(self.side_bar_group_box)
        self.mask_label_3.setGeometry(QtCore.QRect(0, 300, 210, 290))
        self.mask_label_3.setVisible(False)
        self.mask_label_3.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.image_1 = QtGui.QPixmap()
        self.image_1.load(utilitis.get_full_path("GUI/GUIImages/Bild1.png"))
        self.pix_label_1 = QtGui.QLabel(self.side_bar_group_box)
        self.pix_label_1.setPixmap(self.image_1)
        self.pix_label_1.setGeometry(QtCore.QRect(5, 500, 210, 137))
        self.pix_label_1.setObjectName(_fromUtf8("label"))
        self.side_bar_building_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_building_label.setGeometry(QtCore.QRect(5, 25, 60, 30))
        self.side_bar_building_label.setText("Building")
        self.buildings_combo_box_model = QStandardItemModel()
        self.buildings_combo_box_model.removeColumn(0)
        self.buildings_combo_box_model.insertColumn(0)
        self.buildings_combo_box_model.insertColumn(1)
        self.side_bar_buildings_combo_box = QtGui.QComboBox(
            self.side_bar_group_box)
        self.side_bar_buildings_combo_box.setGeometry(
            QtCore.QRect(75, 25, 120, 30))
        self.side_bar_buildings_combo_box.setModel(
            self.buildings_combo_box_model)
        self.side_bar_buildings_combo_box.setModelColumn(0)
        self.connect(self.side_bar_buildings_combo_box, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_building)
        self.side_bar_id_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_id_label.setGeometry(QtCore.QRect(5, 60, 90, 25))
        self.side_bar_id_label.setText("Name:")
        self.side_bar_id_line_edit = QtGui.QLineEdit(self.side_bar_group_box)
        self.side_bar_id_line_edit.setGeometry(QtCore.QRect(105, 60, 90, 25))
        self.connect(self.side_bar_id_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_id_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_street_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_street_label.setGeometry(QtCore.QRect(5, 95, 90, 25))
        self.side_bar_street_label.setText("Street/Nr.:")
        self.side_bar_street_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_street_line_edit.setGeometry(
            QtCore.QRect(105, 95, 90, 25))
        self.connect(self.side_bar_street_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_street_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_location_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_location_label.setGeometry(QtCore.QRect(5, 130, 90, 25))
        self.side_bar_location_label.setText("ZIP/City:")
        self.side_bar_location_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_location_line_edit.setGeometry(
            QtCore.QRect(105, 130, 90, 25))
        self.connect(self.side_bar_location_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_location_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_construction_year_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_construction_year_label.setGeometry(
            QtCore.QRect(5, 165, 90, 25))
        self.side_bar_construction_year_label.setText("Construction Year:")
        self.side_bar_construction_year_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_construction_year_line_edit.setGeometry(
            QtCore.QRect(105, 165, 90, 25))
        self.connect(self.side_bar_construction_year_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_construction_year_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_number_of_floors_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_number_of_floors_label.setGeometry(
            QtCore.QRect(5, 200, 90, 25))
        self.side_bar_number_of_floors_label.setText("Number of Floors:")
        self.side_bar_number_of_floors_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_number_of_floors_line_edit.setGeometry(
            QtCore.QRect(105, 200, 90, 25))
        self.connect(self.side_bar_number_of_floors_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_number_of_floors_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_height_of_floors_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_height_of_floors_label.setGeometry(
            QtCore.QRect(5, 235, 90, 25))
        self.side_bar_height_of_floors_label.setText("Height of Floors:")
        self.side_bar_height_of_floors_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_height_of_floors_line_edit.setGeometry(
            QtCore.QRect(105, 235, 90, 25))
        self.connect(self.side_bar_height_of_floors_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_height_of_floors_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)
        self.side_bar_net_leased_area_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_net_leased_area_label.setGeometry(
            QtCore.QRect(5, 270, 90, 25))
        self.side_bar_net_leased_area_label.setText("Net leased Area:")
        self.side_bar_net_leased_area_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_net_leased_area_line_edit.setGeometry(
            QtCore.QRect(105, 270, 90, 25))
        self.connect(self.side_bar_net_leased_area_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.show_warning_window_ui)
        self.connect(self.side_bar_net_leased_area_line_edit, QtCore.SIGNAL(
            "editingFinished()"), self.clear_focus_line_edits)

        """ All controls in the ribbon """

        self.mask_label_4 = QtGui.QLabel(self.ribbon_group_box)
        self.mask_label_4.setGeometry(QtCore.QRect(0, 0, 899, 109))
        self.mask_label_4.setVisible(False)
        self.mask_label_4.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.new_type_building_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Haus1.png")),
            self.ribbon_widget)
        self.new_type_building_button.setGeometry(QtCore.QRect(10, 5, 70, 70))
        self.new_type_building_button.clicked.connect(
            self.generate_type_building_ui)
        self.new_type_building_button.setToolTip(
            "Click to create a new typebuilding.")
        self.new_type_building_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_type_building_label.setGeometry(QtCore.QRect(10, 80, 70, 25))
        self.new_type_building_label.setText("C" + "reate Type- \nBuilding")
        self.new_empty_building_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/NewEmptyBuilding.png")),
            self.ribbon_widget)
        self.new_empty_building_button.setGeometry(QtCore.QRect(95, 5, 70, 70))
        self.new_empty_building_button.clicked.connect(
            self.create_new_building_ui)
        self.new_empty_building_button.setToolTip(
            "Creates a new building without any zones or values.")
        self.new_building_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_building_label.setGeometry(QtCore.QRect(95, 80, 70, 25))
        self.new_building_label.setText("Create \nBuilding")
        self.new_building_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_zone_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/AddZone.png")),
            self.ribbon_widget)
        self.add_zone_button.setGeometry(QtCore.QRect(180, 5, 70, 70))
        self.add_zone_button.clicked.connect(self.add_thermal_zone)
        self.add_zone_button.setToolTip(
            "Click to create a new thermal zone for the currently displayed"
            "building.")
        self.add_zone_label = QtGui.QLabel(self.ribbon_group_box)
        self.add_zone_label.setGeometry(QtCore.QRect(180, 80, 70, 25))
        self.add_zone_label.setText("Create New \n Zone")
        self.delete_zone_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/DeleteZone.png")),
            self.ribbon_widget)
        self.delete_zone_button.setGeometry(QtCore.QRect(265, 5, 70, 70))
        self.delete_zone_button.clicked.connect(self.delete_thermal_zone)
        self.delete_zone_button.setToolTip(
            "Deletes the currently selected zone from this building.")
        self.delete_label = QtGui.QLabel(self.ribbon_group_box)
        self.delete_label.setGeometry(QtCore.QRect(265, 80, 70, 25))
        self.delete_label.setText("Delete Cur- \nrent Zone")
        self.delete_building_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/EditBuilding.png")),
            self.ribbon_widget)
        self.delete_building_button.setGeometry(QtCore.QRect(350, 5, 70, 70))
        self.delete_building_button.clicked.connect(
            self.warning_delete_building)
        self.delete_building_button.setToolTip(
            "Switches to edit-mode. Allows modification of general"
            "building values.")
        self.delete_label = QtGui.QLabel(self.ribbon_group_box)
        self.delete_label.setGeometry(QtCore.QRect(350, 80, 70, 25))
        self.delete_label.setText("Delete\nBuilding")
        self.load_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Load.png")),
            self.ribbon_widget)
        self.load_button.setGeometry(QtCore.QRect(435, 5, 70, 70))
        self.load_button.clicked.connect(self.load_building_button)
        self.load_button.setToolTip("Loads a building from a .xml file.")
        self.load_label = QtGui.QLabel(self.ribbon_group_box)
        self.load_label.setGeometry(QtCore.QRect(435, 80, 70, 25))
        self.load_label.setText("Load\nBuilding")
        self.new_project_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Project_manager.png")),
            self.ribbon_widget)
        self.new_project_button.setGeometry(QtCore.QRect(520, 5, 70, 70))
        self.new_project_button.clicked.connect(self.create_new_project_ui)
        self.new_project_button.setToolTip("Creates a new Project.")
        self.new_project_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_project_label.setGeometry(QtCore.QRect(520, 80, 70, 25))
        self.new_project_label.setText("Create empty\nProject")
        self.open_simulation_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.open_simulation_button.setGeometry(QtCore.QRect(605, 5, 70, 70))
        self.open_simulation_button.clicked.connect(
            self.show_simulation_window)
        self.open_simulation_button.setToolTip("opens the Simulation Tab.")
        self.open_simulation_label = QtGui.QLabel(self.ribbon_group_box)
        self.open_simulation_label.setGeometry(QtCore.QRect(605, 80, 70, 25))
        self.open_simulation_label.setText("Open Simu-\n lation Tab")
        self.open_export_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.open_export_button.setGeometry(QtCore.QRect(685, 5, 70, 70))
        self.open_export_button.clicked.connect(
            self.show_export_window)
        self.open_export_button.setToolTip("opens the Export Tab.")
        self.open_export_label = QtGui.QLabel(self.ribbon_group_box)
        self.open_export_label.setGeometry(QtCore.QRect(685, 80, 70, 25))
        self.open_export_label.setText("Open Ex-\n port Tab")
        self.save_project_button = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.save_project_button.setGeometry(QtCore.QRect(765, 5, 70, 70))
        self.save_project_button.clicked.connect(
            self.click_save_current_project)
        self.save_project_button.setToolTip("Saves the current project.")
        self.save_project_label = QtGui.QLabel(self.ribbon_group_box)
        self.save_project_label.setGeometry(QtCore.QRect(765, 80, 70, 25))
        self.save_project_label.setText("Save Pro-\n ject Tab")
        self.xml_ui = PictureButton(QtGui.QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.xml_ui.setGeometry(QtCore.QRect(845, 5, 70, 70))
        self.xml_ui.clicked.connect(self.create_xml_ui)
        self.xml_ui_label = QtGui.QLabel(self.ribbon_group_box)
        self.xml_ui_label.setGeometry(QtCore.QRect(845, 80, 70, 25))
        self.xml_ui_label.setText("Update XMl")

        self.side_animation = QtCore.QPropertyAnimation(
            self.side_bar_widget, "geometry")
        self.main_animation = QtCore.QPropertyAnimation(
            self.main_widget, "geometry")

    def __del__(self):
        '''Destructor

        if the destructor is called then the instance is about to be destroyed.
        '''
        sys.stdout = sys.__stdout__

    def normal_output_written(self, text):
        '''Append text to the QTextEdit. Part of the package to display the
        console in the project.
        '''

        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()

    def create_new_project(self):
        '''Creates a new Project

        clears everything and sets the project back to default.
        '''

        self.project = Project()
        self.project.modelica_info = ModelicaInfo()
        self.current_building = 0
        self.current_zone = 0
        self.current_element = 0
        self.current_layer = 0
        self.zone_model.clear()
        self.outer_elements_model.clear()
        self.element_model.clear()
        self.layer_model.clear()
        self.buildings_combo_box_model.clear()
        self.side_bar_construction_year_line_edit.clear()
        self.side_bar_height_of_floors_line_edit.clear()
        self.side_bar_id_line_edit.clear()
        self.side_bar_location_line_edit.clear()
        self.side_bar_net_leased_area_line_edit.clear()
        self.side_bar_number_of_floors_line_edit.clear()
        self.side_bar_street_line_edit.clear()

    def create_new_project_ui(self):
        '''New project window

        creates the window to set the project to default.
        '''

        self.create_new_project_ui_page = QtGui.QWizardPage()
        self.create_new_project_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.create_new_project_ui_page.setWindowTitle("Empty Project")
        self.create_new_project_ui_page.setFixedWidth(350)
        self.create_new_project_ui_page.setFixedHeight(100)
        self.create_new_project_window_layout = QtGui.QGridLayout()
        self.create_new_project_ui_page.setLayout(
            self.create_new_project_window_layout)
        self.warning_message_create_empty_prj_label = QtGui.QLabel()
        self.warning_message_create_empty_prj_label.setText(
            "When creating a new project, all Values in Teaser will be " +
            "removed.")
        self.create_new_project_clear_button = QtGui.QPushButton()
        self.create_new_project_clear_button.setText("Clear")
        self.connect(self.create_new_project_clear_button,
                     SIGNAL("clicked()"), self.create_new_project)
        self.connect(self.create_new_project_clear_button,
                     SIGNAL("clicked()"), self.create_new_project_ui_page,
                     QtCore.SLOT("close()"))
        self.create_new_project_cancel_button = QtGui.QPushButton()
        self.create_new_project_cancel_button.setText("Cancel")
        self.connect(self.create_new_project_cancel_button,
                     SIGNAL("clicked()"), self.create_new_project_ui_page,
                     QtCore.SLOT("close()"))

        self.create_new_project_window_layout.addWidget(
            self.warning_message_create_empty_prj_label, 0, 0, 1, 0)
        self.create_new_project_window_layout.addWidget(
            self.create_new_project_clear_button, 2, 0)
        self.create_new_project_window_layout.addWidget(
            self.create_new_project_cancel_button, 2, 1)
        self.create_new_project_ui_page.setWindowModality(Qt.ApplicationModal)
        self.create_new_project_ui_page.show()

    def create_new_building_ui(self):
        '''New building window

        opens the create new building window.
        '''

        self.generate_new_building_ui_page = QtGui.QWizardPage()
        self.generate_new_building_ui_page.setWindowIcon(self.teaser_icon)
        self.generate_new_building_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.generate_new_building_ui_page.setWindowTitle(
            "Create new Building")
        self.generate_new_building_ui_page.setFixedWidth(300)
        self.generate_new_building_ui_page.setFixedHeight(300)
        self.generate_new_building_window_layout = QtGui.QGridLayout()
        self.generate_new_building_ui_page.setLayout(
            self.generate_new_building_window_layout)

        validator = QtGui.QDoubleValidator()

        self.generate_new_building_name_label = QtGui.QLabel("Name: ")
        self.generate_new_building_name_line_edit = QtGui.QLineEdit()
        self.generate_new_building_name_line_edit.setObjectName(
            "generate_new_building_name_line_edit")

        self.generate_new_building_street_label = QtGui.QLabel("Street/Nr: ")
        self.generate_new_building_street_line_edit = QtGui.QLineEdit()
        self.generate_new_building_street_line_edit.setObjectName(
            "generate_new_building_street_line_edit")

        self.generate_new_building_city_label = QtGui.QLabel("ZIP/City: ")
        self.generate_new_building_city_line_edit = QtGui.QLineEdit()
        self.generate_new_building_city_line_edit.setObjectName(
            "generate_new_building_city_line_edit")

        self.generate_new_building_constr_year_label = QtGui.QLabel(
             "Contruction Year: ")
        self.generate_new_building_constr_year_line_edit = QtGui.QLineEdit()
        self.generate_new_building_constr_year_line_edit.setValidator(
             validator)
        self.generate_new_building_constr_year_line_edit.setObjectName(
            "generate_new_building_constr_year_line_edit")

        self.generate_new_building_number_of_floors_label = QtGui.QLabel(
             "Number of Floors: ")
        self.generate_new_building_number_of_floors_line_edit =\
            QtGui.QLineEdit()
        self.generate_new_building_number_of_floors_line_edit.setValidator(
             validator)
        self.generate_new_building_number_of_floors_line_edit.setObjectName(
            "generate_new_building_number_of_floors_line_edit")

        self.generate_new_building_height_of_floors_label = QtGui.QLabel(
             "Height of Floors: ")
        self.generate_new_building_height_of_floors_line_edit =\
            QtGui.QLineEdit()
        self.generate_new_building_height_of_floors_line_edit.setValidator(
             validator)
        self.generate_new_building_height_of_floors_line_edit.setObjectName(
            "generate_new_building_height_of_floors_line_edit")

        self.generate_new_building_net_leased_area_label = QtGui.QLabel(
             "Net leased Area: ")
        self.generate_new_building_net_leased_area_line_edit =\
            QtGui.QLineEdit()
        self.generate_new_building_net_leased_area_line_edit.setValidator(
             validator)
        self.generate_new_building_net_leased_area_line_edit.setObjectName(
            ".generate_new_building_net_leased_area_line_edit")

        self.generate_new_building_save_button = QtGui.QPushButton()
        self.generate_new_building_save_button.setText("Save")
        self.connect(self.generate_new_building_save_button, SIGNAL(
            "clicked()"), self.check_new_building_inputs)
        self.connect(self.generate_new_building_save_button, SIGNAL(
            "clicked()"), self.generate_new_building_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_building_cancel_button = QtGui.QPushButton()
        self.generate_new_building_cancel_button.setText("Cancel")
        self.connect(self.generate_new_building_cancel_button, SIGNAL(
            "clicked()"), self.generate_new_building_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_name_label, 0, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_name_line_edit, 0, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_street_label, 1, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_street_line_edit, 1, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_city_label, 2, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_city_line_edit, 2, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_constr_year_label, 3, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_constr_year_line_edit, 3, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_number_of_floors_label, 4, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_number_of_floors_line_edit, 4, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_height_of_floors_label, 5, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_height_of_floors_line_edit, 5, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_net_leased_area_label, 6, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_net_leased_area_line_edit, 6, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_save_button, 7, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_cancel_button, 7, 1)
        self.generate_new_building_ui_page.setWindowModality(
            Qt.ApplicationModal)
        self.generate_new_building_ui_page.show()

    def create_new_element_ui(self):
        '''New element window

        opens the window to create a new element.
        '''

        self.create_new_element_ui_page = QtGui.QWizardPage()
        self.create_new_element_ui_page.setWindowIcon(self.teaser_icon)
        self.create_new_element_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.create_new_element_ui_page.setWindowTitle("Create new Element")
        self.create_new_element_ui_page.setFixedWidth(350)
        self.create_new_element_ui_page.setFixedHeight(200)
        self.generate_new_element_window_layout = QtGui.QGridLayout()
        self.create_new_element_ui_page.setLayout(
            self.generate_new_element_window_layout)
        self.generate_new_element_name_label = QtGui.QLabel("Id: ")
        self.generate_new_element_name_line_edit = QtGui.QLineEdit()
        self.generate_new_element_name_line_edit.setObjectName(
            "generate_new_element_name_line_edit")
        self.generate_new_element_type_label = QtGui.QLabel("Type: ")
        self.generate_new_element_type_combobox = QtGui.QComboBox()
        self.generate_new_element_type_combobox.setObjectName(
            "generate_new_element_type_line_edit")
        self.generate_new_element_type_combobox.addItem(
            "Inner Wall", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "Outer Wall", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "Window", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "GroundFloor", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "Rooftop", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "Ceiling", userData=None)
        self.generate_new_element_type_combobox.addItem(
            "Floor", userData=None)
        self.generate_new_element_area_label = QtGui.QLabel("Area: ")
        self.generate_new_element_area_line_edit = QtGui.QLineEdit()
        self.generate_new_element_area_line_edit.setObjectName(
            "generate_new_element_area_line_edit")

        self.generate_new_element_save_button = QtGui.QPushButton()
        self.generate_new_element_save_button.setText("Save")
        self.connect(self.generate_new_element_save_button, SIGNAL(
            "clicked()"), self.check_new_element_inputs)
        self.connect(self.generate_new_element_save_button, SIGNAL(
            "clicked()"), self.create_new_element_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_element_cancel_button = QtGui.QPushButton()
        self.generate_new_element_cancel_button.setText("Cancel")
        self.connect(self.generate_new_element_cancel_button, SIGNAL(
            "clicked()"), self.create_new_element_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_name_label, 1, 0)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_name_line_edit, 1, 1)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_type_label, 2, 0)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_type_combobox, 2, 1)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_area_label, 3, 0)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_area_line_edit, 3, 1)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_save_button, 4, 0)
        self.generate_new_element_window_layout.addWidget(
            self.generate_new_element_cancel_button, 4, 1)
        self.create_new_element_ui_page.setWindowModality(
            Qt.ApplicationModal)
        self.create_new_element_ui_page.show()

    def create_new_envelope_ui(self):
        '''New envelope window

        opens the window to create a new envelope.
        '''

        self.create__envelope_ui = WizardPage()
        self.create__envelope_ui.setWindowIcon(self.teaser_icon)
        self.create__envelope_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.create__envelope_ui.setWindowTitle("Set all construction")
        self.create__envelope_ui.setFixedWidth(400)
        self.create__envelope_ui.setFixedHeight(600)
        self.create__envelope_ui_window_layout = QtGui.QGridLayout()
        self.create__envelope_ui.setLayout(
            self.create__envelope_ui_window_layout)
        self.warning_message_groupbox_layout = QtGui.QGridLayout()
        self.warning_message_groupbox = QtGui.QGroupBox(
            u"Warning")
        self.warning_message_groupbox.setAlignment(0x0004)
        self.warning_message_groupbox.setGeometry(
            QtCore.QRect(0, 0, 60, 60))
        self.warning_message_groupbox.setLayout(
            self.warning_message_groupbox_layout)
        self.warning_message_label = QtGui.QLabel(
            self.warning_message_groupbox)
        self.warning_message_label.setText(
            "All walls with the current orientation in building will be" +
            " overwritten")
        self.warning_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_message_groupbox.setMaximumHeight(48)
        self.warning_message_groupbox.setMinimumHeight(48)
        self.warning_message_groupbox_layout.addWidget(
            self.warning_message_label, 0, 0)
        self.set_all_constr_element_layout = QtGui.QGridLayout()
        self.set_all_constr_element_layout_groupBox = QtGui.QGroupBox(
            "Input values")
        self.set_all_constr_element_layout_groupBox.setLayout(
            self.set_all_constr_element_layout)

        validator = QtGui.QDoubleValidator()

        self.set_all_constr_element_bldg_label = QtGui.QLabel("Building")
        self.set_all_constr_element_bldg_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_bldg_textbox.setText(
            self.current_building.name)
        self.set_all_constr_element_bldg_textbox.setReadOnly(True)
        self.set_all_constr_element_bldg_textbox.setMaximumHeight(24)

        self.set_all_constr_element_orientation_label = QtGui.QLabel(
            "Orientation")
        self.set_all_constr_element_orientation_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_orientation_textbox.setText(
            self.envelope_orientation_combobox.currentText())
        self.set_all_constr_element_orientation_textbox.setReadOnly(True)
        self.set_all_constr_element_orientation_textbox.setMaximumHeight(24)

        self.set_all_constr_element_type_label = QtGui.QLabel("Type")
        self.set_all_constr_element_type_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_type_textbox.setText(
            self.envelope_type_textbox.text())
        self.set_all_constr_element_type_textbox.setReadOnly(True)
        self.set_all_constr_element_type_textbox.setMaximumHeight(24)

        self.set_all_constr_element_tilt_label = QtGui.QLabel("Tilt")
        self.set_all_constr_element_tilt_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_tilt_textbox.setValidator(validator)
        self.set_all_constr_element_tilt_textbox.setMaximumHeight(24)

        self.set_all_constr_element_inner_con_label = QtGui.QLabel(
            "Inner Convection")
        self.set_all_constr_element_inner_con_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_inner_con_textbox.setValidator(validator)
        self.set_all_constr_element_inner_con_textbox.setMaximumHeight(24)

        self.set_all_constr_element_inner_rad_label = QtGui.QLabel(
            "Inner Radiation")
        self.set_all_constr_element_inner_rad_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_inner_rad_textbox.setValidator(validator)
        self.set_all_constr_element_inner_rad_textbox.setMaximumHeight(24)

        self.set_all_constr_element_outer_con_label = QtGui.QLabel(
            "Outer Convection")
        self.set_all_constr_element_outer_con_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_outer_con_textbox.setValidator(validator)
        self.set_all_constr_element_outer_con_textbox.setMaximumHeight(24)

        self.set_all_constr_element_outer_rad_label = QtGui.QLabel(
            "Outer Radiation")
        self.set_all_constr_element_outer_rad_textbox = QtGui.QLineEdit()
        self.set_all_constr_element_outer_rad_textbox.setValidator(validator)
        self.set_all_constr_element_outer_rad_textbox.setMaximumHeight(24)
        self.set_all_constr_save_cancel_layout = QtGui.QGridLayout()
        self.set_all_constr_save_cancel_layout_GroupBox = QtGui.QGroupBox()
        self.set_all_constr_save_cancel_layout_GroupBox.setLayout(
            self.set_all_constr_save_cancel_layout)
        self.set_all_constr_save_cancel_layout_GroupBox.setMaximumHeight(48)

        self.set_all_constr_element_add_material_button = QtGui.QPushButton()
        self.set_all_constr_element_add_material_button.setText("Add Layer")
        self.connect(self.set_all_constr_element_add_material_button,
                     SIGNAL("clicked()"),
                     lambda check_window="set all construction window":
                     self.create_new_layer_ui(check_window))

        self.set_all_constr_element_delete_material_button =\
            QtGui.QPushButton()
        self.set_all_constr_element_delete_material_button.setText(
            "Delete Layer")
        self.connect(self.set_all_constr_element_delete_material_button,
                     SIGNAL("clicked()"),
                     self.delete_selected_layer_set_all_constr)

        self.set_all_constr_element_material_list_view = QtGui.QListView()
        self.set_all_constr_element_material_list_view.setGeometry(
            QtCore.QRect(10, 200, 170, 300))
        self.set_all_constr_element_material_list_view.setObjectName(
            _fromUtf8("ElementMaterialsListViewSetAllConstr"))
        self.set_all_constr_element_material_list_view.setModel(
            self.element_layer_model_set_all_constr)
        self.set_all_constr_element_material_list_view.setItemDelegate(
            self.lVZF)
        self.set_all_constr_element_material_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.set_all_constr_element_material_list_view.doubleClicked.connect(
            self.show_layer_build_ui)

        self.set_all_constr_save_button = QtGui.QPushButton()
        self.set_all_constr_save_button.setText("Save")

        self.connect(self.set_all_constr_save_button, SIGNAL("clicked()"),
                     self.save_input_values_set_all_constr)
        self.connect(self.set_all_constr_save_button, SIGNAL("clicked()"),
                     self.clear_input_values_set_all_constr)
        self.connect(self.set_all_constr_save_button, SIGNAL("clicked()"),
                     self.create__envelope_ui, QtCore.SLOT("close()"))

        self.set_all_constr_cancel_button = QtGui.QPushButton()
        self.set_all_constr_cancel_button.setText("Cancel")
        self.connect(self.set_all_constr_cancel_button, SIGNAL("clicked()"),
                     self.clear_input_values_set_all_constr)
        self.connect(self.set_all_constr_cancel_button, SIGNAL("clicked()"),
                     self.create__envelope_ui, QtCore.SLOT("close()"))

        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_bldg_label, 1, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_bldg_textbox, 1, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_orientation_label, 2, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_orientation_textbox, 2, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_type_label, 3, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_type_textbox, 3, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_tilt_label, 4, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_tilt_textbox, 4, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_inner_con_label, 5, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_inner_con_textbox, 5, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_inner_rad_label, 6, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_inner_rad_textbox, 6, 1)
        if self.set_all_constr_element_type_textbox.text() != "Ground Floor":
            self.set_all_constr_element_layout.addWidget(
                self.set_all_constr_element_outer_con_label, 7, 0)
            self.set_all_constr_element_layout.addWidget(
                self.set_all_constr_element_outer_con_textbox, 7, 1)
            self.set_all_constr_element_layout.addWidget(
                self.set_all_constr_element_outer_rad_label, 8, 0)
            self.set_all_constr_element_layout.addWidget(
                self.set_all_constr_element_outer_rad_textbox, 8, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_add_material_button, 9, 0)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_delete_material_button, 9, 1)
        self.set_all_constr_element_layout.addWidget(
            self.set_all_constr_element_material_list_view, 10, 0, 11, 2)

        self.set_all_constr_save_cancel_layout.addWidget(
            self.set_all_constr_save_button,
            0, 0)
        self.set_all_constr_save_cancel_layout.addWidget(
            self.set_all_constr_cancel_button,
            0, 1)

        self.create__envelope_ui_window_layout.addWidget(
            self.warning_message_groupbox, 0, 0)
        self.create__envelope_ui_window_layout.addWidget(
            self.set_all_constr_element_layout_groupBox, 1, 0)
        self.create__envelope_ui_window_layout.addWidget(
            self.set_all_constr_save_cancel_layout_GroupBox, 2, 0)

        self.create__envelope_ui.closeEvent(
            self, elem_layer=self.element_layer_model_set_all_constr,
            layer_list=self.all_constr_layer_list)
        self.create__envelope_ui.setWindowModality(Qt.ApplicationModal)
        self.create__envelope_ui.show()

    def create_new_layer_ui(self, check):
        '''New layer window

        opens the window to create a new layer.

        Parameters
        ----------

        check : string
            checks in which window this method is called.
        '''

        self.create_layer_ui = QtGui.QWizardPage()
        self.create_layer_ui.setWindowIcon(self.teaser_icon)
        self.create_layer_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.create_layer_ui.setWindowTitle("Layer Details")
        self.create_layer_ui.setFixedWidth(450)
        self.create_layer_ui.setFixedHeight(300)
        self.create_layer_ui_window_layout = QtGui.QGridLayout()
        self.create_layer_ui.setLayout(self.create_layer_ui_window_layout)
        self.materials = Controller.get_materials_from_file(self.project)
        self.is_switchable = False

        self.new_layer_general_layout = QtGui.QGridLayout()
        self.new_layer_general_layout_group_box = \
            QtGui.QGroupBox("Layer Values")
        self.new_layer_general_layout_group_box.setLayout(
            self.new_layer_general_layout)

        self.new_layer_position_label = QtGui.QLabel("Position")
        self.new_layer_position_combobox = QtGui.QComboBox()

        if check == "Element Details Window":
            num_layers = len(self.current_element.layer) + 1
        elif check == "set all construction window":
            num_layers = len(self.all_constr_layer_list) + 1
        elif check == "Update XML":
            num_layers = len(self.xml_layer_list) + 1
        elif check == "xml_modify_layer_window":
            num_layers = len(self.current_wall.layer) + 1

        if num_layers > 1:
            for x in range(0, num_layers):
                self.new_layer_position_combobox.addItem(
                    str(x), userData=None)
        else:
            self.new_layer_position_combobox.addItem(
                "0", userData=None)
        self.new_layer_position_combobox.setCurrentIndex(num_layers - 1)

        self.new_layer_thickness_label = QtGui.QLabel("Layer Thickness")
        self.new_layer_thickness_textbox = QtGui.QLineEdit()
        self.new_layer_thickness_textbox.setObjectName(
            _fromUtf8("ThicknessTextBox"))

        self.new_layer_material_density_label = QtGui.QLabel("Density")
        self.new_layer_material_density_textbox = QtGui.QLineEdit()
        self.new_layer_material_density_textbox.setObjectName(
            _fromUtf8("MaterialDensityTextBox"))

        self.new_layer_material_thermal_conduc_label = \
            QtGui.QLabel("ThermalConduc")
        self.new_layer_material_thermal_conduc_textbox = QtGui.QLineEdit()
        self.new_layer_material_thermal_conduc_textbox.setObjectName(
            _fromUtf8("MaterialThermalConducTextBox"))

        self.new_layer_material_heat_capac_label = QtGui.QLabel("HeatCapac")
        self.new_layer_material_heat_capac_textbox = QtGui.QLineEdit()
        self.new_layer_material_heat_capac_textbox.setObjectName(
            _fromUtf8("MaterialHeatCapacTextBox"))

        self.new_layer_material_solar_absorp_label = \
            QtGui.QLabel("SolarAbsorp")
        self.new_layer_material_solar_absorp_textbox = QtGui.QLineEdit()
        self.new_layer_material_solar_absorp_textbox.setObjectName(
            _fromUtf8("MaterialSolarAbsorpTextBox"))

        self.new_layer_material_ir_emissivity_label = \
            QtGui.QLabel("IrEmissivity")
        self.new_layer_material_ir_emissivity_textbox = QtGui.QLineEdit()
        self.new_layer_material_ir_emissivity_textbox.setObjectName(
            _fromUtf8("MaterialIrEmissivityTextBox"))

        self.new_layer_material_transmittance_label = \
            QtGui.QLabel("Transmittance")
        self.new_layer_material_transmittance_textbox = QtGui.QLineEdit()
        self.new_layer_material_transmittance_textbox.setObjectName(
            _fromUtf8("MaterialTransmittanceTextBox"))

        self.new_layer_material_label = QtGui.QLabel("Material")
        self.new_layer_material_combobox = QtGui.QComboBox()
        self.connect(self.new_layer_material_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.load_material)
        temp_list = []
        for material in self.materials:
            if material.name not in temp_list:
                temp_list.append(material.name)
        self.new_layer_material_combobox.addItems(sorted(temp_list))
        self.is_switchable = True

        self.new_layer_save_button = QtGui.QPushButton()
        self.new_layer_save_button.setText("Save")
        self.connect(self.new_layer_save_button, SIGNAL(
            "clicked()"), lambda check_window=check:
            self.check_new_layer_inputs(check_window))

        if check == "Element Details Window":
            self.connect(self.new_layer_save_button, SIGNAL(
                "clicked()"), self.update_element_details)

        elif check == "set all construction window":
            self.connect(self.new_layer_save_button, SIGNAL(
                "clicked()"), self.update_set_all_construction)

        elif check == "Update XML":
            self.connect(self.new_layer_save_button, SIGNAL(
                "clicked()"), self.update_xml_window)

        elif check == "xml_modify_layer_window":
                self.connect(self.new_layer_save_button, SIGNAL(
                "clicked()"), self.update_xml_window_modify)

        self.connect(self.new_layer_save_button, SIGNAL(
            "clicked()"), self.create_layer_ui, QtCore.SLOT("close()"))

        self.new_layer_cancel_button = QtGui.QPushButton()
        self.new_layer_cancel_button.setText("Cancel")
        self.connect(self.new_layer_cancel_button, SIGNAL(
            "clicked()"), self.create_layer_ui, QtCore.SLOT("close()"))

        self.new_layer_general_layout.addWidget(
            self.new_layer_position_label, 1, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_position_combobox, 1, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_thickness_label, 2, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_thickness_textbox, 2, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_label, 3, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_combobox, 3, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_density_label, 4, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_density_textbox, 4, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_thermal_conduc_label, 5, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_thermal_conduc_textbox, 5, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_heat_capac_label, 6, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_heat_capac_textbox, 6, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_solar_absorp_label, 7, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_solar_absorp_textbox, 7, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_ir_emissivity_label, 8, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_ir_emissivity_textbox, 8, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_transmittance_label, 9, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_material_transmittance_textbox, 9, 1)
        self.new_layer_general_layout.addWidget(
            self.new_layer_save_button, 10, 0)
        self.new_layer_general_layout.addWidget(
            self.new_layer_cancel_button, 10, 1)

        self.create_layer_ui_window_layout.addWidget(
            self.new_layer_general_layout_group_box)
        self.create_layer_ui.setWindowModality(Qt.ApplicationModal)
        self.create_layer_ui.show()

    def click_radio_button_add(self):
        self.create_new_xml_ui_groupbox.setVisible(True)
        self.generate_new_xml_save_cancel_layout_GroupBox.setVisible(True)
        self.xml_ui_modify_groupbox.setVisible(False)
        self.modify_xml_save_cancel_layout_groupBox.setVisible(False)

    def click_radio_button_modify(self):
        self.xml_ui_modify_groupbox.setVisible(True)
        self.modify_xml_save_cancel_layout_groupBox.setVisible(True)
        self.create_new_xml_ui_groupbox.setVisible(False)
        self.generate_new_xml_save_cancel_layout_GroupBox.setVisible(False)

    def create_xml_ui(self):
        '''New element window

        opens the window to create a new element.
        '''
        self.create_new_xml_ui_page = QtGui.QWizardPage()
        self.create_new_xml_ui_page.setWindowIcon(self.teaser_icon)
        self.create_new_xml_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.create_new_xml_ui_page.setWindowTitle("Update")
        self.create_new_xml_ui_page.setFixedWidth(380)
        self.create_new_xml_ui_page.setFixedHeight(500)
        self.create_new_xml_ui_layout = QtGui.QGridLayout()
        self.create_new_xml_ui_page.setLayout(
            self.create_new_xml_ui_layout)
        self.connect(self.create_new_xml_ui_page, SIGNAL("destroyed()"),
                     lambda check_window="Update XML":
                     self.delete_elements_in_lists(check_window))
        self.generate_new_xml_window_layout = QtGui.QGridLayout()
        self.create_new_xml_ui_groupbox = QtGui.QGroupBox(u"Values")
        self.create_new_xml_ui_groupbox.setLayout(
            self.generate_new_xml_window_layout)
        self.thermalZoneFromXML = Controller.get_elements_from_file(
                                                self.project)

        self.generate_new_xml_options_layout = QtGui.QGridLayout()
        self.generate_new_xml_options_groupbox = QtGui.QGroupBox()
        self.generate_new_xml_options_groupbox.setLayout(
            self.generate_new_xml_options_layout)
        self.generate_new_xml_options_groupbox.setMaximumHeight(48)

        self.radio_button_xml_add = QtGui.QRadioButton(u"Add")
        self.radio_button_xml_add.setChecked(True)
        self.radio_button_xml_add.toggled.connect(self.click_radio_button_add)
        self.radio_button_xml_modify = QtGui.QRadioButton(u"Modify")
        self.radio_button_xml_modify.toggled.connect(
            self.click_radio_button_modify)

        self.generate_new_xml_ui_path_label = QtGui.QLabel("Path: ")
        self.generate_new_xml_ui_path_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_path_line_edit.setObjectName(
            "generate_new_xml_ui_path_line_edit")
        self.generate_new_xml_ui_path_line_edit.setText(
            utilitis.get_full_path("Data\Input\InputData\TypeBuildingElements.xml"))
        self.generate_new_xml_ui_browse = QtGui.QPushButton("Browse")
        self.connect(self.generate_new_xml_ui_browse, SIGNAL(
            "clicked()"), self.click_browse_button_xml)
        self.generate_new_xml_ui_type_label = QtGui.QLabel("Type: ")
        self.generate_new_xml_ui_type_combobox = QtGui.QComboBox()
        self.generate_new_xml_ui_type_combobox.setObjectName(
            "generate_new_xml_ui_type_combobox")
        self.generate_new_xml_ui_type_combobox.addItem("Inner Wall")
        self.generate_new_xml_ui_type_combobox.addItem("Outer Wall")
        self.generate_new_xml_ui_type_combobox.addItem("Window")
        self.generate_new_xml_ui_type_combobox.addItem("GroundFloor")
        self.generate_new_xml_ui_type_combobox.addItem("Rooftop")
        self.generate_new_xml_ui_type_combobox.addItem("Ceiling")
        self.generate_new_xml_ui_type_combobox.addItem("Floor")
        self.generate_new_xml_ui_constr_type_label = QtGui.QLabel(
            "Construction type: ")
        self.generate_new_xml_ui_constr_type_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_constr_type_line_edit.setObjectName(
            "generate_new_xml_ui_constr_type_line_edit")
        self.generate_new_xml_ui_age_group_label = QtGui.QLabel(
            "Building age group: ")
        self.generate_new_xml_ui_age_group_left_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_age_group_left_line_edit.setObjectName(
            "generate_new_xml_ui_age_group_left_line_edit")
        self.generate_new_xml_ui_to_label = QtGui.QLabel("to: ")
        self.generate_new_xml_ui_age_group_left_line_edit.setMaximumWidth(100)
        self.generate_new_xml_ui_age_group_right_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_age_group_right_line_edit.setObjectName(
            "generate_new_xml_ui_age_group_right__line_edit ")
        self.generate_new_xml_ui_age_group_right_line_edit.setMaximumWidth(100)
        self.generate_new_xml_ui_age_group_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_age_group_line_edit.setObjectName(
            "generate_new_xml_ui_age_group_line_edit")
        self.generate_new_xml_ui_inner_convection_label = QtGui.QLabel(
            "Inner convection: ")
        self.generate_new_xml_ui_inner_convection_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_inner_convection_line_edit.setObjectName(
            "generate_new_xml_ui_inner_convection_line_edit")
        self.generate_new_xml_ui_outer_convection_label = QtGui.QLabel(
            "Outer convection: ")
        self.generate_new_xml_ui_outer_convection_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_outer_convection_line_edit.setObjectName(
            "generate_new_xml_ui_outer_convection_line_edit")
        self.generate_new_xml_ui_inner_radiation_label = QtGui.QLabel(
            "Inner radiation ")
        self.generate_new_xml_ui_inner_radiation_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_inner_radiation_line_edit.setObjectName(
            "generate_new_xml_ui_inner_radiation_line_edit")
        self.generate_new_xml_ui_outer_radiation_label = QtGui.QLabel(
            "Outer radiation: ")
        self.generate_new_xml_ui_outer_radiation_line_edit = QtGui.QLineEdit()
        self.generate_new_xml_ui_outer_radiation_line_edit.setObjectName(
            "generate_new_xml_ui_outer_radiation_line_edit")

        self.generate_new_xml_ui_add_layer_button = QtGui.QPushButton()
        self.generate_new_xml_ui_add_layer_button.setText("Add Layer")
        self.connect(self.generate_new_xml_ui_add_layer_button,
                     SIGNAL("clicked()"),
                     lambda check_window="Update XML":
                     self.create_new_layer_ui(check_window))

        self.generate_new_xml_ui_delete_layer_button = QtGui.QPushButton()
        self.generate_new_xml_ui_delete_layer_button.setText("Delete Layer")
        self.connect(self.generate_new_xml_ui_delete_layer_button, SIGNAL(
            "clicked()"), self.delete_selected_layer_xml_window)

        self.generate_new_xml_ui_material_list_view = QtGui.QListView()
        self.generate_new_xml_ui_material_list_view.setGeometry(
            QtCore.QRect(10, 200, 170, 300))
        self.generate_new_xml_ui_material_list_view.setObjectName(
            _fromUtf8("XMLMaterialsListView"))
        self.generate_new_xml_ui_material_list_view.setModel(
            self.element_layer_model_update_xml)
        self.generate_new_xml_ui_material_list_view.setItemDelegate(
            self.lVZF)
        self.generate_new_xml_ui_material_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.generate_new_xml_ui_material_list_view.doubleClicked.connect(
            self.show_layer_build_ui)

        self.generate_new_xml_save_cancel_layout = QtGui.QGridLayout()
        self.generate_new_xml_save_cancel_layout_GroupBox = QtGui.QGroupBox()
        self.generate_new_xml_save_cancel_layout_GroupBox.setLayout(
            self.generate_new_xml_save_cancel_layout)
        self.generate_new_xml_save_cancel_layout_GroupBox.setMaximumHeight(48)

        self.generate_new_xml_ui_save_button = QtGui.QPushButton()
        self.generate_new_xml_ui_save_button.setText("Save")
        self.connect(self.generate_new_xml_ui_save_button, SIGNAL(
            "clicked()"), self.add_element_to_xml)
        self.connect(self.generate_new_xml_ui_save_button, SIGNAL(
            "clicked()"), self.create_new_xml_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_xml_ui_cancel_button = QtGui.QPushButton()
        self.generate_new_xml_ui_cancel_button.setText("Cancel")
        self.connect(self.generate_new_xml_ui_cancel_button, SIGNAL(
            "clicked()"), self.create_new_xml_ui_page,
            QtCore.SLOT("close()"))

        self.xml_window_layout_modify = QtGui.QGridLayout()
        self.xml_ui_modify_groupbox = QtGui.QGroupBox(u"Values")
        self.xml_ui_modify_groupbox.setLayout(
                   self.xml_window_layout_modify)
        self.xml_ui_modify_groupbox.setVisible(False)

        self.xml_ui_del_button = QtGui.QPushButton()
        self.xml_ui_del_button.setText("Delete")
        self.connect(self.xml_ui_del_button, SIGNAL("clicked()"),
                     self.delete_wall_in_xml)
        self.xml_ui_del_button.setMinimumWidth(340)

        self.xml_ui_wall_list_view = QtGui.QListView()
        self.xml_ui_wall_list_view.setGeometry(
            QtCore.QRect(10, 200, 170, 300))
        self.xml_ui_wall_list_view.setObjectName(
            _fromUtf8("XMLElementListView"))
        self.xml_ui_wall_list_view.setModel(
            self.element_model_update_xml)
        self.xml_ui_wall_list_view.setItemDelegate(
            self.lVZF)
        self.xml_ui_wall_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.xml_ui_wall_list_view.doubleClicked.connect(
                    self.show_wall_build_ui)

        self.update_wall_details()

        self.modify_xml_save_cancel_layout = QtGui.QGridLayout()
        self.modify_xml_save_cancel_layout_groupBox = QtGui.QGroupBox()
        self.modify_xml_save_cancel_layout_groupBox.setLayout(
            self.modify_xml_save_cancel_layout)
        self.modify_xml_save_cancel_layout_groupBox.setMaximumHeight(48)

        self.modify_xml_ui_save_button = QtGui.QPushButton()
        self.modify_xml_ui_save_button.setText("Save")
        self.connect(self.modify_xml_ui_save_button, SIGNAL(
            "clicked()"), self.delete_element_in_xml)
        self.connect(self.modify_xml_ui_save_button, SIGNAL(
            "clicked()"), self.create_new_xml_ui_page,
            QtCore.SLOT("close()"))

        self.modify_xml_ui_cancel_button = QtGui.QPushButton()
        self.modify_xml_ui_cancel_button.setText("Cancel")
        self.connect(self.modify_xml_ui_cancel_button, SIGNAL(
            "clicked()"), self.create_new_xml_ui_page,
            QtCore.SLOT("close()"))

        self.generate_new_xml_options_layout.addWidget(
            self.radio_button_xml_add, 1, 0, Qt.AlignLeft)
        # self.generate_new_xml_options_layout.addWidget(
        #    self.radio_button_xml_delete, 1, 1)
        self.generate_new_xml_options_layout.addWidget(
            self.radio_button_xml_modify, 1, 1, Qt.AlignRight)

        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_path_label, 1, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_path_line_edit, 1, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_browse, 2, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_type_label, 3, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_type_combobox, 3, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_constr_type_label, 4, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_constr_type_line_edit, 4, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_age_group_label, 5, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_age_group_left_line_edit, 5, 1,
            Qt.AlignLeft)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_to_label, 5, 1, Qt.AlignCenter)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_age_group_right_line_edit, 5, 1,
            Qt.AlignRight)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_inner_convection_label, 6, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_inner_convection_line_edit, 6, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_outer_convection_label, 7, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_outer_convection_line_edit, 7, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_inner_radiation_label, 8, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_inner_radiation_line_edit, 8, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_outer_radiation_label, 9, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_outer_radiation_line_edit, 9, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_add_layer_button, 10, 0)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_delete_layer_button, 10, 1)
        self.generate_new_xml_window_layout.addWidget(
            self.generate_new_xml_ui_material_list_view, 11, 0, 12, 2)

        self.xml_window_layout_modify.addWidget(
                self.xml_ui_wall_list_view, 1, 0, 2, 2)
        self.xml_window_layout_modify.addWidget(
                self.xml_ui_del_button, 0, 0, 1, 1)

        self.generate_new_xml_save_cancel_layout.addWidget(
            self.generate_new_xml_ui_save_button, 1, 0)
        self.generate_new_xml_save_cancel_layout.addWidget(
            self.generate_new_xml_ui_cancel_button, 1, 1)

        self.modify_xml_save_cancel_layout.addWidget(
            self.modify_xml_ui_save_button, 1, 0)
        self.modify_xml_save_cancel_layout.addWidget(
            self.modify_xml_ui_cancel_button, 1, 1)

        self.create_new_xml_ui_layout.addWidget(
            self.generate_new_xml_options_groupbox, 0, 0)
        self.create_new_xml_ui_layout.addWidget(
            self.create_new_xml_ui_groupbox, 1, 0)
        self.create_new_xml_ui_layout.addWidget(
            self.xml_ui_modify_groupbox, 1, 0)
        self.create_new_xml_ui_layout.addWidget(
            self.generate_new_xml_save_cancel_layout_GroupBox, 2, 0)
        self.create_new_xml_ui_layout.addWidget(
            self.modify_xml_save_cancel_layout_groupBox, 2, 0)
        self.create_new_xml_ui_page.setWindowModality(
            Qt.ApplicationModal)
        self.create_new_xml_ui_page.show()

    def generate_type_building_ui(self):
        '''New type building window

        opens a window to create a new type building.
        '''

        self.popup_window_type_building = QtGui.QWizardPage()
        self.popup_window_type_building.setWindowIcon(self.teaser_icon)
        self.current_type_building = "Office"
        self.popup_window_type_building.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.popup_window_type_building.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.popup_window_type_building.setWindowTitle(
            u"generate " + self.current_type_building + " ...")
        self.popup_window_type_building.setFixedWidth(520)
        self.popup_window_type_building.setFixedHeight(800)
        self.popup_layout_type_building = QtGui.QGridLayout()
        self.popup_window_type_building.setLayout(
            self.popup_layout_type_building)
        self.group_box_type_building_sidecontrols = QtGui.QGroupBox(
            u"General Information")
        self.group_box_type_building_right_office = QtGui.QGroupBox(
            u"Specific Type Building Information")
        self.group_box_type_building_right_residential = QtGui.QGroupBox(
            u"Specific Type Building Information")

        self.window_construct_building_type_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_type_label.setGeometry(
            QtCore.QRect(10, 25, 90, 25))
        self.window_construct_building_type_label.setText("Type Building:")
        self.window_construct_building_combo_box = QtGui.QComboBox(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_combo_box.setGeometry(
            QtCore.QRect(110, 25, 120, 25))
        for type_building in self.guiinfo.type_buildings:
            self.window_construct_building_combo_box.addItem(type_building)
        self.connect(self.window_construct_building_combo_box, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_type_building)
        self.window_construct_building_name_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_name_label.setGeometry(
            QtCore.QRect(10, 65, 90, 25))
        self.window_construct_building_name_label.setText("Name:")
        self.window_construct_building_name_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_name_line_edit.setGeometry(
            QtCore.QRect(110, 65, 120, 25))
        self.window_construct_building_street_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_street_label.setGeometry(
            QtCore.QRect(10, 105, 90, 25))
        self.window_construct_building_street_label.setText("Street/Nr.:")
        self.window_construct_building_street_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_street_line_edit.setGeometry(
            QtCore.QRect(110, 105, 120, 25))
        self.window_construct_building_location_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_location_label.setGeometry(
            QtCore.QRect(10, 145, 90, 25))
        self.window_construct_building_location_label.setText("ZIP/City:")
        self.window_construct_building_location_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_location_line_edit.setGeometry(
            QtCore.QRect(110, 145, 120, 25))
        self.window_construct_building_year_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_year_label.setGeometry(
            QtCore.QRect(10, 185, 90, 25))
        self.window_construct_building_year_label.setText("Construction Year:")
        self.window_construct_building_year_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_year_line_edit.setGeometry(
            QtCore.QRect(110, 185, 120, 25))
        self.window_construct_building_number_of_floors_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_number_of_floors_label.setGeometry(
            QtCore.QRect(10, 225, 90, 25))
        self.window_construct_building_number_of_floors_label.setText(
            "Number of Floors:")
        self.window_construct_building_number_of_floors_line_edit = \
            QtGui.QLineEdit(self.group_box_type_building_sidecontrols)
        self.window_construct_building_number_of_floors_line_edit.setGeometry(
            QtCore.QRect(110, 225, 120, 25))
        self.window_construct_building_height_of_floors_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_height_of_floors_label.setGeometry(
            QtCore.QRect(10, 265, 90, 25))
        self.window_construct_building_height_of_floors_label.setText(
            "Height of Floors:")
        self.window_construct_building_height_of_floors_line_edit = \
            QtGui.QLineEdit(self.group_box_type_building_sidecontrols)
        self.window_construct_building_height_of_floors_line_edit.setGeometry(
            QtCore.QRect(110, 265, 120, 25))
        self.window_construct_building_area_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_area_label.setGeometry(
            QtCore.QRect(10, 305, 90, 25))
        self.window_construct_building_area_label.setText("Net leased Area:")
        self.window_construct_building_area_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_area_line_edit.setGeometry(
            QtCore.QRect(110, 305, 120, 25))
        self.test_button = QtGui.QPushButton(
            self.group_box_type_building_sidecontrols)
        self.test_button.setText("Generate random parameters")
        self.test_button.setGeometry(QtCore.QRect(10, 345, 230, 25))
        self.connect(self.test_button,
                     QtCore.SIGNAL("clicked()"),
                     self.fill_random_parameters)
        self.fill_button = QtGui.QPushButton(
            self.group_box_type_building_sidecontrols)
        self.fill_button.setText("Fill current building Information")
        self.fill_button.setGeometry(QtCore.QRect(10, 375, 230, 25))
        self.connect(self.fill_button, QtCore.SIGNAL("clicked()"),
                     self.fill_building_informations)

        # Differentiates between the different types of buildings from combobox
        self.type_building_office_layout = QtGui.QGridLayout()
        self.group_box_type_building_right_office.setLayout(
            self.type_building_office_layout)

        self.group_box_office_layout = QtGui.QGroupBox(u"Layout")
        self.group_box_office_window_area = QtGui.QGroupBox(u"Window Layout")
        self.group_box_office_architecture = QtGui.QGroupBox(
            u"Construction Type")

        self.office_layout = QtGui.QGridLayout()
        self.office_layoutWindowArea = QtGui.QGridLayout()
        self.office_layout_architecture = QtGui.QGridLayout()

        self.group_box_office_layout.setLayout(self.office_layout)
        self.group_box_office_window_area.setLayout(
            self.office_layoutWindowArea)
        self.group_box_office_architecture.setLayout(
            self.office_layout_architecture)

        self.radio_button_office_layout_1 = QtGui.QRadioButton(
            u"Elongated, 1 floor")
        self.radio_button_office_layout_2 = QtGui.QRadioButton(
            u"Elongated, 2 floors")
        self.radio_button_office_layout_3 = QtGui.QRadioButton(
            u"Compact")
        self.radio_button_office_layout_1.setChecked(True)

        self.picture_layout_office_1 = QtGui.QLabel()
        self.picture_layout_office_2 = QtGui.QLabel()
        self.picture_layout_office_3 = QtGui.QLabel()
        self.picture_layout_office_1.setPixmap(
            QtGui.QPixmap(utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/elongated_1floor.png")).scaled(
                    70, 70))
        self.picture_layout_office_2.setPixmap(
            QtGui.QPixmap(utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/elongated_2floors.png")).scaled(
                    70, 70))
        self.picture_layout_office_3.setPixmap(QtGui.QPixmap(
            utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/compact_floor.png")).scaled(
                    70, 70))
        self.office_layout.addWidget(
            self.radio_button_office_layout_1, 1, 0)
        self.office_layout.addWidget(
            self.radio_button_office_layout_2, 2, 0)
        self.office_layout.addWidget(
            self.radio_button_office_layout_3, 3, 0)
        self.office_layout.addWidget(
            self.picture_layout_office_1, 1, 1, Qt.AlignRight)
        self.office_layout.addWidget(
            self.picture_layout_office_2, 2, 1, Qt.AlignRight)
        self.office_layout.addWidget(
            self.picture_layout_office_3, 3, 1, Qt.AlignRight)

        self.radio_button_window_area_office_1 = QtGui.QRadioButton(

            u"Use default values")
        self.radio_button_window_area_office_2 = QtGui.QRadioButton(

            u"Punctuated facade")
        self.radio_button_window_area_office_3 = QtGui.QRadioButton(

            u"Banner facade")
        self.radio_button_window_area_office_4 = QtGui.QRadioButton(

            u"Full glazing")
        self.radio_button_window_area_office_1.setChecked(True)

        self.picture_window_area_office_2 = QtGui.QLabel()
        self.picture_window_area_office_3 = QtGui.QLabel()
        self.picture_window_area_office_4 = QtGui.QLabel()
        self.picture_window_area_office_2.setPixmap(QtGui.QPixmap(
            utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/punctuatedFacade.png"))
            .scaled(70, 70))
        self.picture_window_area_office_3.setPixmap(QtGui.QPixmap(
            utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/bannerFacade.png"))
            .scaled(70, 70))
        self.picture_window_area_office_4.setPixmap(QtGui.QPixmap(
            utilitis.get_full_path(
                "GUI/GUIImages/OfficeBuildings/fullGlazing.png"))
            .scaled(70, 70))
        self.office_layoutWindowArea.addWidget(
            self.radio_button_window_area_office_1, 1, 0)
        self.office_layoutWindowArea.addWidget(
            self.radio_button_window_area_office_2, 2, 0)
        self.office_layoutWindowArea.addWidget(
            self.radio_button_window_area_office_3, 3, 0)
        self.office_layoutWindowArea.addWidget(
            self.radio_button_window_area_office_4, 4, 0)
        self.office_layoutWindowArea.addWidget(
            self.picture_window_area_office_2, 2, 1, Qt.AlignRight)
        self.office_layoutWindowArea.addWidget(
            self.picture_window_area_office_3, 3, 1, Qt.AlignRight)
        self.office_layoutWindowArea.addWidget(
            self.picture_window_area_office_4, 4, 1, Qt.AlignRight)

        self.radio_button_architecture_office_1 = QtGui.QRadioButton(
            u"Heavy")
        self.radio_button_architecture_office_2 = QtGui.QRadioButton(
            u"Light")
        self.radio_button_architecture_office_1.setChecked(True)

        self.office_layout_architecture.addWidget(
            self.radio_button_architecture_office_1, 1, 0)
        self.office_layout_architecture.addWidget(
            self.radio_button_architecture_office_2, 2, 0)

        self.update_building_button = QtGui.QPushButton()
        self.update_building_button.setText("Update current Building")
        self.connect(self.update_building_button, SIGNAL(
            "clicked()"), self.update_building)

        self.connect(self.update_building_button, SIGNAL("clicked()"),
                     self.popup_window_type_building, QtCore.SLOT("close()"))

        self.construct_type_building_button = QtGui.QPushButton(
            u"Generate " + self.current_type_building + " Building")
        self.connect(self.construct_type_building_button, SIGNAL(
            "clicked()"), self.check_inputs_typebuilding)

        self.connect(self.construct_type_building_button, SIGNAL(
            "clicked()"), self.popup_window_type_building,
            QtCore.SLOT("close()"))
        self.type_building_residential_layout = QtGui.QGridLayout()
        self.group_box_type_building_right_residential.setLayout(
            self.type_building_residential_layout)

        self.group_box_residential_neighbour_buildings = QtGui.QGroupBox(
            u"Direct neighbour buildings")
        self.group_box_residential_layout = QtGui.QGroupBox(u"Layout")
        self.group_box_residential_roof = QtGui.QGroupBox(u"Roof")
        self.group_box_residential_basement = QtGui.QGroupBox(u"Basement")
        self.group_box_residential_architecture = QtGui.QGroupBox(
            u"Construction Type")
        self.group_box_residential_architecture.setVisible(False)

        self.layout_residential_neighbour_buildings = QtGui.QGridLayout()
        self.layout_residential_layout = QtGui.QGridLayout()
        self.layout_residential_roof = QtGui.QGridLayout()
        self.layout_residential_basement = QtGui.QGridLayout()
        self.layout_residential_architecture = QtGui.QGridLayout()

        self.group_box_residential_neighbour_buildings.setLayout(
            self.layout_residential_neighbour_buildings)
        self.group_box_residential_layout.setLayout(
            self.layout_residential_layout)
        self.group_box_residential_roof.setLayout(
            self.layout_residential_roof)
        self.group_box_residential_basement.setLayout(
            self.layout_residential_basement)
        self.group_box_residential_architecture.setLayout(
            self.layout_residential_architecture)

        self.radio_button_neighbour_1 = QtGui.QRadioButton(

            u"No neighbour")
        self.radio_button_neighbour_2 = QtGui.QRadioButton(

            u"One neighbour")
        self.radio_button_neighbour_3 = QtGui.QRadioButton(
            u"Two neighbours")
        self.radio_button_neighbour_1.setChecked(True)

        self.picture_neighbour_building_residential_1 = QtGui.QLabel()
        self.picture_neighbour_building_residential_2 = QtGui.QLabel()
        self.picture_neighbour_building_residential_3 = QtGui.QLabel()
        self.picture_neighbour_building_residential_1.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "noNeighbour.png")).scaled(29, 23))
        self.picture_neighbour_building_residential_2.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "oneNeighbour.png")).scaled(46, 23))
        self.picture_neighbour_building_residential_3.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "twoNeighbours.png")).scaled(56, 23))
        self.layout_residential_neighbour_buildings.addWidget(
            self.radio_button_neighbour_1, 1, 0)
        self.layout_residential_neighbour_buildings.addWidget(
            self.radio_button_neighbour_2, 2, 0)
        self.layout_residential_neighbour_buildings.addWidget(
            self.radio_button_neighbour_3, 3, 0)
        self.layout_residential_neighbour_buildings.addWidget(
            self.picture_neighbour_building_residential_1, 1, 1,
            Qt.AlignRight)
        self.layout_residential_neighbour_buildings.addWidget(
            self.picture_neighbour_building_residential_2, 2, 1,
            Qt.AlignRight)
        self.layout_residential_neighbour_buildings.addWidget(
            self.picture_neighbour_building_residential_3, 3, 1,
            Qt.AlignRight)

        self.radio_button_residential_layout_1 = QtGui.QRadioButton(
            u"Compact")
        self.radio_button_residential_layout_2 = QtGui.QRadioButton(
            u"Elongated/Complex")
        self.radio_button_residential_layout_1.setChecked(True)

        self.picture_layout_residential_1 = QtGui.QLabel()
        self.picture_layout_residential_2 = QtGui.QLabel()
        self.picture_layout_residential_1.setPixmap(QPixmap(

            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "compact.png")).scaled(28, 28))
        self.picture_layout_residential_2.setPixmap(QPixmap(

            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "elongatedComplex.png")).scaled(28, 28))
        self.layout_residential_layout.addWidget(
            self.radio_button_residential_layout_1, 1, 0)
        self.layout_residential_layout.addWidget(
            self.radio_button_residential_layout_2, 2, 0)
        self.layout_residential_layout.addWidget(
            self.picture_layout_residential_1, 1, 1, Qt.AlignRight)
        self.layout_residential_layout.addWidget(
            self.picture_layout_residential_2, 2, 1, Qt.AlignRight)

        self.radio_button_residential_roof_1 = QtGui.QRadioButton(
            u"Flat Roof")
        self.radio_button_residential_roof_2 = QtGui.QRadioButton(
            u"Non heated attic")
        self.radio_button_residential_roof_3 = QtGui.QRadioButton(
            u"Partly heated attic")
        self.radio_button_residential_roof_4 = QtGui.QRadioButton(
            u"Heated attic")
        self.radio_button_residential_roof_1.setChecked(True)

        self.h_line_roof = QtGui.QFrame()
        self.h_line_roof.setFrameShape(QtGui.QFrame.HLine)
        self.h_line_roof.setFrameShadow(QtGui.QFrame.Sunken)
        self.check_box_button_roof = QtGui.QCheckBox(
            u"Dormer or similar installations")
        self.picture_roof_residential_1 = QtGui.QLabel()
        self.picture_roof_residential_2 = QtGui.QLabel()
        self.picture_roof_residential_3 = QtGui.QLabel()
        self.picture_roof_residential_4 = QtGui.QLabel()
        self.picture_roof_residential_1.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "flatRoof.png")).scaled(32, 23))
        self.picture_roof_residential_2.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "nonHeatedAttic.png")).scaled(34, 23))
        self.picture_roof_residential_3.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "partyHeatedAttic.png")).scaled(34, 23))
        self.picture_roof_residential_4.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "heatedAttic.png")).scaled(34, 23))
        self.layout_residential_roof.addWidget(
            self.radio_button_residential_roof_1, 1, 0)

        self.layout_residential_roof.addWidget(
            self.radio_button_residential_roof_2, 2, 0)

        self.layout_residential_roof.addWidget(
            self.radio_button_residential_roof_3, 3, 0)

        self.layout_residential_roof.addWidget(
            self.radio_button_residential_roof_4, 4, 0)

        self.layout_residential_roof.addWidget(
            self.picture_roof_residential_1, 1, 1, Qt.AlignRight)

        self.layout_residential_roof.addWidget(
            self.picture_roof_residential_2, 2, 1, Qt.AlignRight)

        self.layout_residential_roof.addWidget(
            self.picture_roof_residential_3, 3, 1, Qt.AlignRight)

        self.layout_residential_roof.addWidget(
            self.picture_roof_residential_4, 4, 1, Qt.AlignRight)

        self.layout_residential_roof.addWidget(
            self.h_line_roof, 5, 0, 1, 0)

        self.layout_residential_roof.addWidget(
            self.check_box_button_roof, 6, 0, 1, 1)

        self.radio_button_residential_basement_1 = QtGui.QRadioButton(
            u"No cellar")
        self.radio_button_residential_basement_2 = QtGui.QRadioButton(
            u"Non heated cellar")
        self.radio_button_residential_basement_3 = QtGui.QRadioButton(
            u"Partly heated cellar")
        self.radio_button_residential_basement_4 = QtGui.QRadioButton(
            u"Heated cellar")
        self.radio_button_residential_basement_1.setChecked(True)

        self.picture_residential_basement_1 = QtGui.QLabel()
        self.picture_residential_basement_2 = QtGui.QLabel()
        self.picture_residential_basement_3 = QtGui.QLabel()
        self.picture_residential_basement_4 = QtGui.QLabel()
        self.picture_residential_basement_1.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "noCellar.png")).scaled(32, 28))
        self.picture_residential_basement_2.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "nonHeatedCellar.png")).scaled(32, 28))
        self.picture_residential_basement_3.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "partlyHeatedCellar.png")).scaled(32, 28))
        self.picture_residential_basement_4.setPixmap(QPixmap(
            utilitis.get_full_path("GUI/GUIImages/Residentials/"
                                 "heatedCellar.png")).scaled(32, 28))
        self.layout_residential_basement.addWidget(
            self.radio_button_residential_basement_1, 1, 0)
        self.layout_residential_basement.addWidget(
            self.radio_button_residential_basement_2, 2, 0)
        self.layout_residential_basement.addWidget(
            self.radio_button_residential_basement_3, 3, 0)
        self.layout_residential_basement.addWidget(
            self.radio_button_residential_basement_4, 4, 0)
        self.layout_residential_basement.addWidget(
            self.picture_residential_basement_1, 1, 1, Qt.AlignRight)
        self.layout_residential_basement.addWidget(
            self.picture_residential_basement_2, 2, 1, Qt.AlignRight)
        self.layout_residential_basement.addWidget(
            self.picture_residential_basement_3, 3, 1, Qt.AlignRight)
        self.layout_residential_basement.addWidget(
            self.picture_residential_basement_4, 4, 1, Qt.AlignRight)
        self.radio_button_residential_architecture_1 = QtGui.QRadioButton(
            u"Heavy")
        self.radio_button_residential_architecture_2 = QtGui.QRadioButton(
            u"Light")
        self.radio_button_residential_architecture_1.setChecked(True)

        self.layout_residential_architecture.addWidget(
            self.radio_button_residential_architecture_1, 1, 0)
        self.layout_residential_architecture.addWidget(
            self.radio_button_residential_architecture_2, 2, 0)
        self.popup_layout_type_building.addWidget(
            self.group_box_type_building_sidecontrols, 0, 0, 5, 3)
        self.popup_layout_type_building.addWidget(
            self.group_box_office_architecture, 5, 0, 1, 3)
        self.type_building_office_layout.addWidget(
            self.group_box_office_layout, 0, 0, 1, 1)
        self.type_building_office_layout.addWidget(
            self.group_box_office_window_area, 3, 0, 1, 1)

        self.type_building_residential_layout.addWidget(
            self.group_box_residential_neighbour_buildings, 0, 0, 1, 1)
        self.type_building_residential_layout.addWidget(
            self.group_box_residential_layout, 1, 0, 1, 1)
        self.type_building_residential_layout.addWidget(
            self.group_box_residential_roof, 2, 0, 1, 1)
        self.type_building_residential_layout.addWidget(
            self.group_box_residential_basement, 3, 0, 1, 1)
        self.popup_layout_type_building.addWidget(
            self.group_box_residential_architecture, 5, 0, 1, 3)
        self.popup_layout_type_building.addWidget(
            self.group_box_type_building_right_office, 0, 3, 6, 1)
        self.popup_layout_type_building.addWidget(
            self.group_box_type_building_right_residential, 0, 3, 6, 1)
        self.group_box_type_building_right_residential.setVisible(False)
        self.popup_layout_type_building.addWidget(
            self.update_building_button, 6, 0, 1, 4)
        self.popup_layout_type_building.addWidget(
            self.construct_type_building_button, 7, 0, 1, 4)
        self.popup_window_type_building.setLayout(
            self.popup_layout_type_building)
        self.popup_window_type_building.setWindowModality(Qt.ApplicationModal)
        self.popup_window_type_building.show()

    def generate_zone_ui(self):
        '''New zone window

        opens a window to create a new zone.
        '''

        self.generate_zone_ui_page = QtGui.QWizardPage()
        self.generate_zone_ui_page.setWindowIcon(self.teaser_icon)
        self.generate_zone_ui_page.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.generate_zone_ui_page.setWindowTitle("Create new Zone")
        self.generate_zone_ui_page.setFixedWidth(350)
        self.generate_zone_ui_page.setFixedHeight(200)
        self.generate_zone_window_layout = QtGui.QGridLayout()
        self.generate_zone_ui_page.setLayout(self.generate_zone_window_layout)

        self.generate_zone_name_label = QtGui.QLabel("Name: ")
        self.generate_zone_name_line_edit = QtGui.QLineEdit()
        self.generate_zone_name_line_edit.setObjectName(
            "generate_zone_name_line_edit")

        self.generate_zone_area_label = QtGui.QLabel("Area: ")
        self.generate_zone_area_line_edit = QtGui.QLineEdit()
        self.generate_zone_area_line_edit.setObjectName(
            "generate_zone_area_line_edit")

        self.generate_zone_usage_label = QtGui.QLabel("Type: ")
        self.generate_zone_usage_combobox = QtGui.QComboBox()
        self.generate_zone_usage_combobox.setObjectName(
            "generate_zone_usage_combobox")
        for zone_type in self.guiinfo.thermal_zone_types:
            self.generate_zone_usage_combobox.addItem(zone_type)

        self.generate_zone_save_button = QtGui.QPushButton()
        self.generate_zone_save_button.setText("Save")
        self.connect(self.generate_zone_save_button, SIGNAL(
            "clicked()"), self.check_inputs_new_zone)
        self.connect(self.generate_zone_save_button, SIGNAL(
            "clicked()"), self.generate_zone_ui_page, QtCore.SLOT("close()"))

        self.generate_zone_cancel_button = QtGui.QPushButton()
        self.generate_zone_cancel_button.setText("Cancel")
        self.connect(self.generate_zone_cancel_button, SIGNAL("clicked()"),
                     self.generate_zone_ui_page, QtCore.SLOT("close()"))

        self.generate_zone_window_layout.addWidget(
            self.generate_zone_name_label, 1, 0)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_name_line_edit, 1, 1)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_area_label, 2, 0)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_area_line_edit, 2, 1)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_usage_label, 3, 0)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_usage_combobox, 3, 1)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_save_button, 4, 0)
        self.generate_zone_window_layout.addWidget(
            self.generate_zone_cancel_button, 4, 1)
        self.generate_zone_ui_page.setWindowModality(Qt.ApplicationModal)
        self.generate_zone_ui_page.show()

    def save_changed_layer_values(self):
        '''Saves layer inputs

        replaces the previous values of the current layer with the inputs
        from the text fields.
        '''

        for zone in self.current_building.thermal_zones:
            if zone.internal_id == self.current_zone.internal_id:
                for element in zone.inner_walls:
                    if element.internal_id == self.current_element.internal_id:
                        for layer in element.layer:
                            if layer.internal_id == self.current_layer.\
                                    internal_id:
                                layer.thickness = self.thickness_textbox.text()
                                layer.material.name = \
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    self.material_density_textbox.text()
                                layer.material.thermal_conduc = \
                                    self.material_thermal_conduc_textbox.text()
                                layer.material.heat_capac = \
                                    self.material_heat_capac_textbox.text()
                                layer.material.solar_absorp = \
                                    self.material_solar_absorp_textbox.text()
                                layer.material.ir_emissivity = \
                                    self.material_ir_emissivity_textbox.text()
                                layer.material.transmittance = \
                                    self.material_transmittance_textbox.text()
                                break
                for element in zone.outer_walls:
                    if element.internal_id == self.current_element.internal_id:
                        for layer in element.layer:
                            if layer.internal_id == self.current_layer.\
                                    internal_id:
                                layer.thickness = self.thickness_textbox.text()
                                layer.material.name = \
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    self.material_density_textbox.text()
                                layer.material.thermal_conduc = \
                                    self.material_thermal_conduc_textbox.text()
                                layer.material.heat_capac = \
                                    self.material_heat_capac_textbox.text()
                                layer.material.solar_absorp = \
                                    self.material_solar_absorp_textbox.text()
                                layer.material.ir_emissivity = \
                                    self.material_ir_emissivity_textbox.text()
                                layer.material.transmittance = \
                                    self.material_transmittance_textbox.text()
                                break
                for element in zone.windows:
                    if element.internal_id == self.current_element.internal_id:
                        for layer in element.layer:
                            if layer.internal_id == self.current_layer.\
                                    internal_id:
                                layer.thickness = self.thickness_textbox.text()
                                layer.material.name = \
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    self.material_density_textbox.text()
                                layer.material.thermal_conduc = \
                                    self.material_thermal_conduc_textbox.text()
                                layer.material.heat_capac = \
                                    self.material_heat_capac_textbox.text()
                                layer.material.solar_absorp = \
                                    self.material_solar_absorp_textbox.text()
                                layer.material.ir_emissivity = \
                                    self.material_ir_emissivity_textbox.text()
                                layer.material.transmittance = \
                                    self.material_transmittance_textbox.text()
                                break

    def save_changed_layer_values_set_all_constr(self):
        '''Saves the layer inputs in set all construction window

        replaces the previous values of the current layer in envelope with
        the inputs from the text fields in set all construction window.
        '''

        for layer in self.all_constr_layer_list:
                if layer.internal_id == self.current_layer.internal_id:
                                layer.thickness = self.thickness_textbox.text()
                                layer.material.name =\
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    self.material_density_textbox.text()
                                layer.material.thermal_conduc = \
                                    self.material_thermal_conduc_textbox.text()
                                layer.material.heat_capac = \
                                    self.material_heat_capac_textbox.text()
                                layer.material.solar_absorp = \
                                    self.material_solar_absorp_textbox.text()
                                layer.material.ir_emissivity = \
                                    self.material_ir_emissivity_textbox.text()
                                layer.material.transmittance = \
                                    self.material_transmittance_textbox.text()
                                break

    def save_changed_layer_values_xml(self):
        '''Saves the layer inputs in set all construction window

        replaces the previous values of the current layer in envelope with
        the inputs from the text fields in set all construction window.
        '''

        for layer in self.xml_layer_list:
                if layer.internal_id == self.current_layer.internal_id:
                                layer.thickness = self.thickness_textbox.text()
                                layer.material.name =\
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    self.material_density_textbox.text()
                                layer.material.thermal_conduc = \
                                    self.material_thermal_conduc_textbox.text()
                                layer.material.heat_capac = \
                                    self.material_heat_capac_textbox.text()
                                layer.material.solar_absorp = \
                                    self.material_solar_absorp_textbox.text()
                                layer.material.ir_emissivity = \
                                    self.material_ir_emissivity_textbox.text()
                                layer.material.transmittance = \
                                    self.material_transmittance_textbox.text()
                                break
                            
    def save_changed_layer_values_xml_modify(self):
        '''Saves the layer inputs in set all construction window
        replaces the previous values of the current layer in envelope with
        the inputs from the text fields in set all construction window.
        '''
    
        for layer in self.current_wall.layer:
                if layer.id == self.current_layer.id:
                                layer.thickness = float(self.thickness_textbox.text())
                                layer.material.name =\
                                    self.material_combobox.currentText()
                                layer.material.density = \
                                    float(self.material_density_textbox.text())
                                layer.material.thermal_conduc = \
                                    float(self.material_thermal_conduc_textbox.text())
                                layer.material.heat_capac = \
                                    float(self.material_heat_capac_textbox.text())
                                layer.material.solar_absorp = \
                                    float(self.material_solar_absorp_textbox.text())
                                layer.material.ir_emissivity = \
                                    float(self.material_ir_emissivity_textbox.text())
                                #layer.Material.transmittance = \
                                #    float(self.material_transmittance_textbox.text())
                                break

    def save_changed_simulation_values(self):
        '''Saves the inputs in the simulation window

        replaces the previous values of the current project with the inputs
        from the text fields in the simulation window.

        '''

        self.project.name = self.project_name_lineedit.text()
        self.project.modelica_info.runtime_simulation =\
            self.simulation_runtime_lineedit.text()
        self.project.modelica_info.interval_output =\
            self.simulation_interval_output_lineedit.text()
        self.project.modelica_info.current_solver =\
            self.simulation_solver_combobox.currentText()
        if self.simulation_equidistant_output_checkbox.isChecked():
            self.project.modelica_info.equidistant_output = True
        else:
            self.project.modelica_info.equidistant_output = False

    def save_changed_element_values(self):
        '''Saves element inputs

        replaces the previous values of the current element with the inputs
        from the text fields.
        '''

        for zone in self.current_building.thermal_zones:
            if zone.internal_id == self.current_zone.internal_id:
                for element in zone.inner_walls:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.inner_walls.index(element)
                        zone.inner_walls[index].name = \
                            str(self.element_name_textbox.text())
                        zone.inner_walls[index].construction_type = \
                            str(self.element_construction_type_combobox.
                                currentText())
                        zone.inner_walls[index].orientation = \
                            self.guiinfo.orientations_strings[
                            str(self.element_orientation_combobox.
                                currentText())]
                        zone.inner_walls[index].area = \
                            str(self.element_area_textbox.text())
                        zone.inner_walls[index].year_of_construction = \
                            str(self.element_year_of_construction_textbox.
                                text())
                        zone.inner_walls[index].year_of_retrofit = \
                            str(self.element_year_of_retrofit_textbox.text())
                        zone.inner_walls[index].tilt = \
                            str(self.element_tilt_textbox.text())
                        zone.inner_walls[index].inner_convection = \
                            str(self.element_inner_convection_textbox.text())
                        zone.inner_walls[index].inner_radiation = \
                            str(self.element_inner_radiation_textbox.text())
                for element in zone.outer_walls:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.outer_walls.index(element)
                        zone.outer_walls[index].name = \
                            str(self.element_name_textbox.text())
                        zone.outer_walls[index].construction_type = \
                            str(self.element_construction_type_combobox.
                                currentText())
                        zone.outer_walls[index].orientation = \
                            self.guiinfo.orientations_strings[
                            self.element_orientation_combobox.currentText()]
                        zone.outer_walls[index].area = \
                            str(self.element_area_textbox.text())
                        zone.outer_walls[index].year_of_construction = \
                            str(self.element_year_of_construction_textbox.
                                text())
                        zone.outer_walls[index].year_of_retrofit = \
                            str(self.element_year_of_retrofit_textbox.text())
                        zone.outer_walls[index].tilt = \
                            str(self.element_tilt_textbox.text())
                        zone.outer_walls[index].inner_convection = \
                            str(self.element_inner_convection_textbox.text())
                        zone.outer_walls[index].inner_radiation = \
                            str(self.element_inner_radiation_textbox.text())
                        zone.outer_walls[index].outer_convection = \
                            float(self.element_outer_convection_textbox.text())
                        zone.outer_walls[index].outer_radiation = \
                            float(self.element_outer_radiation_textbox.text())
                        break
                for element in zone.windows:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.windows.index(element)
                        zone.windows[index].name = \
                            str(self.element_name_textbox.text())
                        zone.windows[index].construction_type = \
                            str(self.element_construction_type_combobox.
                                currentText())
                        zone.windows[index].orientation = \
                            self.guiinfo.orientations_strings[
                            self.element_orientation_combobox.currentText()]
                        zone.windows[index].area = \
                            str(self.element_area_textbox.text())
                        zone.windows[index].year_of_construction = \
                            str(self.element_year_of_construction_textbox.
                                text())
                        zone.windows[index].year_of_retrofit = \
                            str(self.element_year_of_retrofit_textbox.text())
                        zone.windows[index].tilt = \
                            str(self.element_tilt_textbox.text())
                        zone.windows[index].inner_convection = \
                            str(self.element_inner_convection_textbox.text())
                        zone.windows[index].inner_radiation = \
                            str(self.element_inner_radiation_textbox.text())
                        zone.windows[index].outer_convection = \
                            float(self.element_outer_convection_textbox.text())
                        zone.windows[index].outer_radiation = \
                            float(self.element_outer_radiation_textbox.text())
                        break

    def save_input_values_set_all_constr(self):
        '''Saves element inputs in the set all construction window

        replaces the previous values of the current element with the inputs
        from the text fields in the set all construction window
        '''

        bldg = self.current_building
        orientation = int(self.guiinfo.orientations_strings[
                          str(self.set_all_constr_element_orientation_textbox.
                              text())])
        element_type = self.set_all_constr_element_type_textbox.text()

        tilt = float(self.set_all_constr_element_tilt_textbox.text())
        inner_con = float(self.set_all_constr_element_inner_con_textbox.text())
        inner_rad = float(self.set_all_constr_element_inner_rad_textbox.text())

        if element_type != "Ground Floor":
            if(element_type == "Outer Wall"):
                element_type = "OuterWall"
            outer_con = float(self.set_all_constr_element_outer_con_textbox.
                              text())
            outer_rad = float(self.set_all_constr_element_outer_rad_textbox.
                              text())
        elif element_type == "Ground Floor":
            element_type = "GroundFLoor"
            outer_con = None
            outer_rad = None
        layer_set = self.all_constr_layer_list

        Controller.click_change_all_constr(bldg, orientation, element_type,
                                           tilt, inner_con, inner_rad,
                                           outer_con, outer_rad, layer_set)
        self.display_current_building()

    def save_changed_zone_values(self):
        '''Saves zone values

        updates the displayed details of the currently selected zone after
        changes are saved.
        '''

        self.current_zone.name = self.zone_id_textbox.text()
        self.current_zone.area = self.zone_net_leased_area_textbox.text()
        self.current_zone.use_conditions.usage =\
            self.zone_type_combobox.currentText()
        if str(self.cooling_ahu_start_dropdown.currentText()).startswith('0'):
            self.current_zone.use_conditions.cooling_time[0] = \
                int(self.cooling_ahu_start_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.cooling_time[0] = \
                int(self.cooling_ahu_start_dropdown.currentText()[0] +
                    self.cooling_ahu_start_dropdown.currentText()[1])
        if str(self.cooling_ahu_end_dropdown.currentText()).startswith('0'):
            self.current_zone.use_conditions.cooling_time[1] = \
                int(self.cooling_ahu_end_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.cooling_time[1] = \
                int(self.cooling_ahu_end_dropdown.currentText()[0] +
                    self.cooling_ahu_end_dropdown.currentText()[1])
        if str(self.heating_ahu_start_dropdown.currentText()).startswith('0'):
            self.current_zone.use_conditions.heating_time[0] = \
                int(self.heating_ahu_start_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.heating_time[0] = \
                int(self.heating_ahu_start_dropdown.currentText()[0] +
                    self.heating_ahu_start_dropdown.currentText()[1])
        if str(self.heating_ahu_end_dropdown.currentText()).startswith('0'):
            self.current_zone.use_conditions.heating_time[1] = \
                int(self.heating_ahu_end_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.heating_time[1] = \
                int(self.heating_ahu_end_dropdown.currentText()[0] +
                    self.heating_ahu_end_dropdown.currentText()[1])

        self.current_zone.use_conditions.set_temp_heat = \
            self.set_temp_heat_line_edit.text()
        self.current_zone.use_conditions.set_temp_cool = \
            self.set_temp_cool_line_edit.text()
        self.current_zone.use_conditions.temp_set_back = \
            self.temp_set_back_line_edit.text()
        self.current_zone.use_conditions.min_air_exchange = \
            self.min_air_flow_line_edit.text()
        self.current_zone.use_conditions.min_ahu = \
            self.min_ahu_line_edit.text()
        self.current_zone.use_conditions.max_ahu = \
            self.max_ahu_line_edit.text()
        if self.with_ahu_combobox.currentText() == 'True':
            self.current_zone.use_conditions.with_ahu = True
        else:
            self.current_zone.use_conditions.with_ahu = False
        self.current_zone.use_conditions.rel_humidity = float(
            self.re_humidity_line_edit.text())
        self.current_zone.use_conditions.persons = \
            self.persons_line_edit.text()
        self.current_zone.use_conditions.machines = \
            self.machines_line_edit.text()
        self.current_zone.use_conditions.lighting_power = \
            self.lighting_line_edit.text()

        self.current_zone.t_inside = self.mean_temp_inner_line_edit.text()
        self.current_zone.t_outside = self.mean_temp_outer_line_edit.text()
        self.current_zone.infiltration_rate = \
            self.infiltration_rate_line_edit.text()

        # TODO: Not sure if this for loop is really necessary
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == self.current_zone.internal_id:
                self.current_building.thermal_zones[self.current_building.
                                                    thermal_zones.
                                                    index(zone)] = \
                    self.current_zone

        self.display_current_building()

    def save_changed_envelopes_values(self):
        '''Saves envelope values

        updates the displayed details of the currently selected envelope after
        changes are saved.
        '''

        orientation_before_changing = \
            self.envelope_orientation_before_changing
        orientation_after_changing = \
            str(self.envelope_orientation_combobox.currentText())
        area = float(self.envelope_area_textbox.text())
        if self.current_envelope.startswith("Outer Wall"):
            element_type = "Outer Wall"
        elif self.current_envelope.startswith("Rooftop"):
            element_type = "Rooftop"
        elif self.current_envelope.startswith("Ground Floor"):
            element_type = "Ground Floor"
        elif self.current_envelope.startswith("Window"):
            element_type = "Window"
        if orientation_before_changing == orientation_after_changing:
            if self.current_envelope.startswith("Window"):
                for orientation_value in self.guiinfo.orientations_numbers.\
                                             keys():
                    orientation_string = str(self.guiinfo.orientations_numbers
                                             [orientation_value])
                    if self.envelope_orientation_combobox.currentText() == \
                            orientation_string:
                            self.current_building.set_window_area(
                                float(self.envelope_area_textbox.text()),
                                orientation_value)
            else:
                for orientation_value in self.guiinfo.orientations_numbers.\
                                             keys():
                    orientation_string = str(self.guiinfo.orientations_numbers
                                             [orientation_value])
                    if self.envelope_orientation_combobox.currentText() == \
                            orientation_string:
                            self.current_building.set_outer_wall_area(
                                float(self.envelope_area_textbox.text()),
                                orientation_value)
        else:
            orientation_number_before_changing = \
                self.guiinfo.orientations_strings[orientation_before_changing]
            orientation_number_after_changing = \
                self.guiinfo.orientations_strings[orientation_after_changing]
            Controller.click_save_envelopes(self.current_building,
                                            orientation_number_before_changing,
                                            orientation_number_after_changing,
                                            element_type, area)
        self.display_current_building()

    def add_element_to_xml(self):

        path = str(self.generate_new_xml_ui_path_line_edit.text())
        type_of_element = self.generate_new_xml_ui_type_combobox.currentText()
        constr_type = \
            self.generate_new_xml_ui_constr_type_line_edit.text()
        building_from = float(
            self.generate_new_xml_ui_age_group_left_line_edit.text())
        building_to = float(
            self.generate_new_xml_ui_age_group_right_line_edit.text())
        building_age_group = [building_from, building_to]
        inner_con = float(
            self.generate_new_xml_ui_inner_convection_line_edit.text())
        outer_con = float(
            self.generate_new_xml_ui_outer_convection_line_edit.text())
        inner_rad = float(
            self.generate_new_xml_ui_inner_radiation_line_edit.text())
        outer_rad = float(
            self.generate_new_xml_ui_outer_radiation_line_edit.text())
        layer_set = self.xml_layer_list

        element = Controller.create_element(type_of_element, constr_type,
                                            building_age_group, inner_con,
                                            outer_con, inner_rad, outer_rad,
                                            layer_set)
        Controller.add_element_to_xml(element, path)

    def modify_element_in_xml(self):

        path = str(self.generate_new_xml_ui_path_line_edit.text())
        type_of_element = self.wall_type_line_edit.text()
        if type_of_element == "InnerWall":
            type_of_element = "Inner Wall"
        if type_of_element == "OuterWall":
            type_of_element = "Outer Wall"
        constr_type = \
            self.wall_construction_type_combobox.currentText()
        building_from = float(
            self.wall_Building_age_group_textbox_from.text())
        building_to = float(
            self.wall_Building_age_group_textbox_to.text())
        building_age_group = [building_from, building_to]
        inner_con = float(
            self.wall_inner_convection_textbox.text())
        inner_rad = float(
            self.wall_inner_radiation_textbox.text())
        if type_of_element == "Inner Wall" or "GroundFloor":
            outer_con = 0
            outer_rad = 0

        else:
            outer_con = float(self.wall_outer_convection_textbox.text())
            outer_rad = float(self.wall_outer_radiation_textbox.text())

        layer_set = self.current_wall.layer
        element = Controller.create_element(type_of_element, constr_type,
                                            building_age_group, inner_con,
                                            outer_con, inner_rad, outer_rad,
                                            layer_set)
        Controller.delete_element_in_xml(self.selected_wall, path)
        Controller.add_element_to_xml(element, path)
        self.project.data = self.project.instantiate_data_class()
        self.thermalZoneFromXML = Controller.get_elements_from_file(
                                                self.project)
        self.update_wall_details()

    def delete_element_in_xml(self):
        path = str(self.generate_new_xml_ui_path_line_edit.text())
        Controller.delete_element_in_xml(self.deleted_wall, path=path)
        self.project.data = self.project.instantiate_data_class()

    def clear_input_values_set_all_constr(self):
        '''Clears layer values

        clears the displayed layers of the currently selected envelope after
        changes are saved.
        '''

        # clears the list in python 3
        try:
            self.element_layer_model_set_all_constr.clear()
            self.all_constr_layer_list.clear()
        # clears the list in pyhton 2
        except:
            self.element_layer_model_set_all_constr = QStandardItemModel()
            self.all_constr_layer_list = []

    def clear_focus_line_edits(self):
        self.side_bar_id_line_edit.clearFocus()
        self.side_bar_construction_year_line_edit.clearFocus()
        self.side_bar_height_of_floors_line_edit.clearFocus()
        self.side_bar_location_line_edit.clearFocus()
        self.side_bar_net_leased_area_line_edit.clearFocus()
        self.side_bar_number_of_floors_line_edit.clearFocus()
        self.side_bar_street_line_edit.clearFocus()

    def check_inputs_new_zone(self):
        '''checks inputs of a new zone

        checks if the inputs from the new_zone window fulfill the specified
        criteria of not being empty.
        '''

        if self.generate_zone_name_line_edit.text() == "":
            QtGui.QMessageBox.warning(self,
                                      u"Can't add Zone!",
                                      u"You need to fill out the Name field.")
        if self.generate_zone_area_line_edit.text() == "":
            QtGui.QMessageBox.warning(self,
                                      u"Can't add Zone!",
                                      u"You need to fill out the Area field.")
        if self.generate_zone_usage_combobox.currentText() == "":
            QtGui.QMessageBox.warning(self,
                                      u"Can't add Zone!",
                                      u"You need to fill out the Usage field.")
        if self.generate_zone_name_line_edit.text() != \
            "" and self.generate_zone_area_line_edit.text() != ""\
                and self.generate_zone_usage_combobox.currentText() != "":

            Controller.click_add_zone_button(
                self.current_building,
                self.generate_zone_name_line_edit.text(),
                self.generate_zone_area_line_edit.text(),
                self.generate_zone_usage_combobox.currentText())
            self.display_current_building()

    def check_inputs_edit_element(self):
        '''checks inputs of a element, which is edit

        checks conditions for inputs from the element edit window.
        '''

        self.current_element.name = self.edit_element_name_line_edit.text()
        self.current_element.area = float(
            self.edit_element_area_line_edit.text())
        self.display_current_element()

    def check_inputs_edit_zone(self):
        '''checks inputs of a Zone, which is edit

        checks if all necessary values to edit a given zone are still
        not empty
        '''

        if self.edit_zone_area_line_edit.text() == "":
            self.edit_zone_failed_label.setVisible(True)
            self.edit_zone_area_label = self.set_text_color(
                self.edit_zone_area_label, "red")
            self.edit_zone_failed_label = self.set_text_color(
                self.edit_zone_failed_label, "red")
            self.edit_gen_inf_tab_widget.setCurrentIndex(0)
        else:
            self.edit_zone_area_label = self.set_text_color(
                self.edit_zone_area_label, "black")
        if self.new_zone_name_line_edit.text() == "":
            self.edit_zone_failed_label.setVisible(True)
            self.edit_zone_name_label = self.set_text_color(
                self.edit_zone_name_label, "red")
            self.edit_zone_failed_label = self.set_text_color(
                self.edit_zone_failed_label, "red")
            self.edit_gen_inf_tab_widget.setCurrentIndex(0)
        else:
            self.edit_zone_name_label = self.set_text_color(
                self.edit_zone_name_label, "black")
        if self.edit_zone_volume_line_edit.text() == "":
            self.edit_zone_failed_label.setVisible(True)
            self.edit_zone_volume_label = self.set_text_color(
                self.edit_zone_volume_label, "red")
            self.edit_zone_failed_label = self.set_text_color(
                self.edit_zone_failed_label, "red")
            self.edit_gen_inf_tab_widget.setCurrentIndex(0)
        else:
            self.edit_zone_volume_label = self.set_text_color(
                self.edit_zone_volume_label, "black")
        if self.edit_zone_area_line_edit.text() != ""\
            and self.edit_zone_name_line_edit.text() != ""\
                and self.edit_zone_volume_line_edit.text() != "":

                self.current_zone.area = self.edit_zone_area_line_edit.text()
                self.current_zone.name = self.edit_zone_name_line_edit.text()
                self.current_zone.volume = \
                    self.edit_zone_volume_line_edit.text()
                self.display_current_building()

    def check_inputs_typebuilding(self):
        '''checks inputs of a type building

        checks if all necessary values to create a type building are
        not empty/floats.
        '''

        self.fill_typebuilding_attributes()
        self.project, int_id = Controller.click_generate_type_building_button(
            self.project,
            self.window_construct_building_name_line_edit.text(),
            self.window_construct_building_year_line_edit.text(),
            self.window_construct_building_number_of_floors_line_edit.text(),
            self.window_construct_building_height_of_floors_line_edit.text(),
            self.current_type_building,
            self.window_construct_building_area_line_edit.text(),
            self.window_construct_building_street_line_edit.text(),
            self.window_construct_building_location_line_edit.text(),
            self.type_building_ind_att)

        for building in self.project.buildings:
            if building.internal_id == int_id:
                self.current_building = building
        self.display_current_building()


    def check_new_building_inputs(self):
        ''' Creates a new empty building
        '''

        self.current_building = Controller.click_add_new_building(
            self.project, "temp")
        self.current_building.name = \
            self.generate_new_building_name_line_edit.text()
        self.current_building.street_name = \
            self.generate_new_building_street_line_edit.text()
        self.current_building.city = \
            self.generate_new_building_city_line_edit.text()
        self.current_building.year_of_construction = \
            self.generate_new_building_constr_year_line_edit.text()
        self.current_building.number_of_floors = \
            self.generate_new_building_number_of_floors_line_edit.text()
        self.current_building.height_of_floors = \
            self.generate_new_building_height_of_floors_line_edit.text()
        self.current_building.net_leased_area = \
            self.generate_new_building_net_leased_area_line_edit.text()
        self.project.buildings.append(self.current_building)
        self.display_current_building()

    def check_new_element_inputs(self):
        '''checks inputs of an new element

        checks if all inputed values are correct and then updates
        the list of elements of the currently displayed zone.
        '''

        # TODO: Wir wollten keine Messageboxes mehr, also userinput
        # anders abfangen.

        try:
            float(self.generate_new_element_area_line_edit.text())
        except ValueError:
            QtGui.QMessageBox.warning(
                self, u"Warning", u"Area has to be a number.")
            return

        self.current_zone = Controller.click_add_new_element(
            self.current_zone, self.generate_new_element_name_line_edit.text(),
            self.generate_new_element_type_combobox.currentText(),
            float(self.generate_new_element_area_line_edit.text()))
        self.element_model.clear()

        for inner_wall in self.current_zone.inner_walls:
            if type(inner_wall).__name__ == "InnerWall":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) +
                    "\nType:\t".expandtabs(11) +
                    "Inner Wall \n Area:\t".expandtabs(11) +
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
            if type(inner_wall).__name__ == "Floor":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) +
                    "\nType:\t".expandtabs(11) +
                    "Floor \n Area:\t".expandtabs(11) +
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
            if type(inner_wall).__name__ == "Ceiling":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) +
                    "\nType:\t".expandtabs(11) +
                    "Ceiling \n Area:\t".expandtabs(11) +
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
        for element in self.current_zone.outer_walls:
            if type(element).__name__ == "GroundFloor":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) +
                    str(element.name) +
                    "\nType:\t".expandtabs(11) +
                    "Ground Floor \n Area:\t".expandtabs(11) +
                    str(element.area) +
                    "\n Orientation:\t".expandtabs(11) +
                    str(element.orientation),
                    element.internal_id)
                self.element_model.appendRow(item)
            if type(element).__name__ == "Rooftop":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) +
                    str(element.name) +
                    "\nType:\t".expandtabs(11) +
                    "Rooftop \n Area:\t".expandtabs(11) +
                    str(element.area) +
                    "\n Orientation:\t".expandtabs(11) +
                    str(element.orientation),
                    element.internal_id)
                self.element_model.appendRow(item)
            if type(element).__name__ == "OuterWall":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) +
                    str(element.name) +
                    "\nType:\t".expandtabs(11) +
                    "Outer Wall \n Area:\t".expandtabs(11) +
                    str(element.area) +
                    "\n Orientation:\t".expandtabs(11) +
                    str(element.orientation),
                    element.internal_id)
                self.element_model.appendRow(item)
        for element in self.current_zone.windows:
            item = TrackableItem(
                "Name:\t".expandtabs(8) + str(element.name) +
                "\nType:\t".expandtabs(11) +
                "Window \n Area:\t".expandtabs(11) +
                str(element.area), element.internal_id)
            self.element_model.appendRow(item)

    def check_new_layer_inputs(self, check):
        '''Check inputs of a new layer

        adds a new layer to the current element or envelope and checks if the
        input is correct

        Parameters
        ----------

        check : string
            checks in which window this method is called.
        '''

        if self.new_layer_thickness_textbox.text() is not "":
            thick = float(self.new_layer_thickness_textbox.text())
        else:
            thick = 1
        if self.new_layer_material_density_textbox.text() is not "":
            dens = float(self.new_layer_material_density_textbox.text())
        else:
            dens = 1
        if self.new_layer_material_thermal_conduc_textbox.text() is not "":
            therm = float(
                self.new_layer_material_thermal_conduc_textbox.text())
        else:
            therm = 1
        if self.new_layer_material_heat_capac_textbox.text() is not "":
            heat = float(self.new_layer_material_heat_capac_textbox.text())
        else:
            heat = 1
        if self.new_layer_material_solar_absorp_textbox.text() is not "":
            solar = float(self.new_layer_material_solar_absorp_textbox.text())
        else:
            solar = 1
        if self.new_layer_material_ir_emissivity_textbox.text() is not "":
            ir = float(self.new_layer_material_ir_emissivity_textbox.text())
        else:
            ir = 1
        if self.new_layer_material_transmittance_textbox.text() is not "":
            trans = float(self.new_layer_material_transmittance_textbox.text())
        else:
            trans = 1

        if check == "Element Details Window":
                self.current_element = Controller.click_add_new_layer(
                    self.current_element,
                    int(self.new_layer_position_combobox.currentText()),
                    thick, self.new_layer_material_combobox.currentText(),
                    dens, therm, heat, solar, ir, trans)

        elif check == "set all construction window":
            position = int(self.new_layer_position_combobox.currentText())
            exists = False
            for layer in self.all_constr_layer_list:
                if layer.position == position:
                        exists = True
                if exists:
                    layer.position = layer.position + 1

            self.all_constr_layer_list.insert(position,
                Controller.click_add_new_layer(
                None, int(self.new_layer_position_combobox.currentText()),
                thick, self.new_layer_material_combobox.currentText(), dens,
                therm, heat, solar, ir, trans))

        elif check == "Update XML":
            parent = None
            position = int(self.new_layer_position_combobox.currentText())
            material = self.new_layer_material_combobox.currentText()
            self.xml_layer_list.insert(
                position, Controller.click_add_new_layer(
                                    parent, position, thick, material, dens,
                                    therm, heat, solar, ir, trans))
            self.xml_layer_list[position].id = position + 1

        elif check == "xml_modify_layer_window":
            position = int(self.new_layer_position_combobox.currentText())
            material = self.new_layer_material_combobox.currentText()
            self.current_wall = Controller.click_add_new_layer(
                                        self.current_wall, position, thick,
                                        material, dens, therm, heat, solar,
                                        ir, trans)

    def change_zone_values_ui(self, item):
        '''Displays attributes of a selected zone

        opens a window to see all attributes from the currently selected zone.
        '''

        self.zone_element_model = QStandardItemModel()
        current_item = self.zone_model.itemFromIndex(item)
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == current_item.internal_id:
                self.current_zone = zone
                self.display_current_zone()

        self.zone_value_window = QtGui.QWizardPage()
        self.zone_value_window.setWindowIcon(self.teaser_icon)
        self.zone_value_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.zone_value_window.setWindowTitle("Zone Details")
        self.zone_value_window.setFixedWidth(450)
        self.zone_value_window.setFixedHeight(600)
        self.zone_value_window_layout = QtGui.QGridLayout()
        self.zone_value_window.setLayout(self.zone_value_window_layout)

        self.groupbox_general_zone_values_layout = QtGui.QGroupBox(
            u"General Zone Values")
        self.zone_values_tab = QTabWidget()
        self.groupbox_save_cancel_buttons = QtGui.QGroupBox()
        self.groupbox_zone_usage_layout = QtGui.QGroupBox(u"Usage")
        self.general_zone_values_layout = QtGui.QGridLayout()
        self.element_values_layout = QtGui.QGridLayout()
        self.save_cancel_layout = QtGui.QGridLayout()
        self.zone_usage_times_layout = QtGui.QGridLayout()
        self.zone_usage_layout = QtGui.QGridLayout()
        self.static_heat_layout = QtGui.QGridLayout()
        self.static_heat_layout.setHorizontalSpacing(10)

        tab_1 = QTabWidget()
        tab_2 = QTabWidget()
        tab_3 = QTabWidget()
        tab_4 = QTabWidget()

        self.zone_values_tab.addTab(tab_1, u"     Elements      ")
        self.zone_values_tab.addTab(tab_2, u"      Usage        ")
        self.zone_values_tab.addTab(tab_3, u"   Usage Times     ")
        self.zone_values_tab.addTab(tab_4, u"  Static Heat Load ")
        self.zone_values_tab.setStyleSheet(
            "QTabBar::tab { height: 25px; width: 104px; }")

        self.groupbox_general_zone_values_layout.setLayout(
            self.general_zone_values_layout)
        tab_1.setLayout(self.element_values_layout)
        tab_2.setLayout(self.zone_usage_times_layout)
        tab_3.setLayout(self.zone_usage_layout)
        tab_4.setLayout(self.static_heat_layout)
        self.groupbox_save_cancel_buttons.setLayout(self.save_cancel_layout)

        self.zone_type_label = QtGui.QLabel("Zone Type")

        self.zone_type_combobox = QtGui.QComboBox()
        self.zone_type_combobox.setObjectName(_fromUtf8("ZoneTypeGroupBox"))
        for thermal_zone_type in self.guiinfo.thermal_zone_types:
            self.zone_type_combobox.addItem(thermal_zone_type, userData=None)
        self.zone_type_combobox.setCurrentIndex(
            self.zone_type_combobox.findText(
                str(self.current_zone.use_conditions.usage)))
        self.connect(self.zone_type_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_current_zone_type)

        self.zone_id_label = QtGui.QLabel("Zone Id")
        self.zone_id_textbox = QtGui.QLineEdit()
        self.zone_id_textbox.setObjectName(_fromUtf8("ZoneNameTextBox"))
        self.zone_id_textbox.setText(self.current_zone.name)

        self.zone_net_leased_area_label = QtGui.QLabel("Net leased Area")
        self.zone_net_leased_area_textbox = QtGui.QLineEdit()
        self.zone_net_leased_area_textbox.setObjectName(_fromUtf8(
            "ZoneNetLeasedAreaTextBox"))
        self.zone_net_leased_area_textbox.setText(str(self.current_zone.area))

        self.general_zone_values_layout.addWidget(self.zone_type_label, 1, 0)
        self.general_zone_values_layout.addWidget(
            self.zone_type_combobox, 1, 1)
        self.general_zone_values_layout.addWidget(self.zone_id_label, 2, 0)
        self.general_zone_values_layout.addWidget(self.zone_id_textbox, 2, 1)
        self.general_zone_values_layout.addWidget(
            self.zone_net_leased_area_label, 3, 0)
        self.general_zone_values_layout.addWidget(
            self.zone_net_leased_area_textbox, 3, 1)

        self.zone_element_list_view = QtGui.QListView()
        self.zone_element_list_view.setObjectName(
            _fromUtf8("zone_element_list_view"))
        self.zone_element_list_view.setModel(self.element_model)
        self.zone_element_list_view.setItemDelegate(self.lVZF)
        self.zone_element_list_view.doubleClicked.connect(
            self.show_element_build_ui)
        self.zone_element_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.add_element_button = QtGui.QPushButton()
        self.add_element_button.setText("Add new Element")
        self.connect(self.add_element_button, SIGNAL(
            "clicked()"), self.create_new_element_ui)
        self.delete_element_button = QtGui.QPushButton()
        self.delete_element_button.setText("Delete Element")
        self.connect(self.delete_element_button, SIGNAL(
            "clicked()"), self.delete_current_element)
        self.element_values_layout.addWidget(self.add_element_button, 0, 0)
        self.element_values_layout.addWidget(self.delete_element_button, 0, 1)
        self.element_values_layout.addWidget(self.zone_element_list_view,
                                             1, 0, 1, 2)

        self.cooling_ahu_start_label = QtGui.QLabel("Cooling AHU Start: ")
        self.cooling_ahu_end_label = QtGui.QLabel("End: ")
        self.cooling_ahu_start_dropdown = QtGui.QComboBox()
        self.cooling_ahu_start_dropdown.setMaximumWidth(60)
        self.cooling_ahu_end_dropdown = QtGui.QComboBox()
        self.cooling_ahu_end_dropdown.setMaximumWidth(60)

        self.heating_ahu_start_label = QtGui.QLabel("Heating AHU Start: ")
        self.heating_ahu_end_label = QtGui.QLabel("End: ")
        self.heating_ahu_start_dropdown = QtGui.QComboBox()
        self.heating_ahu_start_dropdown.setMaximumWidth(60)
        self.heating_ahu_end_dropdown = QtGui.QComboBox()
        self.heating_ahu_end_dropdown.setMaximumWidth(60)

        for time in self.guiinfo.hoursInADay:
            self.cooling_ahu_start_dropdown.addItem(time, userData=None)
            self.cooling_ahu_end_dropdown.addItem(time, userData=None)
            self.heating_ahu_start_dropdown.addItem(time, userData=None)
            self.heating_ahu_end_dropdown.addItem(time, userData=None)
            if len(str(self.current_zone.use_conditions.cooling_time[0])) == 1:
                fixed_c_t_s = "0" + str(
                    self.current_zone.use_conditions.cooling_time[0]) + ":00"
            else:
                fixed_c_t_s = str(
                    self.current_zone.use_conditions.cooling_time[0]) + ":00"
            if len(str(self.current_zone.use_conditions.cooling_time[1])) == 1:
                fixed_c_t_e = "0" + str(
                    self.current_zone.use_conditions.cooling_time[1]) + ":00"
            else:
                fixed_c_t_e = str(
                    self.current_zone.use_conditions.cooling_time[1]) + ":00"
            if len(str(self.current_zone.use_conditions.heating_time[0])) == 1:
                fixed_h_t_s = "0" + str(
                    self.current_zone.use_conditions.heating_time[0]) + ":00"
            else:
                fixed_h_t_s = str(
                    self.current_zone.use_conditions.heating_time[0]) + ":00"
            if len(str(self.current_zone.use_conditions.heating_time[1])) == 1:
                fixed_h_t_e = "0" + str(
                    self.current_zone.use_conditions.heating_time[1]) + ":00"
            else:
                fixed_h_t_e = str(
                    self.current_zone.use_conditions.heating_time[1]) + ":00"
            if (time == fixed_c_t_s):
                self.cooling_ahu_start_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_c_t_e):
                self.cooling_ahu_end_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_h_t_s):
                self.heating_ahu_start_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_h_t_e):
                self.heating_ahu_end_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))

        self.zone_element_save_button = QtGui.QPushButton()
        self.zone_element_save_button.setText("Save")
        self.connect(self.zone_element_save_button, SIGNAL(
            "clicked()"), self.save_changed_zone_values)
        self.connect(self.zone_element_save_button, SIGNAL(
            "clicked()"), self.zone_value_window, QtCore.SLOT("close()"))

        self.zone_element_cancel_button = QtGui.QPushButton()
        self.zone_element_cancel_button.setText("Cancel")
        self.connect(self.zone_element_cancel_button, SIGNAL(
            "clicked()"), self.zone_value_window, QtCore.SLOT("close()"))

        self.set_temp_heat_label_1 = QtGui.QLabel("Set Temp Heating: ")
        self.set_temp_heat_line_edit = QtGui.QLineEdit()
        self.set_temp_heat_line_edit.setText(str(
            self.current_zone.use_conditions.set_temp_heat))
        self.set_temp_heat_label_2 = QtGui.QLabel("K")

        self.set_temp_cool_label_1 = QtGui.QLabel("Set Temp Cooling: ")
        self.set_temp_cool_line_edit = QtGui.QLineEdit()
        self.set_temp_cool_line_edit.setText(str(
            self.current_zone.use_conditions.set_temp_cool))
        self.set_temp_cool_label_2 = QtGui.QLabel("K")

        self.temp_set_back_label_1 = QtGui.QLabel("Temp Setback: ")
        self.temp_set_back_line_edit = QtGui.QLineEdit()
        self.temp_set_back_line_edit.setText(str(
            self.current_zone.use_conditions.temp_set_back))
        self.temp_set_back_label_2 = QtGui.QLabel("K")

        self.min_air_flow_label_1 = QtGui.QLabel("Minimal Airflow: ")
        self.min_air_flow_line_edit = QtGui.QLineEdit()
        self.min_air_flow_line_edit.setText(str(
            self.current_zone.use_conditions.min_air_exchange))
        self.min_air_flow_label_2 = QtGui.QLabel("m^3/(h m^2)")

        self.min_ahu_label_1 = QtGui.QLabel("Minimal AHU: ")
        self.min_ahu_line_edit = QtGui.QLineEdit()
        self.min_ahu_line_edit.setText(str(
            self.current_zone.use_conditions.min_ahu))
        self.min_ahu_label_2 = QtGui.QLabel("m^3/(h m^2)")

        self.max_ahu_label_1 = QtGui.QLabel("Maximal AHU: ")
        self.max_ahu_line_edit = QtGui.QLineEdit()
        self.max_ahu_line_edit.setText(str(
            self.current_zone.use_conditions.max_ahu))
        self.max_ahu_label_2 = QtGui.QLabel("m^3/(h m^2)")

        self.with_ahu_label_1 = QtGui.QLabel("With AHU: ")
        self.with_ahu_combobox = QtGui.QComboBox()
        self.with_ahu_combobox.addItem("False", userData=None)
        self.with_ahu_combobox.addItem("True", userData=None)
        if (self.current_zone.use_conditions.with_ahu == "True"):
            self.with_ahu_combobox.setCurrentIndex(
                self.with_ahu_combobox.findText("True"))
        else:
            self.with_ahu_combobox.setCurrentIndex(
                self.with_ahu_combobox.findText("False"))

        self.re_humidity_label_1 = QtGui.QLabel("Relative Humidity: ")
        self.re_humidity_line_edit = QtGui.QLineEdit()
        self.re_humidity_line_edit.setText(str(
            self.current_zone.use_conditions.rel_humidity))
        self.re_humidity_label_2 = QtGui.QLabel("%")

        self.persons_label_1 = QtGui.QLabel("Persons: ")
        self.persons_line_edit = QtGui.QLineEdit()
        self.persons_line_edit.setText(str(
            self.current_zone.use_conditions.persons))
        self.persons_label_2 = QtGui.QLabel("W/m^2")

        self.figure_profiles = plt.figure()
        self.canvas_profiles = FigureCanvas(self.figure_profiles)
        data_persons = [1.0 for x in range(24)]
        data_machines = [1.0 for x in range(24)]
        # TODO: data_lighting = [1.0 for x in range(24)]
        for hour in range(0, 24):
            try:
                data_persons[hour] =\
                    self.current_zone.use_conditions.profile_persons[hour]
                data_machines[hour] =\
                    self.current_zone.use_conditions.profile_machines[hour]
            # TODO: data_lighting[hour] = \
            # self.current_zone.use_conditions.profile_lighting[hour]
            except IndexError:
                break
        ax_p = self.figure_profiles.add_subplot(111)
        ax_p.hold(False)
        ax_p.plot(data_persons, 'b-', data_machines, 'r-')
        # TODO: ax_p.plot(data_persons,
        #                 'b-', data_machines, 'r-', data_lighting, 'g-')
        ax_p.set_ylim([0, 1])
        self.canvas_profiles.draw()
        # TODO: Find a better way to set up a caption to explain the colors
        self.graph_label = QtGui.QLabel("Red: Machines, Blue: Persons")
        # TODO: self.graph_label = QtGui.QLabel("Red: Machines, Blue: Persons"
        #                                         , Green: Lighting)

        self.usagePicPixMap = QtGui.QPixmap("GUI/sheep_PNG2186.png")
        self.usage_pic_label = QtGui.QLabel()
        self.usage_pic_label.setPixmap(self.usagePicPixMap)

        self.machines_label_1 = QtGui.QLabel("Machines: ")
        self.machines_line_edit = QtGui.QLineEdit()
        self.machines_line_edit.setText(str(
            self.current_zone.use_conditions.machines))
        self.machines_label_2 = QtGui.QLabel("W/m^2")

        self.lighting_label_1 = QtGui.QLabel("Lighting: ")
        self.lighting_line_edit = QtGui.QLineEdit()
        self.lighting_line_edit.setText(str(
            self.current_zone.use_conditions.maintained_illuminace))
        self.lighting_label_2 = QtGui.QLabel("W/m^2")

        self.mean_temp_out_label_1 = QtGui.QLabel("Mean Outdoor Temp: ")
        self.mean_temp_outer_line_edit = QtGui.QLineEdit()
        self.mean_temp_outer_line_edit.setText(
            str(self.current_zone.t_outside))
        self.mean_temp_out_label_2 = QtGui.QLabel("K")

        self.mean_temp_in_label_1 = QtGui.QLabel("Mean Indoor Temp: ")
        self.mean_temp_inner_line_edit = QtGui.QLineEdit()
        self.mean_temp_inner_line_edit.setText(str(self.current_zone.t_inside))
        self.mean_temp_in_label_2 = QtGui.QLabel("K")

        self.infiltration_rate_label_1 = QtGui.QLabel("Infiltration Rate: ")
        self.infiltration_rate_line_edit = QtGui.QLineEdit()
        if self.current_zone.infiltration_rate is not None:
            self.infiltration_rate_line_edit.setText(str(
                self.current_zone.infiltration_rate))
        else:
            self.infiltration_rate_line_edit.setText("1")
        self.infiltration_rate_label_2 = QtGui.QLabel("1/h")

        # Cheat to group the other controls on top
        self.space_label = QtGui.QLabel()

        self.zone_usage_times_layout.addWidget(
            self.cooling_ahu_start_label, 1, 1)
        self.zone_usage_times_layout.addWidget(
            self.cooling_ahu_start_dropdown, 1, 2)
        self.zone_usage_times_layout.addWidget(
            self.cooling_ahu_end_label, 1, 3)
        self.zone_usage_times_layout.addWidget(
            self.cooling_ahu_end_dropdown, 1, 4)
        self.zone_usage_times_layout.addWidget(
            self.heating_ahu_start_label, 2, 1)
        self.zone_usage_times_layout.addWidget(
            self.heating_ahu_start_dropdown, 2, 2)
        self.zone_usage_times_layout.addWidget(
            self.heating_ahu_end_label, 2, 3)
        self.zone_usage_times_layout.addWidget(
            self.heating_ahu_end_dropdown, 2, 4)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_heat_label_1, 3, 1)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_heat_line_edit, 3, 2)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_heat_label_2, 3, 3)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_cool_label_1, 4, 1)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_cool_line_edit, 4, 2)
        self.zone_usage_times_layout.addWidget(
            self.set_temp_cool_label_2, 4, 3)
        self.zone_usage_times_layout.addWidget(
            self.temp_set_back_label_1, 5, 1)
        self.zone_usage_times_layout.addWidget(
            self.temp_set_back_line_edit, 5, 2)
        self.zone_usage_times_layout.addWidget(
            self.temp_set_back_label_2, 5, 3)
        self.zone_usage_times_layout.addWidget(self.min_air_flow_label_1, 6, 1)
        self.zone_usage_times_layout.addWidget(
            self.min_air_flow_line_edit, 6, 2)
        self.zone_usage_times_layout.addWidget(self.min_air_flow_label_2, 6, 3)
        self.zone_usage_times_layout.addWidget(self.min_ahu_label_1, 7, 1)
        self.zone_usage_times_layout.addWidget(self.min_ahu_line_edit, 7, 2)
        self.zone_usage_times_layout.addWidget(self.min_ahu_label_2, 7, 3)
        self.zone_usage_times_layout.addWidget(self.max_ahu_label_1, 8, 1)
        self.zone_usage_times_layout.addWidget(self.max_ahu_line_edit, 8, 2)
        self.zone_usage_times_layout.addWidget(self.max_ahu_label_2, 8, 3)
        self.zone_usage_times_layout.addWidget(self.with_ahu_label_1, 9, 1)
        self.zone_usage_times_layout.addWidget(self.with_ahu_combobox, 9, 2)
        self.zone_usage_times_layout.addWidget(self.re_humidity_label_1, 10, 1)
        self.zone_usage_times_layout.addWidget(
            self.re_humidity_line_edit, 10, 2)
        self.zone_usage_times_layout.addWidget(self.re_humidity_label_2, 10, 3)

        self.zone_usage_layout.addWidget(self.persons_label_1, 1, 1)
        self.zone_usage_layout.addWidget(self.persons_line_edit, 1, 2)
        self.zone_usage_layout.addWidget(self.persons_label_2, 1, 3)
        self.zone_usage_layout.addWidget(self.canvas_profiles, 2, 1, 2, 3)
        self.zone_usage_layout.addWidget(self.graph_label, 4, 1)
        self.zone_usage_layout.addWidget(self.machines_label_1, 5, 1)
        self.zone_usage_layout.addWidget(self.machines_line_edit, 5, 2)
        self.zone_usage_layout.addWidget(self.machines_label_2, 5, 3)
        self.zone_usage_layout.addWidget(self.lighting_label_1, 6, 1)
        self.zone_usage_layout.addWidget(self.lighting_line_edit, 6, 2)
        self.zone_usage_layout.addWidget(self.lighting_label_2, 6, 3)

        self.static_heat_layout.addWidget(self.mean_temp_out_label_1, 1, 1)
        self.static_heat_layout.addWidget(
            self.mean_temp_outer_line_edit, 1, 2)
        self.static_heat_layout.addWidget(self.mean_temp_out_label_2, 1, 3)
        self.static_heat_layout.addWidget(self.mean_temp_in_label_1, 2, 1)
        self.static_heat_layout.addWidget(
            self.mean_temp_inner_line_edit, 2, 2)
        self.static_heat_layout.addWidget(self.mean_temp_in_label_2, 2, 3)
        self.static_heat_layout.addWidget(self.infiltration_rate_label_1, 3, 1)
        self.static_heat_layout.addWidget(
            self.infiltration_rate_line_edit, 3, 2)
        self.static_heat_layout.addWidget(self.infiltration_rate_label_2, 3, 3)
        self.static_heat_layout.addWidget(self.space_label, 4, 0, 9, 3)

        self.save_cancel_layout.addWidget(self.zone_element_save_button, 1, 0)
        self.save_cancel_layout.addWidget(
            self.zone_element_cancel_button, 1, 1)

        self.groupbox_general_zone_values_layout.setMaximumHeight(120)
        self.zone_value_window_layout.addWidget(
            self.groupbox_general_zone_values_layout, 2, 0, 1, 0)
        self.zone_value_window_layout.addWidget(
            self.zone_values_tab, 7, 0, 1, 0)
        self.zone_value_window_layout.addWidget(
            self.groupbox_save_cancel_buttons, 8, 0, 1, 0)
        self.zone_value_window.setWindowModality(Qt.ApplicationModal)
        self.zone_value_window.show()

    def change_envelopes_values_ui(self, item):
        '''Displays attributes of a selected envelope

        opens a window to see all attributes from the currently selected
        envelope.
        '''

        self.envelopes_value_window = QtGui.QWizardPage()
        self.envelopes_value_window.setWindowIcon(self.teaser_icon)
        self.envelopes_value_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.envelopes_value_window.setWindowTitle("Envelopes Details")
        self.envelopes_value_window.setFixedWidth(300)
        self.envelopes_value_window.setFixedHeight(200)
        self.envelopes_value_window_layout = QtGui.QGridLayout()
        self.envelopes_value_window.setLayout(
            self.envelopes_value_window_layout)

        self.general_envelope_values_groupbox =\
            QtGui.QGroupBox(u"General Envelope Values")
        self.general_envelope_values_groupbox.setGeometry(
            QtCore.QRect(0, 0, 120, 120))
        self.general_envelope_values_layout = QtGui.QGridLayout()
        self.general_envelope_values_groupbox.setLayout(
            self.general_envelope_values_layout)

        self.envelope_type_label = QtGui.QLabel("Type")
        self.envelope_type_textbox = QtGui.QLineEdit()
        self.envelope_type_textbox.setObjectName(_fromUtf8(
            u"EnvelopeNameTextBox"))
        self.envelope_type_textbox.setReadOnly(True)

        self.envelope_area_label = QtGui.QLabel("Area")
        self.envelope_area_textbox = QtGui.QLineEdit()
        self.envelope_area_textbox.setObjectName(_fromUtf8(
            u"EnvelopeAreaTextBox"))

        self.envelope_orientation_label = QtGui.QLabel("Orientation")
        self.envelope_orientation_combobox = QtGui.QComboBox()
        self.envelope_orientation_combobox.setObjectName(_fromUtf8(
            "EnvelopeOrientationGroupBox"))
        for orientation in self.guiinfo.orientations:
            self.envelope_orientation_combobox.addItem(
                orientation, userData=None)

        current_item = self.outer_elements_model.itemFromIndex(item)
        string_current_item = str(current_item.text())
        listOfCurItem = string_current_item.split()
        self.current_envelope = string_current_item
        if string_current_item.startswith("Outer Wall"):
            self.envelope_type_textbox.setText(str("Outer Wall"))
            self.envelope_area_textbox.setText(str(listOfCurItem[5]))
            self.envelope_orientation_combobox.setCurrentIndex(
                self.envelope_orientation_combobox.findText(
                    str(listOfCurItem[3])))

        elif string_current_item.startswith("Rooftop"):
            self.envelope_type_textbox.setText(str("Rooftop"))
            self.envelope_area_textbox.setText(str(listOfCurItem[4]))
            self.envelope_orientation_combobox.setCurrentIndex(
                self.envelope_orientation_combobox.findText(
                    str(listOfCurItem[2])))

        elif string_current_item.startswith("Ground Floor"):
            self.envelope_type_textbox.setText(str("Ground Floor"))
            self.envelope_area_textbox.setText(str(listOfCurItem[5]))
            self.envelope_orientation_combobox.setCurrentIndex(
                self.envelope_orientation_combobox.findText(
                    str(listOfCurItem[3])))

        elif string_current_item.startswith("Window"):
            self.envelope_type_textbox.setText(str("Window"))
            self.envelope_area_textbox.setText(str(listOfCurItem[4]))
            self.envelope_orientation_combobox.setCurrentIndex(
                self.envelope_orientation_combobox.findText(
                    str(listOfCurItem[2])))

        self.envelope_orientation_before_changing = \
            str(self.envelope_orientation_combobox.currentText())
        self.groupbox_save_cancel_buttons = QtGui.QGroupBox()
        self.save_cancel_layout = QtGui.QGridLayout()
        self.groupbox_save_cancel_buttons.setLayout(self.save_cancel_layout)

        self.envelope_element_save_button = QtGui.QPushButton()
        self.envelope_element_save_button.setText("Save")

        self.envelope_element_cancel_button = QtGui.QPushButton()
        self.envelope_element_cancel_button.setText("Cancel")

        self.envelope_element_set_all_construction_button = QtGui.QPushButton()
        self.envelope_element_set_all_construction_button.setText(
            "Set all construction")
        self.connect(self.envelope_element_save_button, SIGNAL("clicked()"),
                     self.save_changed_envelopes_values)
        self.connect(self.envelope_element_save_button, SIGNAL("clicked()"),
                     self.envelopes_value_window, QtCore.SLOT("close()"))
        self.connect(self.envelope_element_cancel_button, SIGNAL("clicked()"),
                     self.envelopes_value_window, QtCore.SLOT("close()"))
        self.connect(self.envelope_element_set_all_construction_button,
                     SIGNAL("clicked()"), self.create_new_envelope_ui)
        self.save_cancel_layout.addWidget(
            self.envelope_element_save_button, 0, 0)
        self.save_cancel_layout.addWidget(
            self.envelope_element_cancel_button, 0, 1)
        self.save_cancel_layout.addWidget(
            self.envelope_element_set_all_construction_button, 1, 0, 1, 0)

        self.general_envelope_values_layout.addWidget(
            self.envelope_type_label, 1, 0)
        self.general_envelope_values_layout.addWidget(
            self.envelope_type_textbox, 1, 1)
        self.general_envelope_values_layout.addWidget(
            self.envelope_orientation_label, 2, 0)
        self.general_envelope_values_layout.addWidget(
            self.envelope_orientation_combobox, 2, 1)
        self.general_envelope_values_layout.addWidget(
            self.envelope_area_label, 3, 0)
        self.general_envelope_values_layout.addWidget(
            self.envelope_area_textbox, 3, 1)

        self.general_envelope_values_groupbox.setMaximumHeight(120)
        self.general_envelope_values_groupbox.setMinimumHeight(120)
        self.envelope_element_list_view = QtGui.QListView()
        self.envelope_element_list_view.setObjectName(
            _fromUtf8("envelope_element_list_view"))
        self.envelope_element_list_view.setModel(self.outer_elements_model)
        self.envelope_element_list_view.setItemDelegate(self.lVZF)
        self.envelopes_value_window_layout.addWidget(
            self.general_envelope_values_groupbox, 0, 0)
        self.envelopes_value_window_layout.addWidget(
            self.groupbox_save_cancel_buttons, 1, 0)
        self.envelopes_value_window.setWindowModality(Qt.ApplicationModal)
        self.envelopes_value_window.show()

    def update_zone_details(self):
        '''Update the zone details window

        updates the zone details window after something has been changed.
        '''

        self.element_model.clear()
        if self.current_zone.inner_walls:
            for inner_wall in self.current_zone.inner_walls:
                if type(inner_wall).__name__ == "InnerWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Inner Wall \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == "Floor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Floor \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == "Ceiling":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Ceiling \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
        if self.current_zone.outer_walls:
            for outer_wall in self.current_zone.outer_walls:
                if type(outer_wall).__name__ == "OuterWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(outer_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Outer Wall \n Area:\t".expandtabs(11) +
                        str(outer_wall.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(outer_wall.orientation),
                        outer_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(outer_wall).__name__ == \
                        "GroundFloor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(outer_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Ground Floor \n Area:\t".expandtabs(11) +
                        str(outer_wall.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(outer_wall.orientation),
                        outer_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(outer_wall).__name__ == "Rooftop":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(outer_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Rooftop \n Area:\t".expandtabs(11) +
                        str(outer_wall.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(outer_wall.orientation),
                        outer_wall.internal_id)
                    self.element_model.appendRow(item)
        if self.current_zone.windows:
            for window in self.current_zone.windows:
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(window.name) +
                    "\nType:\t".expandtabs(11) +
                    "Windows \n Area:\t".expandtabs(11) +
                    str(window.area) +
                    "\n Orientation:\t".expandtabs(11) +
                    str(window.orientation), window.internal_id)
                self.element_model.appendRow(item)

        for time in self.guiinfo.hoursInADay:
            if len(str(self.current_zone.use_conditions.cooling_time[0])) == 1:
                fixed_c_t_s = "0" + str(
                    self.current_zone.use_conditions.cooling_time[0]) + ":00"
            else:
                fixed_c_t_s = str(
                    self.current_zone.use_conditions.cooling_time[0]) + ":00"
            if len(str(self.current_zone.use_conditions.cooling_time[1])) == 1:
                fixed_c_t_e = "0" + str(
                    self.current_zone.use_conditions.cooling_time[1]) + ":00"
            else:
                fixed_c_t_e = str(
                    self.current_zone.use_conditions.cooling_time[1]) + ":00"
            if len(str(self.current_zone.use_conditions.heating_time[0])) == 1:
                fixed_h_t_s = "0" + str(
                    self.current_zone.use_conditions.heating_time[0]) + ":00"
            else:
                fixed_h_t_s = str(
                    self.current_zone.use_conditions.heating_time[0]) + ":00"
            if len(str(self.current_zone.use_conditions.heating_time[1])) == 1:
                fixed_h_t_e = "0" + str(
                    self.current_zone.use_conditions.heating_time[1]) + ":00"
            else:
                fixed_h_t_e = str(
                    self.current_zone.use_conditions.heating_time[1]) + ":00"
            if (time == fixed_c_t_s):
                self.cooling_ahu_start_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_c_t_e):
                self.cooling_ahu_end_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_h_t_s):
                self.heating_ahu_start_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
            if (time == fixed_h_t_e):
                self.heating_ahu_end_dropdown.setCurrentIndex(
                    self.guiinfo.hoursInADay.index(time))
        self.set_temp_heat_line_edit.setText(str(
            self.current_zone.use_conditions.set_temp_heat))
        self.set_temp_cool_line_edit.setText(str(
            self.current_zone.use_conditions.set_temp_cool))
        self.temp_set_back_line_edit.setText(str(
            self.current_zone.use_conditions.temp_set_back))
        self.min_air_flow_line_edit.setText(str(
            self.current_zone.use_conditions.min_air_exchange))
        self.min_ahu_line_edit.setText(str(
            self.current_zone.use_conditions.min_ahu))
        self.max_ahu_line_edit.setText(str(
            self.current_zone.use_conditions.max_ahu))
        if (self.current_zone.use_conditions.with_ahu == "True"):
            self.with_ahu_combobox.setCurrentIndex(
                self.with_ahu_combobox.findText("True"))
        else:
            self.with_ahu_combobox.setCurrentIndex(
                self.with_ahu_combobox.findText("False"))
        self.re_humidity_line_edit.setText(str(
            self.current_zone.use_conditions.rel_humidity))
        self.persons_line_edit.setText(str(
            self.current_zone.use_conditions.persons))
        self.machines_line_edit.setText(str(
            self.current_zone.use_conditions.machines))
        self.lighting_line_edit.setText(str(
            self.current_zone.use_conditions.maintained_illuminace))
        self.mean_temp_outer_line_edit.setText(str(
            self.current_zone.t_outside))
        self.mean_temp_inner_line_edit.setText(str(
            self.current_zone.t_inside))
        self.infiltration_rate_line_edit.setText(str(
            self.current_zone.infiltration_rate))
        self.canvas_profiles.repaint()
        data_persons = [1.0 for x in range(24)]
        data_machines = [1.0 for x in range(24)]
        # TODO: data_lighting = [1.0 for x in range(24)]
        for hour in range(0, 24):
            try:
                data_persons[hour] =\
                    self.current_zone.use_conditions.profile_persons[hour]
                data_machines[hour] =\
                    self.current_zone.use_conditions.profile_machines[hour]
            except IndexError:
                break
            # TODO: data_lighting[hour] =\
            #        self.current_zone.use_conditions.profile_lighting[hour]
        ax_p = self.figure_profiles.add_subplot(111)
        ax_p.hold(False)
        ax_p.plot(range(24), data_persons, 'b-',
                  range(24), data_machines, 'r-')
        # TODO: ax_p.plot(range(24), data_persons, 'b-', range(24),
        # data_machines, 'r-', data_lighting, 'g-')
        ax_p.set_ylim([0, 1])
        self.canvas_profiles.draw()

    def update_wall_details(self):
        '''Update the wall details window

        updates the wall details window after wall have been changed.
        '''

        self.element_model_update_xml.clear()
        for inner_wall in self.thermalZoneFromXML.inner_walls:
            if type(inner_wall).__name__ == "InnerWall":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + inner_wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(inner_wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(inner_wall.building_age_group), inner_wall.internal_id)
                self.element_model_update_xml.appendRow(item)
            if type(inner_wall).__name__ == "Floor":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + inner_wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(inner_wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(inner_wall.building_age_group), inner_wall.internal_id)
                self.element_model_update_xml.appendRow(item)
            if type(inner_wall).__name__ == "Ceiling":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + inner_wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(inner_wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(inner_wall.building_age_group), inner_wall.internal_id)
                self.element_model_update_xml.appendRow(item)
        for wall in self.thermalZoneFromXML.outer_walls:
            if type(wall).__name__ == "GroundFloor":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(wall.building_age_group), wall.internal_id)
                self.element_model_update_xml.appendRow(item)
            if type(wall).__name__ == "Rooftop":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(wall.building_age_group), wall.internal_id)
                self.element_model_update_xml.appendRow(item)
            if type(wall).__name__ == "OuterWall":
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + wall.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(wall.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(wall.building_age_group), wall.internal_id)
                self.element_model_update_xml.appendRow(item)
        for window in self.thermalZoneFromXML.windows:
                item = TrackableItem(
                    "Type:\t".expandtabs(8) + window.name +
                    "\nconstruction_type:\t".expandtabs(11) +
                    str(window.construction_type) +
                    "\nbuilding_age_group:\t".expandtabs(11) +
                    str(window.building_age_group), window.internal_id)
                self.element_model_update_xml.appendRow(item)

    def update_element_details(self):
        '''Update the element details window

        updates the element details window after layers have been changed.
        '''

        self.element_layer_model.clear()
        for layer in self.current_element.layer:
            item = TrackableItem(
                "Material:\t".expandtabs(8) + str(layer.material.name) +
                "\nThickness:\t".expandtabs(14) + str(layer.thickness) +
                "\t", layer.internal_id)
            self.element_layer_model.appendRow(item)

    def update_set_all_construction(self):
        '''Update the set all construction window

        updates the set all construction window after layers have been changed.
        '''

        self.element_layer_model_set_all_constr.clear()
        for layer in self.all_constr_layer_list:
            item = TrackableItem(
                "Material:\t".expandtabs(8) + str(layer.material.name) +
                "\nThickness:\t".expandtabs(14) + str(layer.thickness) +
                "\t", layer.internal_id)
            self.element_layer_model_set_all_constr.appendRow(item)

    def update_xml_window(self):
        '''Update the xml window

        updates the set all construction window after layers have been changed.
        '''
        self.element_layer_model_update_xml.clear()
        for layer in self.xml_layer_list:
            item = TrackableItem(
                "Material:\t".expandtabs(8) + str(layer.material.name) +
                "\nThickness:\t".expandtabs(14) + str(layer.thickness) +
                "\t", layer.internal_id)
            self.element_layer_model_update_xml.appendRow(item)

    def update_xml_window_modify(self):
        '''Update the listView in the layer details window 

        updates the window after layers have been changed.
        '''
        self.wall_layer_model.clear()
        for layer in self.current_wall.layer:
            item = TrackableItem(
                "Material:\t".expandtabs(8) + str(layer.material.name) +
                "\nThickness:\t".expandtabs(14) + str(layer.thickness) +
                "\t", layer.id)
            self.wall_layer_model.appendRow(item)

    def show_warning_window_ui(self):
        
        self.warning_window = QtGui.QWizardPage()
        self.warning_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.warning_window.setWindowTitle("Warning")
        self.warning_window.setFixedWidth(300)
        self.warning_window.setFixedHeight(100)
        self.warning_window_layout = QtGui.QGridLayout()
        self.warning_window.setLayout(self.warning_window_layout)

        self.warning_label = QtGui.QLabel(self.warning_window)
        self.warning_label.setGeometry(QtCore.QRect(10, 0, 280, 50))
        self.warning_label.setText("This has no effect on your building" +
                                   " parameters, its just \n" +
                                   "general information.")
        self.warning_window_save_button = QtGui.QPushButton(
            self.warning_window)
        self.warning_window_save_button.setText("Ok")
        self.warning_window_save_button.setGeometry(
            QtCore.QRect(0, 60, 145, 25))
        self.connect(self.warning_window_save_button, SIGNAL("clicked()"),
                     self.warning_window, QtCore.SLOT("close()"))
        self.connect(self.warning_window_save_button, SIGNAL("clicked()"),
                     self.click_update_building)
        self.connect(self.warning_window_save_button, SIGNAL("clicked()"),
                     self.display_current_building)
        self.warning_window_cancel_button = QtGui.QPushButton(
            self.warning_window)
        self.warning_window_cancel_button.setText("Cancel")
        self.warning_window_cancel_button.setGeometry(
            QtCore.QRect(155, 60, 145, 25))
        self.connect(self.warning_window_cancel_button, SIGNAL("clicked()"),
                     self.warning_window, QtCore.SLOT("close()"))
        self.connect(self.warning_window_cancel_button, SIGNAL("clicked()"),
                     self.display_current_building)

        if isinstance(self.current_building, NonResidential) or \
           isinstance(self.current_building, Residential):
            self.warning_window_save_button.setGeometry(
                    QtCore.QRect(0, 60, 100, 25))
            self.warning_window_cancel_button.setGeometry(
                    QtCore.QRect(100, 60, 100, 25))
            self.warning_window_update_button = QtGui.QPushButton(
                self.warning_window)
            self.warning_window_update_button.setText("Update Archetype")
            self.warning_window_update_button.setGeometry(
                QtCore.QRect(200, 60, 100, 25))
            self.connect(self.warning_window_update_button,
                         SIGNAL("clicked()"),
                         self.warning_window, QtCore.SLOT("close()"))            
            self.connect(self.warning_window_update_button,
                         SIGNAL("clicked()"),
                         self.click_update_building)
                                            
        self.warning_window.setWindowModality(Qt.ApplicationModal)
        self.warning_window.show()
        
    def show_element_build_ui(self, item):
        '''Displays attributes of a selected element

        opens a window to display all attributes of the currently selected
        element.
        '''

        self.element_build_ui = QtGui.QWizardPage()
        self.element_build_ui.setWindowIcon(self.teaser_icon)
        self.element_build_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.element_build_ui.setWindowTitle("Element Details")
        self.element_build_ui.setFixedWidth(450)
        self.element_build_ui.setFixedHeight(600)
        self.element_build_ui_window_layout = QtGui.QGridLayout()
        self.element_build_ui.setLayout(self.element_build_ui_window_layout)

        self.element_layer_model.clear()

        current_item = self.element_model.itemFromIndex(item)
        if "Inner Wall" in current_item.text():
            for element in self.current_zone.inner_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Floor" in current_item.text():
            for element in self.current_zone.inner_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Ceiling" in current_item.text():
            for element in self.current_zone.inner_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Outer Wall" in current_item.text():
            for element in self.current_zone.outer_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Ground Floor" in current_item.text():
            for element in self.current_zone.outer_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Rooftop" in current_item.text():
            for element in self.current_zone.outer_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Window" in current_item.text():
            for element in self.current_zone.windows:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element

        for layer in self.current_element.layer:
            item = TrackableItem("Material:\t".expandtabs(8) +
                                 str(layer.material.name) +
                                 "\nThickness:\t".expandtabs(14) +
                                 str(layer.thickness) +
                                 "\t", layer.internal_id)
            self.element_layer_model.appendRow(item)

        self.element_general_layout = QtGui.QGridLayout()
        self.element_general_layout_groupBox = QtGui.QGroupBox(
            "General Element Values")
        self.element_general_layout_groupBox.setLayout(
            self.element_general_layout)

        self.element_save_cancel_layout = QtGui.QGridLayout()
        self.element_save_cancel_layoutGroupBox = QtGui.QGroupBox()
        self.element_save_cancel_layoutGroupBox.setLayout(
            self.element_save_cancel_layout)
        self.element_save_cancel_layoutGroupBox.setMaximumHeight(48)

        self.element_type_label = QtGui.QLabel("Type")
        self.element_type_textbox = QtGui.QTextEdit()
        self.element_type_textbox.setText(
            type(self.current_element).__name__)
        self.element_type_textbox.setReadOnly(True)
        self.element_type_textbox.setMaximumHeight(24)

        self.element_construction_type_label = QtGui.QLabel(
            "Construction Type")
        self.element_construction_type_combobox = QtGui.QComboBox()
        self.element_construction_type_combobox.setObjectName(
            _fromUtf8("ElementConstructionTypeComboBox"))
        self.element_construction_type_combobox.addItem("heavy", userData=None)
        self.element_construction_type_combobox.addItem("light", userData=None)
        if self.current_element.construction_type == "heavy":
            self.element_construction_type_combobox.setCurrentIndex(0)
        if self.current_element.construction_type == "light":
            self.element_construction_type_combobox.setCurrentIndex(1)
        self.connect(self.element_construction_type_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_constr_type)

        self.element_orientation_label = QtGui.QLabel("Orientation")
        self.element_orientation_combobox = QtGui.QComboBox()
        self.element_orientation_combobox.setObjectName(
            _fromUtf8("ElementOrientationComboBox"))
        for orientation in self.guiinfo.orientations:
            self.element_orientation_combobox.addItem(
                orientation, userData=None)
        if(self.current_element.orientation is not None):
            orientation_string = str(self.guiinfo.orientations_numbers
                                     [self.current_element.orientation])
            self.element_orientation_combobox.setCurrentIndex(
                self.element_orientation_combobox.findText(
                    orientation_string))
        else:
            self.element_orientation_combobox.setCurrentIndex(-1)

        self.element_name_label = QtGui.QLabel("Name")
        self.element_name_textbox = QtGui.QLineEdit()
        self.element_name_textbox.setObjectName(
            _fromUtf8("ElementNameTextBox"))
        self.element_name_textbox.setText(str(self.current_element.name))

        self.element_area_label = QtGui.QLabel("Area")
        self.element_area_textbox = QtGui.QLineEdit()
        self.element_area_textbox.setObjectName(
            _fromUtf8("ElementAreaTextBox"))
        self.element_area_textbox.setText(str(round(
            self.current_element.area, 2)))

        self.element_year_of_construction_label = QtGui.QLabel(
            "Year Of Construction")
        self.element_year_of_construction_textbox = QtGui.QLineEdit()
        self.element_year_of_construction_textbox.setObjectName(
            _fromUtf8("ElementYearOfConstructionTextBox"))
        if self.current_element.year_of_construction is None:
            self.element_year_of_construction_textbox.setText(
                str(0))
        else:
            self.element_year_of_construction_textbox.setText(
                str(self.current_element.year_of_construction))

        self.element_year_of_retrofit_label = QtGui.QLabel(
            "Year Of Retrofit")
        self.element_year_of_retrofit_textbox = QtGui.QLineEdit()
        self.element_year_of_retrofit_textbox.setObjectName(
            _fromUtf8("ElementYearOfRetrofitTextBox"))
        if self.current_element._year_of_retrofit is None:
            self.element_year_of_retrofit_textbox.setText(
                str(0))
        else:
            self.element_year_of_retrofit_textbox.setText(
                str(self.current_element._year_of_retrofit))

        self.element_tilt_label = QtGui.QLabel("Tilt")
        self.element_tilt_textbox = QtGui.QLineEdit()
        self.element_tilt_textbox.setObjectName(
            _fromUtf8("ElementTiltTextBox"))
        if self.current_element.tilt is None:
            self.element_tilt_textbox.setText(
                str(0))
        else:
            self.element_tilt_textbox.setText(
                str(self.current_element.tilt))

        self.element_inner_convection_label = QtGui.QLabel("Inner Convection")
        self.element_inner_convection_textbox = QtGui.QLineEdit()
        self.element_inner_convection_textbox.setObjectName(
            _fromUtf8("ElementInnerConvectionTextBox"))
        if self.current_element.inner_convection is None:
            self.element_inner_convection_textbox.setText(
                str(0))
        else:
            self.element_inner_convection_textbox.setText(
                str(self.current_element.inner_convection))

        self.element_inner_radiation_label = QtGui.QLabel("Inner Radiation")
        self.element_inner_radiation_textbox = QtGui.QLineEdit()
        self.element_inner_radiation_textbox.setObjectName(
            _fromUtf8("ElementInnerRadiationTextBox"))
        if self.current_element.inner_radiation is None:
            self.element_inner_radiation_textbox.setText(
                str(0))
        else:
            self.element_inner_radiation_textbox.setText(
                str(self.current_element.inner_radiation))

        if not type(self.current_element).__name__ == "InnerWall":

            self.element_outer_convection_label = QtGui.QLabel(
                "Outer Convection")
            self.element_outer_convection_textbox = QtGui.QLineEdit()
            self.element_outer_convection_textbox.setObjectName(
                _fromUtf8("ElementOuterConvectionTextBox"))
            self.element_outer_convection_textbox.setText(
                str(self.current_element.outer_convection))

            self.element_outer_radiation_label = QtGui.QLabel(
                "Outer Radiation")
            self.element_outer_radiation_textbox = QtGui.QLineEdit()
            self.element_outer_radiation_textbox.setObjectName(
                _fromUtf8("ElementOuterRadiationTextBox"))
            self.element_outer_radiation_textbox.setText(
                str(self.current_element.outer_radiation))

        self.element_uvalue_label = QtGui.QLabel("U-Value (W/m2K)")
        self.element_uvalue_textbox = QtGui.QLineEdit()
        self.element_uvalue_textbox.setObjectName(
            _fromUtf8("ElementUValueTextBox"))
        self.element_uvalue_textbox.setText(str(float(
            Controller.get_u_value(self.current_element))))
        self.element_uvalue_textbox.setReadOnly(True)

        self.element_add_material_button = QtGui.QPushButton()
        self.element_add_material_button.setText("Add Layer")
        self.connect(self.element_add_material_button, SIGNAL("clicked()"),
                     lambda check_window="Element Details Window":
                     self.create_new_layer_ui(check_window))

        self.element_delete_material_button = QtGui.QPushButton()
        self.element_delete_material_button.setText("Delete Layer")
        self.connect(self.element_delete_material_button, SIGNAL("clicked()"),
                     self.delete_selected_layer)

        self.set_all_constr_element_material_list_view = QtGui.QListView()
        self.element_material_list_view = QtGui.QListView()
        self.element_material_list_view.setGeometry(
            QtCore.QRect(10, 200, 170, 300))
        self.element_material_list_view.setObjectName(
            _fromUtf8("ElementMaterialsListView"))
        self.element_material_list_view.setModel(self.element_layer_model)
        self.element_material_list_view.setItemDelegate(self.lVZF)
        self.element_material_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.element_material_list_view.doubleClicked.connect(
            self.show_layer_build_ui)
        self.element_material_list_label = QtGui.QLabel()
        self.element_material_list_label.setGeometry(
            QtCore.QRect(175, 200, 25, 300))
        self.element_material_list_label.setText("From inner\n\n\n\n\n\n\n\n"
                                                 "To Outer")

        self.element_save_button = QtGui.QPushButton()
        self.element_save_button.setText("Save")

        self.connect(self.element_save_button, SIGNAL("clicked()"),
                     self.load_constr_type)
        self.connect(self.element_save_button, SIGNAL("clicked()"),
                     self.save_changed_element_values)
        self.connect(self.element_save_button, SIGNAL("clicked()"),
                     self.update_zone_details)
        self.connect(self.element_save_button, SIGNAL("clicked()"),
                     self.element_build_ui, QtCore.SLOT("close()"))
        # self.connect(self.element_save_button, SIGNAL("clicked()"),
        #              self.zone_value_window, QtCore.SLOT("update()"))

        self.element_cancel_button = QtGui.QPushButton()
        self.element_cancel_button.setText("Cancel")
        self.connect(self.element_cancel_button, SIGNAL("clicked()"),
                     self.element_build_ui, QtCore.SLOT("close()"))

        if type(self.current_element).__name__ == "InnerWall":

            self.element_general_layout.addWidget(
                self.element_type_label, 1, 0)
            self.element_general_layout.addWidget(
                self.element_type_textbox, 1, 1)
            self.element_general_layout.addWidget(
                self.element_construction_type_label, 2, 0)
            self.element_general_layout.addWidget(
                self.element_construction_type_combobox, 2, 1)
            self.element_general_layout.addWidget(
                self.element_orientation_label, 3, 0)
            self.element_general_layout.addWidget(
                self.element_orientation_combobox, 3, 1)
            self.element_general_layout.addWidget(
                self.element_name_label, 4, 0)
            self.element_general_layout.addWidget(
                self.element_name_textbox, 4, 1)
            self.element_general_layout.addWidget(
                self.element_area_label, 5, 0)
            self.element_general_layout.addWidget(
                self.element_area_textbox, 5, 1)
            self.element_general_layout.addWidget(
                self.element_year_of_construction_label, 6, 0)
            self.element_general_layout.addWidget(
                self.element_year_of_construction_textbox, 6, 1)
            self.element_general_layout.addWidget(
                self.element_year_of_retrofit_label, 7, 0)
            self.element_general_layout.addWidget(
                self.element_year_of_retrofit_textbox, 7, 1)
            self.element_general_layout.addWidget(
                self.element_tilt_label, 8, 0)
            self.element_general_layout.addWidget(
                self.element_tilt_textbox, 8, 1)
            self.element_general_layout.addWidget(
                self.element_inner_convection_label, 9, 0)
            self.element_general_layout.addWidget(
                self.element_inner_convection_textbox, 9, 1)
            self.element_general_layout.addWidget(
                self.element_inner_radiation_label, 10, 0)
            self.element_general_layout.addWidget(
                self.element_inner_radiation_textbox, 10, 1)
            self.element_general_layout.addWidget(
                self.element_uvalue_label, 11, 0)
            self.element_general_layout.addWidget(
                self.element_uvalue_textbox, 11, 1)
            self.element_general_layout.addWidget(
                self.element_add_material_button, 12, 0)
            self.element_general_layout.addWidget(
                self.element_delete_material_button, 12, 1)
            self.element_general_layout.addWidget(
                self.element_material_list_view, 13, 0, 14, 3)
            self.element_general_layout.addWidget(
                self.element_material_list_label, 13, 3, 14, 4)
            self.element_save_cancel_layout.addWidget(
                self.element_save_button, 0, 0)
            self.element_save_cancel_layout.addWidget(
                self.element_cancel_button, 0, 1)

        else:

            self.element_general_layout.addWidget(
                self.element_type_label, 1, 0)
            self.element_general_layout.addWidget(
                self.element_type_textbox, 1, 1)
            self.element_general_layout.addWidget(
                self.element_construction_type_label, 2, 0)
            self.element_general_layout.addWidget(
                self.element_construction_type_combobox, 2, 1)
            self.element_general_layout.addWidget(
                self.element_orientation_label, 3, 0)
            self.element_general_layout.addWidget(
                self.element_orientation_combobox, 3, 1)
            self.element_general_layout.addWidget(
                self.element_name_label, 4, 0)
            self.element_general_layout.addWidget(
                self.element_name_textbox, 4, 1)
            self.element_general_layout.addWidget(
                self.element_area_label, 5, 0)
            self.element_general_layout.addWidget(
                self.element_area_textbox, 5, 1)
            self.element_general_layout.addWidget(
                self.element_year_of_construction_label, 6, 0)
            self.element_general_layout.addWidget(
                self.element_year_of_construction_textbox, 6, 1)
            self.element_general_layout.addWidget(
                self.element_year_of_retrofit_label, 7, 0)
            self.element_general_layout.addWidget(
                self.element_year_of_retrofit_textbox, 7, 1)
            self.element_general_layout.addWidget(
                self.element_tilt_label, 8, 0)
            self.element_general_layout.addWidget(
                self.element_tilt_textbox, 8, 1)
            self.element_general_layout.addWidget(
                self.element_inner_convection_label, 9, 0)
            self.element_general_layout.addWidget(
                self.element_inner_convection_textbox, 9, 1)

            self.element_general_layout.addWidget(
                self.element_inner_radiation_label, 10, 0)
            self.element_general_layout.addWidget(
                self.element_inner_radiation_textbox, 10, 1)
            self.element_general_layout.addWidget(
                self.element_outer_convection_label, 11, 0)
            self.element_general_layout.addWidget(
                self.element_outer_convection_textbox, 11, 1)
            self.element_general_layout.addWidget(
                self.element_outer_radiation_label, 12, 0)
            self.element_general_layout.addWidget(
                self.element_outer_radiation_textbox, 12, 1)
            self.element_general_layout.addWidget(
                self.element_uvalue_label, 13, 0)
            self.element_general_layout.addWidget(
                self.element_uvalue_textbox, 13, 1)
            self.element_general_layout.addWidget(
                self.element_add_material_button, 14, 0)
            self.element_general_layout.addWidget(
                self.element_delete_material_button, 14, 1)
            self.element_general_layout.addWidget(
                self.element_material_list_view, 15, 0, 15, 3)
            self.element_general_layout.addWidget(
                self.element_material_list_label, 15, 3, 15, 4)
            self.element_save_cancel_layout.addWidget(
                self.element_save_button, 0, 0)
            self.element_save_cancel_layout.addWidget(
                self.element_cancel_button, 0, 1)

        self.element_build_ui_window_layout.addWidget(
            self.element_general_layout_groupBox)
        self.element_build_ui_window_layout.addWidget(
            self.element_save_cancel_layoutGroupBox)
        self.element_build_ui.setWindowModality(Qt.ApplicationModal)
        self.element_build_ui.show()

    def show_wall_build_ui(self, item):
        '''Displays attributes of a selected wall

        opens a window to display all attributes of the currently selected
        wall.
        '''

        self.wall_build_ui = QtGui.QWizardPage()
        self.wall_build_ui.setWindowIcon(self.teaser_icon)
        self.wall_build_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.wall_build_ui.setWindowTitle("Wall Details")
        self.wall_build_ui.setFixedWidth(450)
        self.wall_build_ui.setFixedHeight(600)
        self.wall_build_ui_window_layout = QtGui.QGridLayout()
        self.wall_build_ui.setLayout(self.wall_build_ui_window_layout)

        self.wall_general_layout = QtGui.QGridLayout()
        self.wall_general_layout_groupBox = QtGui.QGroupBox(
            "General Wall Values")
        self.wall_general_layout_groupBox.setLayout(
            self.wall_general_layout)

        self.wall_save_cancel_layout = QtGui.QGridLayout()
        self.wall_save_cancel_layoutGroupBox = QtGui.QGroupBox()
        self.wall_save_cancel_layoutGroupBox.setLayout(
            self.wall_save_cancel_layout)
        self.wall_save_cancel_layoutGroupBox.setMaximumHeight(48)

        current_item_from_index = self.element_model_update_xml.itemFromIndex(
                                       item)
        if "InnerWall" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.inner_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "Floor" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.inner_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "Ceiling" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.inner_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "OuterWall" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.outer_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "GroundFloor" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.outer_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "Rooftop" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.outer_walls:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break
        if "Window" in current_item_from_index.text():
            for element in self.thermalZoneFromXML.windows:
                if element.internal_id == \
                   current_item_from_index.internal_id:
                    self.current_wall = element
                    self.selected_wall = element
                    break

        self.wall_type_label = QtGui.QLabel("Type")
        self.wall_type_line_edit = QtGui.QLineEdit()
        if "OuterWall" in current_item_from_index.text():
            self.wall_type_line_edit.setText("OuterWall")
        elif "Rooftop" in current_item_from_index.text():
            self.wall_type_line_edit.setText("Rooftop")
        elif "Window" in current_item_from_index.text():
            self.wall_type_line_edit.setText("Window")
        elif "Rooftop" in current_item_from_index.text():
            self.wall_type_line_edit.setText("Rooftop")
        elif "GroundFloor" in current_item_from_index.text():
            self.wall_type_line_edit.setText("GroundFloor")
        elif "InnerWall" in current_item_from_index.text():
            self.wall_type_line_edit.setText("InnerWall")
        elif "Ceiling" in current_item_from_index.text():
            self.wall_type_line_edit.setText("Ceiling")
        elif "Floor" in current_item_from_index.text():
            self.wall_type_line_edit.setText("Floor")
        self.wall_type_line_edit.setReadOnly(True)
        self.wall_type_line_edit.setMaximumHeight(24)

        self.wall_construction_type_label = QtGui.QLabel(
            "Construction Type")
        self.wall_construction_type_combobox = QtGui.QComboBox()
        self.wall_construction_type_combobox.setObjectName(
            _fromUtf8("WallConstructionTypeComboBox"))
        self.wall_construction_type_combobox.addItem("heavy", userData=None)
        self.wall_construction_type_combobox.addItem("light", userData=None)

        self.wall_Building_age_group_label = QtGui.QLabel(
             "Building_age_group")
        self.wall_Building_age_group_textbox_from = QtGui.QLineEdit()
        self.wall_Building_age_group_textbox_from.setObjectName(
            _fromUtf8("building_age_group_text_box_from"))
        self.wall_Building_age_group_textbox_from.setText(
            str(self.current_wall.building_age_group[0]))
        self.wall_Building_age_group_textbox_from.setMaximumWidth(100)
        self.wall_Building_age_group_label_to = QtGui.QLabel(
             "to:")
        self.wall_Building_age_group_textbox_to = QtGui.QLineEdit()
        self.wall_Building_age_group_textbox_to.setObjectName(
            _fromUtf8("building_age_group_text_box"))
        self.wall_Building_age_group_textbox_to.setText(
            str(self.current_wall.building_age_group[1]))
        self.wall_Building_age_group_textbox_to.setMaximumWidth(100)

        self.wall_inner_convection_label = QtGui.QLabel("Inner Convection")
        self.wall_inner_convection_textbox = QtGui.QLineEdit()
        self.wall_inner_convection_textbox.setObjectName(
            _fromUtf8("WallInnerConvectionTextBox"))
        self.wall_inner_convection_textbox.setText(str(
            self.current_wall.inner_convection))

        self.wall_inner_radiation_label = QtGui.QLabel("Inner Radiation")
        self.wall_inner_radiation_textbox = QtGui.QLineEdit()
        self.wall_inner_radiation_textbox.setObjectName(
            _fromUtf8("WallInnerRadiationTextBox"))
        self.wall_inner_radiation_textbox.setText(str(
            self.current_wall.inner_radiation))

        self.wall_outer_convection_label = QtGui.QLabel(
                "Outer Convection")
        self.wall_outer_convection_textbox = QtGui.QLineEdit()
        self.wall_outer_convection_textbox.setObjectName(
            _fromUtf8("WallOuterConvectionTextBox"))

        self.wall_outer_radiation_label = QtGui.QLabel(
            "Outer Radiation")
        self.wall_outer_radiation_textbox = QtGui.QLineEdit()
        self.wall_outer_radiation_textbox.setObjectName(
            _fromUtf8("WallOuterRadiationTextBox"))

        if self.wall_type_line_edit.text() != \
                "InnerWall" and "Floor" and "Ceiling":
            self.wall_outer_convection_textbox.setText(str(
                self.current_wall.outer_convection))
            self.wall_outer_radiation_textbox.setText(str(
                self.current_wall.outer_radiation))

        self.wall_add_material_button = QtGui.QPushButton()
        self.wall_add_material_button.setText("Add Layer")
        self.connect(self.wall_add_material_button, SIGNAL("clicked()"),
                     lambda check_window="xml_modify_layer_window":
                     self.create_new_layer_ui(check_window))

        self.wall_delete_material_button = QtGui.QPushButton()
        self.wall_delete_material_button.setText("Delete Layer")
        self.connect(self.wall_delete_material_button, SIGNAL("clicked()"),
                     self.delete_selected_layer_xml__modify_window)

        self.wall_layer_model.clear()
        for layer in self.current_wall.layer:
            item = TrackableItem("Material:\t".expandtabs(8) +
                                 str(layer.material.name) +
                                 "\nThickness:\t".expandtabs(14) +
                                 str(layer.thickness) +
                                 "\t", layer.id)
            self.wall_layer_model.appendRow(item)

        self.wall_material_list_view = QtGui.QListView()
        self.wall_material_list_view.setGeometry(
            QtCore.QRect(10, 200, 170, 300))
        self.wall_material_list_view.setObjectName(
            _fromUtf8("WallMaterialsListView"))
        self.wall_material_list_view.setModel(self.wall_layer_model)
        self.wall_material_list_view.setItemDelegate(self.lVZF)
        self.wall_material_list_view.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.lVZF.height = 45
        self.wall_material_list_view.doubleClicked.connect(
            self.show_layer_build_ui_xml)

        self.wall_material_list_label = QtGui.QLabel()
        self.wall_material_list_label.setGeometry(
            QtCore.QRect(175, 200, 25, 300))
        self.wall_material_list_label.setText("From inner\n\n\n\n\n\n\n\n"
                                              "To Outer")
        self.wall_save_button = QtGui.QPushButton()
        self.wall_save_button.setText("Save")
        self.connect(self.wall_save_button, SIGNAL("clicked()"),
                     self.modify_element_in_xml)
        self.connect(self.wall_save_button, SIGNAL("clicked()"),
                     self.wall_build_ui, QtCore.SLOT("close()"))

        self.wall_cancel_button = QtGui.QPushButton()
        self.wall_cancel_button.setText("Cancel")
        self.connect(self.wall_cancel_button, SIGNAL("clicked()"),
                     self.wall_build_ui, QtCore.SLOT("close()"))

        self.wall_general_layout.addWidget(
            self.wall_type_label, 1, 0)
        self.wall_general_layout.addWidget(
            self.wall_type_line_edit, 1, 1)
        self.wall_general_layout.addWidget(
            self.wall_construction_type_label, 2, 0)
        self.wall_general_layout.addWidget(
            self.wall_construction_type_combobox, 2, 1)
        self.wall_general_layout.addWidget(
            self.wall_Building_age_group_label, 3, 0)
        self.wall_general_layout.addWidget(
            self.wall_Building_age_group_textbox_from, 3, 1, Qt.AlignLeft)
        self.wall_general_layout.addWidget(
            self.wall_Building_age_group_label_to, 3, 1, Qt.AlignCenter)
        self.wall_general_layout.addWidget(
            self.wall_Building_age_group_textbox_to, 3, 1, Qt.AlignRight)
        self.wall_general_layout.addWidget(
            self.wall_inner_convection_label, 4, 0)
        self.wall_general_layout.addWidget(
            self.wall_inner_convection_textbox, 4, 1)
        self.wall_general_layout.addWidget(
            self.wall_inner_radiation_label, 5, 0)
        self.wall_general_layout.addWidget(
            self.wall_inner_radiation_textbox, 5, 1)
        if self.wall_type_line_edit.text() != \
                "InnerWall" and "Floor" and "Ceiling":
            self.wall_general_layout.addWidget(
                self.wall_outer_convection_label, 6, 0)
            self.wall_general_layout.addWidget(
                self.wall_outer_convection_textbox, 6, 1)
            self.wall_general_layout.addWidget(
                self.wall_outer_radiation_label, 7, 0)
            self.wall_general_layout.addWidget(
                self.wall_outer_radiation_textbox, 7, 1)
        self.wall_general_layout.addWidget(
            self.wall_add_material_button, 8, 0)
        self.wall_general_layout.addWidget(
            self.wall_delete_material_button, 8, 1)
        self.wall_general_layout.addWidget(
            self.wall_material_list_view, 9, 0, 9, 3)
        self.wall_general_layout.addWidget(
            self.wall_material_list_label, 9, 3, 9, 4)
        self.wall_save_cancel_layout.addWidget(
            self.wall_save_button, 0, 0)
        self.wall_save_cancel_layout.addWidget(
            self.wall_cancel_button, 0, 1)

        self.wall_build_ui_window_layout.addWidget(
            self.wall_general_layout_groupBox)
        self.wall_build_ui_window_layout.addWidget(
            self.wall_save_cancel_layoutGroupBox)
        self.wall_build_ui.setWindowModality(Qt.ApplicationModal)
        self.wall_build_ui.show()

    def show_export_window(self):
        '''Displays options of export

        opens a window that displays the options to export the project.
        '''

        self.export_window_ui = QtGui.QWizardPage()
        self.export_window_ui.setWindowIcon(self.teaser_icon)
        self.export_window_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.export_window_ui.setWindowTitle("Export")
        self.export_window_ui.setFixedWidth(380)
        self.export_window_ui.setFixedHeight(320)
        self.export_window_ui_layout = QtGui.QGridLayout()
        self.export_window_ui.setLayout(self.export_window_ui_layout)

        self.export_groupbox = QtGui.QGroupBox("Export")
        self.export_groupbox.setGeometry(QtCore.QRect(5, 5, 360, 155))
        self.export_groupbox.setMinimumSize(QtCore.QSize(360, 155))
        self.export_groupbox.setMaximumSize(QtCore.QSize(360, 155))
        self.export_groupbox.setObjectName(_fromUtf8("exportGroupBox"))

        self.aixlib_groupbox = QtGui.QGroupBox("AixLib")
        self.aixlib_groupbox.setGeometry(QtCore.QRect(5, 5, 360, 120))
        self.aixlib_groupbox.setMinimumSize(QtCore.QSize(360, 120))
        self.aixlib_groupbox.setMaximumSize(QtCore.QSize(360, 120))
        self.aixlib_groupbox.setObjectName(_fromUtf8("AixLibGroupBox"))

        self.annex_groupbox = QtGui.QGroupBox("Annex60")
        self.annex_groupbox.setGeometry(QtCore.QRect(5, 5, 360, 120))
        self.annex_groupbox.setMinimumSize(QtCore.QSize(360, 120))
        self.annex_groupbox.setMaximumSize(QtCore.QSize(360, 120))
        self.annex_groupbox.setObjectName(_fromUtf8("AnnexGroupBox"))
        self.annex_groupbox.setVisible(False)

        self.export_model_groupbox = QtGui.QGroupBox("")
        self.export_model_groupbox.setGeometry(QtCore.QRect(5, 5, 360, 120))
        self.export_model_groupbox.setMinimumSize(QtCore.QSize(360, 120))
        self.export_model_groupbox.setMaximumSize(QtCore.QSize(360, 120))
        self.export_model_groupbox.setObjectName(_fromUtf8("GroupBoxModel"))

        self.export_button = QtGui.QPushButton(self.export_groupbox)
        self.export_button.setGeometry(QtCore.QRect(5, 20, 305, 25))
        self.export_button.clicked.connect(self.click_export_button)
        self.export_button.setText("Export model for all buildings")
        self.export_button_one = QtGui.QPushButton(self.export_groupbox)
        self.export_button_one.setGeometry(QtCore.QRect(5, 55, 305, 25))
        self.export_button_one.clicked.connect(self.click_export_button)
        self.export_button_one.setText("Export model for current building")
        self.export_save_template_label = QtGui.QLabel(self.export_groupbox)
        self.export_save_template_label.setGeometry(
            QtCore.QRect(5, 90, 110, 25))
        self.export_save_template_label.setText("File path:")
        self.export_save_template_lineedit = QtGui.QLineEdit(
            self.export_groupbox)
        self.export_save_template_lineedit .setGeometry(
            QtCore.QRect(130, 90, 130, 25))
        if self.file_path == "":
            self.export_save_template_lineedit.setText(
                utilitis.get_default_path())
            utilitis.create_path(str(
                                self.export_save_template_lineedit.text()))
            self.file_path = self.export_save_template_lineedit.text()
        else:
            self.export_save_template_lineedit.setText(self.file_path)
            utilitis.create_path(str(
                                self.export_save_template_lineedit.text()))
        self.export_save_template_button = QtGui.QPushButton(
            self.export_groupbox)
        self.export_save_template_button.setGeometry(
            QtCore.QRect(265, 90, 80, 25))
        self.export_save_template_button.setText("Browse")
        self.export_save_template_button.clicked.connect(
            self.click_browse_button)
        self.export_label_library = QtGui.QLabel(self.export_groupbox)
        self.export_label_library.setGeometry(
            QtCore.QRect(5, 125, 120, 25))
        self.export_label_library.setText("Library:")
        self.export_create_library_combobox = QtGui.QComboBox(
            self.export_groupbox)
        self.export_create_library_combobox.setGeometry(
            QtCore.QRect(130, 125, 215, 25))

        self.export_template_label_model = QtGui.QLabel(self.aixlib_groupbox)
        self.export_template_label_model.setGeometry(
            QtCore.QRect(5, 20, 120, 25))
        self.export_template_label_model.setText("Model type:")
        self.export_create_template_model_combobox = QtGui.QComboBox(
            self.aixlib_groupbox)
        self.export_create_template_model_combobox.setGeometry(
            QtCore.QRect(130, 20, 215, 25))
        self.export_template_label_zone = QtGui.QLabel(self.aixlib_groupbox)
        self.export_template_label_zone.setGeometry(
            QtCore.QRect(5, 55, 120, 25))
        self.export_template_label_zone.setText("Zone type:")
        self.export_create_template_zone_combobox = QtGui.QComboBox(
            self.aixlib_groupbox)
        self.export_create_template_zone_combobox.setGeometry(
            QtCore.QRect(130, 55, 215, 25))
        self.export_template_label_corG = QtGui.QLabel(self.aixlib_groupbox)
        self.export_template_label_corG.setGeometry(
            QtCore.QRect(5, 90, 120, 25))
        self.export_template_label_corG.setText("corG:")
        self.radio_button_corG_1 = QtGui.QRadioButton(self.aixlib_groupbox)
        self.radio_button_corG_1.setGeometry(QtCore.QRect(130, 90, 120, 25))
        self.radio_button_corG_1.setText("with CorG")
        self.radio_button_corG_2 = QtGui.QRadioButton(self.aixlib_groupbox)
        self.radio_button_corG_2.setGeometry(QtCore.QRect(250, 90, 120, 25))
        self.radio_button_corG_2.setText("without CorG")
        self.radio_button_corG_1.setChecked(True)

        self.annex_number_of_elements = QtGui.QLabel(self.annex_groupbox)
        self.annex_number_of_elements.setGeometry(
            QtCore.QRect(5, 20, 120, 25))
        self.annex_number_of_elements.setText("Number of elements:")
        self.annex_create_number_of_elements_combobox = QtGui.QComboBox(
            self.annex_groupbox)
        self.annex_create_number_of_elements_combobox.setGeometry(
            QtCore.QRect(130, 20, 215, 25))
        self.annex_merge_windows = QtGui.QLabel(self.annex_groupbox)
        self.annex_merge_windows.setGeometry(
            QtCore.QRect(5, 55, 120, 25))
        self.annex_merge_windows.setText("Merge windows:")
        self.annex_create_merge_windows_combobox = QtGui.QComboBox(
            self.annex_groupbox)
        self.annex_create_merge_windows_combobox.setGeometry(
            QtCore.QRect(130, 55, 215, 25))

        library_type_list = ["AixLib", "Annex60"]
        modelTypeList = ["MultizoneEquipped", "Multizone", "None"]
        zoneTypeList = ["ThermalZoneEquipped", "ThermalZone", "None"]
        number_of_elements_list = ["2", "3", "4"]
        merging_windows_list = ["True", "False"]

        self.export_create_library_combobox.addItems(library_type_list)
        self.export_create_template_model_combobox.addItems(modelTypeList)
        self.export_create_template_zone_combobox.addItems(zoneTypeList)
        self.annex_create_number_of_elements_combobox.addItems(
                                                    number_of_elements_list)
        self.annex_create_merge_windows_combobox.addItems(
                                                    merging_windows_list)

        self.connect(self.export_create_library_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_lib)

        self.export_window_ui_layout.addWidget(
            self.export_groupbox, 1, 1)
        self.export_window_ui_layout.addWidget(
            self.aixlib_groupbox, 2, 1)
        self.export_window_ui_layout.addWidget(
            self.annex_groupbox, 2, 1)

        self.export_window_ui.setWindowModality(Qt.ApplicationModal)
        self.export_window_ui.show()

    def show_simulation_window(self):
        '''Displays attributes of simulation

        opens a window to display the project name and all simulation
        attributes.
        '''

        self.simulation_window_ui = QtGui.QWizardPage()
        self.simulation_window_ui.setWindowIcon(self.teaser_icon)
        self.simulation_window_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.simulation_window_ui.setWindowTitle("Simulation")
        self.simulation_window_ui.setFixedWidth(330)
        self.simulation_window_ui.setFixedHeight(280)
        self.simulation_window_ui_layout = QtGui.QGridLayout()
        self.simulation_window_ui.setLayout(self.simulation_window_ui_layout)

        self.project_name_groupbox = QtGui.QGroupBox("Project")
        self.project_name_groupbox.setGeometry(QtCore.QRect(10, 10, 315, 40))
        self.project_name_groupbox.setMinimumSize(QtCore.QSize(315, 40))
        self.project_name_groupbox.setMaximumSize(QtCore.QSize(315, 40))
        self.project_name_label = QtGui.QLabel(self.project_name_groupbox)
        self.project_name_label.setGeometry(QtCore.QRect(5, 10, 90, 25))
        self.project_name_label.setText("Project Name:")
        self.project_name_lineedit = QtGui.QLineEdit(
            self.project_name_groupbox)
        self.project_name_lineedit.setGeometry(QtCore.QRect(100, 10, 180, 25))
        self.project_name_lineedit.setText(str(self.project.name))

        self.simulation_groupbox = QtGui.QGroupBox("Simulation")
        self.simulation_groupbox.setGeometry(QtCore.QRect(380, 85, 315, 160))
        self.simulation_groupbox.setMinimumSize(QtCore.QSize(315, 160))
        self.simulation_groupbox.setMaximumSize(QtCore.QSize(315, 160))
        self.simulation_groupbox.setObjectName(_fromUtf8("simulationGroupBox"))
        self.simulation_runtime_label_1 = QtGui.QLabel(
            self.simulation_groupbox)
        self.simulation_runtime_label_1.setGeometry(
            QtCore.QRect(5, 20, 90, 25))
        self.simulation_runtime_label_1.setText("Runtime Simulation:")
        self.simulation_runtime_lineedit = QtGui.QLineEdit(
            self.simulation_groupbox)
        self.simulation_runtime_lineedit.setGeometry(
            QtCore.QRect(100, 20, 180, 25))
        self.simulation_runtime_lineedit.setText(
            self.project.modelica_info.runtime_simulation)
        self.simulation_runtime_label_2 = QtGui.QLabel(
            self.simulation_groupbox)
        self.simulation_runtime_label_2.setGeometry(
            QtCore.QRect(285, 20, 10, 25))
        self.simulation_runtime_label_2.setText("s")
        self.simulation_interval_output_label_1 = QtGui.QLabel(
            self.simulation_groupbox)
        self.simulation_interval_output_label_1.setGeometry(
            QtCore.QRect(5, 55, 90, 25))
        self.simulation_interval_output_label_1.setText("Interval Output:")
        self.simulation_interval_output_lineedit = QtGui.QLineEdit(
            self.simulation_groupbox)
        self.simulation_interval_output_lineedit.setGeometry(
            QtCore.QRect(100, 55, 180, 25))
        self.simulation_interval_output_lineedit.setText(
            self.project.modelica_info.interval_output)
        self.simulation_interval_output_label_2 = QtGui.QLabel(
            self.simulation_groupbox)
        self.simulation_interval_output_label_2.setGeometry(
            QtCore.QRect(285, 55, 10, 25))
        self.simulation_interval_output_label_2.setText("s")
        self.simulation_solver_label = QtGui.QLabel(self.simulation_groupbox)
        self.simulation_solver_label.setGeometry(QtCore.QRect(5, 90, 90, 25))
        self.simulation_solver_label.setText("Solver:")
        self.simulation_solver_combobox = QtGui.QComboBox(
            self.simulation_groupbox)
        self.simulation_solver_combobox.setGeometry(
            QtCore.QRect(100, 90, 180, 25))
        for solver in self.project.modelica_info.solver:
            self.simulation_solver_combobox.addItem(solver)
        self.simulation_solver_combobox.setCurrentIndex(
            self.simulation_solver_combobox.findText(
                self.project.modelica_info.current_solver))
        self.simulation_equidistant_output_checkbox = QtGui.QCheckBox(
            self.simulation_groupbox)
        self.simulation_equidistant_output_checkbox.setGeometry(
            QtCore.QRect(5, 125, 290, 20))
        self.simulation_equidistant_output_checkbox.setChecked(
            self.project.modelica_info.equidistant_output)
        self.simulation_equidistant_output_checkbox.setText(
            "Equidistant Output")

        self.simulation_save_cancel_groupbox = QtGui.QGroupBox()
        self.simulation_save_cancel_groupbox.setGeometry(
            QtCore.QRect(10, 530, 315, 35))
        self.simulation_save_cancel_groupbox.setMinimumSize(
            QtCore.QSize(315, 35))
        self.simulation_save_cancel_groupbox.setMaximumSize(
            QtCore.QSize(315, 35))
        self.simulation_save_button = QtGui.QPushButton(
            self.simulation_save_cancel_groupbox)
        self.simulation_save_button.setText("Save")
        self.simulation_save_button.setGeometry(QtCore.QRect(5, 5, 90, 25))
        self.connect(self.simulation_save_button, SIGNAL("clicked()"),
                     self.save_changed_simulation_values)
        self.connect(self.simulation_save_button, SIGNAL("clicked()"),
                     self.simulation_window_ui, QtCore.SLOT("close()"))
        self.simulation_cancel_button = QtGui.QPushButton(
            self.simulation_save_cancel_groupbox)
        self.simulation_cancel_button.setText("Cancel")
        self.simulation_cancel_button.setGeometry(QtCore.QRect(100, 5, 80, 25))
        self.connect(self.simulation_cancel_button, SIGNAL("clicked()"),
                     self.simulation_window_ui, QtCore.SLOT("close()"))

        self.simulation_window_ui_layout.addWidget(
            self.project_name_groupbox, 1, 1)
        self.simulation_window_ui_layout.addWidget(
            self.simulation_groupbox, 2, 1)
        self.simulation_window_ui_layout.addWidget(
            self.simulation_save_cancel_groupbox, 3, 1)
        self.simulation_window_ui.setWindowModality(Qt.ApplicationModal)
        self.simulation_window_ui.show()

    def show_layer_build_ui(self, item):
        '''Displays attributes of a selected layer

        opens a window to see all attributes from the currently selected layer.
        '''

        self.layer_build_ui = QtGui.QWizardPage()
        self.layer_build_ui.setWindowIcon(self.teaser_icon)
        self.layer_build_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.layer_build_ui.setWindowTitle("Layer Details")
        self.layer_build_ui.setFixedWidth(450)
        self.layer_build_ui.setFixedHeight(300)
        self.layer_build_ui_window_layout = QtGui.QGridLayout()
        self.layer_build_ui.setLayout(self.layer_build_ui_window_layout)
        self.layer_model = QtGui.QStandardItemModel()
        self.materials = Controller.get_materials_from_file(self.project)
        self.is_switchable = False

        sender = self.sender().objectName()
        try:
            if sender == self.element_material_list_view.objectName():
                current_item = self.element_layer_model.itemFromIndex(item)
                current_layer = self.current_element.layer
        except:
            try:
                if sender == \
                  self.set_all_constr_element_material_list_view.objectName():
                    current_item = \
                     self.element_layer_model_set_all_constr.itemFromIndex(
                                                             item)
                    current_layer = self.all_constr_layer_list
            except:
                if sender == \
                  self.generate_new_xml_ui_material_list_view.objectName():
                    current_item = \
                        self.element_layer_model_update_xml.itemFromIndex(item)
                    current_layer = self.xml_layer_list

        for layer in current_layer:
            if layer.internal_id == current_item.internal_id:
                self.current_layer = layer
                break
        self.layer_general_layout = QtGui.QGridLayout()
        self.layer_general_layout_group_box = QtGui.QGroupBox("Layer Values")
        self.layer_general_layout_group_box.setLayout(
            self.layer_general_layout)

        self.thickness_label = QtGui.QLabel("Layer Thickness")
        self.thickness_textbox = QtGui.QLineEdit()
        self.thickness_textbox.setObjectName(_fromUtf8("ThicknessTextBox"))
        self.thickness_textbox.setText(str(self.current_layer.thickness))

        self.material_label = QtGui.QLabel("Material")
        self.material_combobox = QtGui.QComboBox()
        self.connect(self.material_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_material)
        temp_list = []
        for material in self.materials:
            if material.name not in temp_list:
                temp_list.append(material.name)
        if self.current_layer.material.name not in temp_list and\
                self.current_layer.material.name is not None:
            temp_list.append(self.current_layer.material.name)
        self.material_combobox.addItems(sorted(temp_list))
        self.material_combobox.setCurrentIndex(
            self.material_combobox.findText(self.current_layer.material.name))
        self.is_switchable = True

        self.material_density_label = QtGui.QLabel("Density")
        self.material_density_textbox = QtGui.QLineEdit()
        self.material_density_textbox.setObjectName(
            _fromUtf8("MaterialDensityTextBox"))
        self.material_density_textbox.setText(
            str(self.current_layer.material.density))

        self.material_thermal_conduc_label = QtGui.QLabel("ThermalConduc")
        self.material_thermal_conduc_textbox = QtGui.QLineEdit()
        self.material_thermal_conduc_textbox.setObjectName(
            _fromUtf8("MaterialThermalConducTextBox"))
        self.material_thermal_conduc_textbox.setText(
            str(self.current_layer.material.thermal_conduc))

        self.material_heat_capac_label = QtGui.QLabel("HeatCapac")
        self.material_heat_capac_textbox = QtGui.QLineEdit()
        self.material_heat_capac_textbox.setObjectName(
            _fromUtf8("MaterialHeatCapacTextBox"))
        self.material_heat_capac_textbox.setText(
            str(self.current_layer.material.heat_capac))

        self.material_solar_absorp_label = QtGui.QLabel("SolarAbsorp")
        self.material_solar_absorp_textbox = QtGui.QLineEdit()
        self.material_solar_absorp_textbox.setObjectName(
            _fromUtf8("MaterialSolarAbsorpTextBox"))
        self.material_solar_absorp_textbox.setText(
            str(self.current_layer.material.solar_absorp))

        self.material_ir_emissivity_label = QtGui.QLabel("IrEmissivity")
        self.material_ir_emissivity_textbox = QtGui.QLineEdit()
        self.material_ir_emissivity_textbox.setObjectName(
            _fromUtf8("MaterialIrEmissivityTextBox"))
        self.material_ir_emissivity_textbox.setText(
            str(self.current_layer.material.ir_emissivity))

        self.material_transmittance_label = QtGui.QLabel("Transmittance")
        self.material_transmittance_textbox = QtGui.QLineEdit()
        self.material_transmittance_textbox.setObjectName(
            _fromUtf8("MaterialTransmittanceTextBox"))
        self.material_transmittance_textbox.setText(
            str(self.current_layer.material.transmittance))

        self.layer_save_button = QtGui.QPushButton()
        self.layer_save_button.setText("Save")

        try:
            if sender == self.element_material_list_view.objectName():
                self.connect(self.layer_save_button, SIGNAL(
                    "clicked()"), self.save_changed_layer_values)
                self.connect(self.layer_save_button, SIGNAL(
                    "clicked()"), self.update_element_details)
        except:
            try:
                if sender == \
                  self.set_all_constr_element_material_list_view.objectName():
                    self.connect(self.layer_save_button, SIGNAL(
                        "clicked()"),
                        self.save_changed_layer_values_set_all_constr)
                    self.connect(self.layer_save_button, SIGNAL(
                        "clicked()"), self.update_set_all_construction)
            except:
                if sender == \
                  self.generate_new_xml_ui_material_list_view.objectName():
                    self.connect(self.layer_save_button, SIGNAL(
                        "clicked()"), self.save_changed_layer_values_xml)
                    self.connect(self.layer_save_button, SIGNAL(
                        "clicked()"), self.update_xml_window)
        self.connect(self.layer_save_button, SIGNAL(
            "clicked()"), self.layer_build_ui, QtCore.SLOT("close()"))

        self.layer_cancel_button = QtGui.QPushButton()
        self.layer_cancel_button.setText("Cancel")
        self.connect(self.layer_cancel_button, SIGNAL(
            "clicked()"), self.layer_build_ui, QtCore.SLOT("close()"))

        self.layer_general_layout.addWidget(self.thickness_label, 1, 0)
        self.layer_general_layout.addWidget(self.thickness_textbox, 1, 1)
        self.layer_general_layout.addWidget(self.material_label, 2, 0)
        self.layer_general_layout.addWidget(self.material_combobox, 2, 1)
        self.layer_general_layout.addWidget(self.material_density_label, 3, 0)
        self.layer_general_layout.addWidget(
            self.material_density_textbox, 3, 1)
        self.layer_general_layout.addWidget(
            self.material_thermal_conduc_label, 4, 0)
        self.layer_general_layout.addWidget(
            self.material_thermal_conduc_textbox, 4, 1)
        self.layer_general_layout.addWidget(
            self.material_heat_capac_label, 5, 0)
        self.layer_general_layout.addWidget(
            self.material_heat_capac_textbox, 5, 1)
        self.layer_general_layout.addWidget(
            self.material_solar_absorp_label, 6, 0)
        self.layer_general_layout.addWidget(
            self.material_solar_absorp_textbox, 6, 1)
        self.layer_general_layout.addWidget(
            self.material_ir_emissivity_label, 7, 0)
        self.layer_general_layout.addWidget(
            self.material_ir_emissivity_textbox, 7, 1)
        self.layer_general_layout.addWidget(
            self.material_transmittance_label, 8, 0)
        self.layer_general_layout.addWidget(
            self.material_transmittance_textbox, 8, 1)
        self.layer_general_layout.addWidget(self.layer_save_button, 9, 0)
        self.layer_general_layout.addWidget(self.layer_cancel_button, 9, 1)

        self.layer_build_ui_window_layout.addWidget(
            self.layer_general_layout_group_box)
        self.layer_build_ui.setWindowModality(Qt.ApplicationModal)
        self.layer_build_ui.show()

    def show_layer_build_ui_xml(self, item):
        '''Displays attributes of a selected layer

        opens a window to see all attributes from the currently selected layer.
        '''

        self.layer_build_ui = QtGui.QWizardPage()
        self.layer_build_ui.setWindowIcon(self.teaser_icon)
        self.layer_build_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.layer_build_ui.setWindowTitle("Layer Details")
        self.layer_build_ui.setFixedWidth(450)
        self.layer_build_ui.setFixedHeight(300)
        self.layer_build_ui_window_layout = QtGui.QGridLayout()
        self.layer_build_ui.setLayout(self.layer_build_ui_window_layout)
        self.layer_model = QtGui.QStandardItemModel()
        self.materials = Controller.get_materials_from_file(self.project)
        self.is_switchable = False

        sender = self.sender().objectName()
        try:
            if sender == self.wall_material_list_view.objectName():
                current_item = self.wall_layer_model.itemFromIndex(item)
                current_layer = self.current_wall.layer
                for layer in current_layer:
                    if layer.id == current_item.internal_id:
                        self.current_layer = layer
                        break
        except:
            pass

        self.layer_general_layout = QtGui.QGridLayout()
        self.layer_general_layout_group_box = QtGui.QGroupBox("Layer Values")
        self.layer_general_layout_group_box.setLayout(
            self.layer_general_layout)

        self.thickness_label = QtGui.QLabel("Layer Thickness")
        self.thickness_textbox = QtGui.QLineEdit()
        self.thickness_textbox.setObjectName(_fromUtf8("ThicknessTextBox"))
        self.thickness_textbox.setText(str(self.current_layer.thickness))

        self.material_label = QtGui.QLabel("Material")
        self.material_combobox = QtGui.QComboBox()
        self.connect(self.material_combobox, QtCore.SIGNAL(
            "currentIndexChanged(int)"), self.switch_material)
        temp_list = []
        for material in self.materials:
            if material.name not in temp_list:
                temp_list.append(material.name)
        if self.current_layer.material.name not in temp_list and\
                self.current_layer.material.name is not None:
            temp_list.append(self.current_layer.material.name)
        self.material_combobox.addItems(sorted(temp_list))
        self.material_combobox.setCurrentIndex(
            self.material_combobox.findText(self.current_layer.material.name))
        self.is_switchable = True

        self.material_density_label = QtGui.QLabel("Density")
        self.material_density_textbox = QtGui.QLineEdit()
        self.material_density_textbox.setObjectName(
            _fromUtf8("MaterialDensityTextBox"))
        self.material_density_textbox.setText(
            str(self.current_layer.material.density))

        self.material_thermal_conduc_label = QtGui.QLabel("ThermalConduc")
        self.material_thermal_conduc_textbox = QtGui.QLineEdit()
        self.material_thermal_conduc_textbox.setObjectName(
            _fromUtf8("MaterialThermalConducTextBox"))
        self.material_thermal_conduc_textbox.setText(
            str(self.current_layer.material.thermal_conduc))

        self.material_heat_capac_label = QtGui.QLabel("HeatCapac")
        self.material_heat_capac_textbox = QtGui.QLineEdit()
        self.material_heat_capac_textbox.setObjectName(
            _fromUtf8("MaterialHeatCapacTextBox"))
        self.material_heat_capac_textbox.setText(
            str(self.current_layer.material.heat_capac))

        self.material_solar_absorp_label = QtGui.QLabel("SolarAbsorp")
        self.material_solar_absorp_textbox = QtGui.QLineEdit()
        self.material_solar_absorp_textbox.setObjectName(
            _fromUtf8("MaterialSolarAbsorpTextBox"))
        self.material_solar_absorp_textbox.setText(
            str(self.current_layer.material.solar_absorp))

        self.material_ir_emissivity_label = QtGui.QLabel("IrEmissivity")
        self.material_ir_emissivity_textbox = QtGui.QLineEdit()
        self.material_ir_emissivity_textbox.setObjectName(
            _fromUtf8("MaterialIrEmissivityTextBox"))
        self.material_ir_emissivity_textbox.setText(
            str(self.current_layer.material.ir_emissivity))

        '''
        self.material_transmittance_label = QtGui.QLabel("Transmittance")
        self.material_transmittance_textbox = QtGui.QLineEdit()
        self.material_transmittance_textbox.setObjectName(
            _fromUtf8("MaterialTransmittanceTextBox"))
        '''
        self.layer_save_button = QtGui.QPushButton()
        self.layer_save_button.setText("Save")
        self.connect(self.layer_save_button, SIGNAL("clicked()"),
                     self.save_changed_layer_values_xml_modify)
        self.connect(self.layer_save_button, SIGNAL("clicked()"),
                     self.update_xml_window_modify)
        self.connect(self.layer_save_button, SIGNAL(
            "clicked()"), self.layer_build_ui, QtCore.SLOT("close()"))

        self.connect(self.layer_save_button, SIGNAL(
            "clicked()"), self.layer_build_ui, QtCore.SLOT("close()"))

        self.layer_cancel_button = QtGui.QPushButton()
        self.layer_cancel_button.setText("Cancel")
        self.connect(self.layer_cancel_button, SIGNAL(
            "clicked()"), self.layer_build_ui, QtCore.SLOT("close()"))

        self.layer_general_layout.addWidget(self.thickness_label, 1, 0)
        self.layer_general_layout.addWidget(self.thickness_textbox, 1, 1)
        self.layer_general_layout.addWidget(self.material_label, 2, 0)
        self.layer_general_layout.addWidget(self.material_combobox, 2, 1)
        self.layer_general_layout.addWidget(self.material_density_label, 3, 0)
        self.layer_general_layout.addWidget(
            self.material_density_textbox, 3, 1)
        self.layer_general_layout.addWidget(
            self.material_thermal_conduc_label, 4, 0)
        self.layer_general_layout.addWidget(
            self.material_thermal_conduc_textbox, 4, 1)
        self.layer_general_layout.addWidget(
            self.material_heat_capac_label, 5, 0)
        self.layer_general_layout.addWidget(
            self.material_heat_capac_textbox, 5, 1)
        self.layer_general_layout.addWidget(
            self.material_solar_absorp_label, 6, 0)
        self.layer_general_layout.addWidget(
            self.material_solar_absorp_textbox, 6, 1)
        self.layer_general_layout.addWidget(
            self.material_ir_emissivity_label, 7, 0)
        self.layer_general_layout.addWidget(
            self.material_ir_emissivity_textbox, 7, 1)
        '''
        self.layer_general_layout.addWidget(
            self.material_transmittance_label, 8, 0)
        self.layer_general_layout.addWidget(
            self.material_transmittance_textbox, 8, 1)
        '''
        self.layer_general_layout.addWidget(self.layer_save_button, 9, 0)
        self.layer_general_layout.addWidget(self.layer_cancel_button, 9, 1)

        self.layer_build_ui_window_layout.addWidget(
            self.layer_general_layout_group_box)
        self.layer_build_ui.setWindowModality(Qt.ApplicationModal)
        self.layer_build_ui.show()

    def display_current_building(self):
        '''Displays the current Building

        if some values of the current builing has changed, this method shows
        the updated building in the GUI.
        If the building is switched all the values of the new Building will
        taken over and displayed.
        '''

        if (self.current_building):

            """ Displaying values on the sidebar controls"""

            self.side_bar_id_line_edit.setText(
                str(self.current_building.name))
            self.side_bar_construction_year_line_edit.setText(
                str(self.current_building.year_of_construction))
            self.side_bar_height_of_floors_line_edit.setText(
                str(self.current_building.height_of_floors))
            self.side_bar_location_line_edit.setText(
                str(self.current_building.city))
            self.side_bar_net_leased_area_line_edit.setText(
                str(self.current_building.net_leased_area))
            self.side_bar_number_of_floors_line_edit.setText(
                str(self.current_building.number_of_floors))
            self.side_bar_street_line_edit.setText(
                str(self.current_building.street_name))

            """ updates the combobox displaying all buildings """

            try:
                if (self.side_bar_buildings_combo_box.findData(
                        str(self.current_building.internal_id)) == -1):
                    self.side_bar_buildings_combo_box.addItem(
                        self.current_building.name,
                        str(self.current_building.internal_id))
                    self.side_bar_buildings_combo_box.setCurrentIndex(
                        self.side_bar_buildings_combo_box.findData(
                            str(self.current_building.internal_id)))
                elif (self.side_bar_buildings_combo_box.currentText !=
                      self.side_bar_id_line_edit.text):
                    self.side_bar_buildings_combo_box.setItemText(
                        self.side_bar_buildings_combo_box.currentIndex(),
                        self.current_building.name)
            except AttributeError:
                pass

            """ Displaying zones in the two list views in the main frame """

            self.zone_model.clear()
            self.outer_elements_model.clear()
            self.element_model.clear()
            for zone in self.project.\
                buildings[self.project.buildings.index(
                    self.current_building)].thermal_zones:
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(zone.name) +
                    "\n" + "Type:\t".expandtabs(11) +
                    str(type(zone).__name__) + "\n Area:\t".expandtabs(11) +
                    str(zone.area), zone.internal_id)
                self.zone_model.appendRow(item)
                if zone.inner_walls:
                    for inner_wall in zone.inner_walls:
                        if type(inner_wall).__name__ == \
                                "InnerWall":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) + str(inner_wall.name)
                                + "\nType:\t".expandtabs(11) +
                                "Inner Wall \n Area:\t".expandtabs(11) +
                                str(inner_wall.area), inner_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(inner_wall).__name__ == \
                                "Floor":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) + str(inner_wall.name)
                                + "\nType:\t".expandtabs(11) +
                                "Floor \n Area:\t".expandtabs(11) +
                                str(inner_wall.area), inner_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(inner_wall).__name__ == \
                                "Ceiling":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) + str(inner_wall.name)
                                + "\nType:\t".expandtabs(11) +
                                "Ceiling \n Area:\t".expandtabs(11) +
                                str(inner_wall.area), inner_wall.internal_id)
                            self.element_model.appendRow(item)
                if zone.outer_walls:
                    for outer_wall in zone.outer_walls:
                        if type(outer_wall).__name__ == \
                                "GroundFloor":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) +
                                str(outer_wall.name) +
                                "\nType:\t".expandtabs(11) +
                                "Ground Floor \n Area:\t".expandtabs(11) +
                                str(outer_wall.area) +
                                "\n Orientation:\t".expandtabs(11) +
                                str(outer_wall.orientation),
                                outer_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(outer_wall).__name__ == \
                                "Rooftop":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) +
                                str(outer_wall.name) +
                                "\nType:\t".expandtabs(11) +
                                "Rooftop \n Area:\t".expandtabs(11) +
                                str(outer_wall.area) +
                                "\n Orientation:\t".expandtabs(11) +
                                str(outer_wall.orientation),
                                outer_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(outer_wall).__name__ == \
                                "OuterWall":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) +
                                str(outer_wall.name) +
                                "\nType:\t".expandtabs(11) +
                                "Outer Wall \n Area:\t".expandtabs(11) +
                                str(outer_wall.area) +
                                "\n Orientation:\t".expandtabs(11) +
                                str(outer_wall.orientation),
                                outer_wall.internal_id)
                            self.element_model.appendRow(item)
                if zone.windows:
                    for window in zone.windows:
                        item = TrackableItem(
                            "Name:\t".expandtabs(8) + str(window.name) +
                            "\nType:\t".expandtabs(11) +
                            "Windows \n Area:\t".expandtabs(11) +
                            str(window.area) +
                            "\n Orientation:\t".expandtabs(11) +
                            str(window.orientation),
                            window.internal_id)
                        self.element_model.appendRow(item)

            for orientation in self.guiinfo.orientations_numbers.keys():
                if self.current_building.get_outer_wall_area(orientation) != 0:
                    if orientation == -1:
                        item1 = QStandardItem(
                         "Rooftop \nOrientation:\t" +
                         str(self.guiinfo.orientations_numbers[orientation]) +
                         "\t".expandtabs(12) + "\n" + " Area: " +
                         str(self.current_building.
                             get_outer_wall_area(orientation)))

                    elif orientation == -2:
                        item1 = QStandardItem(
                         "Ground Floor \nOrientation:\t" +
                         str(self.guiinfo.orientations_numbers[orientation]) +
                         "\t".expandtabs(12) + "\n" + " Area: " +
                         str(self.current_building.
                             get_outer_wall_area(orientation)))
                    else:
                        item1 = QStandardItem(
                         "Outer Wall \nOrientation:\t" +
                         str(self.guiinfo.orientations_numbers[orientation]) +
                         "\t".expandtabs(12) + "\n" + " Area: " +
                         str(self.current_building.
                             get_outer_wall_area(orientation)))

                    self.outer_elements_model.appendRow(item1)

                if self.current_building.get_window_area(orientation) != 0:
                    item2 = QStandardItem(
                        "Window \nOrientation:\t" +
                        str(self.guiinfo.orientations_numbers[orientation]) +
                        "\t".expandtabs(16) + "\n" + " Area: " +
                        str(self.current_building.
                            get_window_area(orientation)))
                    self.outer_elements_model.appendRow(item2)

    def display_current_zone(self):
        '''Displays the current zone

        update and display the zone lists in the main window.
        '''

        if (self.current_zone):
            self.element_model.clear()
            self.edit_zone_area_line_edit.setText(str(self.current_zone.area))
            self.edit_zone_name_line_edit.setText(str(self.current_zone.name))
            self.edit_zone_volume_line_edit.setText(
                str(self.current_zone.volume))
            for inner_wall in self.current_zone.inner_walls:
                if type(inner_wall).__name__ == "InnerWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Inner Wall \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == "Floor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Floor \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == "Ceiling":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) +
                        "\nType:\t".expandtabs(11) +
                        "Ceiling \n Area:\t".expandtabs(11) +
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
            for element in self.current_zone.outer_walls:
                if type(element).__name__ == "GroundFloor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(element.name) +
                        "\nType:\t".expandtabs(11) +
                        "Ground Floor \n Area:\t".expandtabs(11) +
                        str(element.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(element.orientation),
                        element.internal_id)
                    self.element_model.appendRow(item)
                if type(element).__name__ == "Rooftop":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(element.name) +
                        "\nType:\t".expandtabs(11) +
                        "Rooftop \n Area:\t".expandtabs(11) +
                        str(element.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(element.orientation),
                        element.internal_id)
                    self.element_model.appendRow(item)
                if type(element).__name__ == "OuterWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) +
                        str(element.name) +
                        "\nType:\t".expandtabs(11) +
                        "Outer Wall \n Area:\t".expandtabs(11) +
                        str(element.area) +
                        "\n Orientation:\t".expandtabs(11) +
                        str(element.orientation),
                        element.internal_id)
                    self.element_model.appendRow(item)
            for element in self.current_zone.windows:
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(element.name) +
                    "\nType:\t".expandtabs(11) +
                    "Window \n Area:\t".expandtabs(11) +
                    str(element.area) + "\n Orientation:\t".expandtabs(11) +
                    str(element.orientation), element.internal_id)
                self.element_model.appendRow(item)

    def display_current_element(self):
        '''Displays the current element

        transfers all relevant values of the current element to gui controls
        like text fields and the list of layers.
        '''

        if (self.current_element):

            """ Displaying values on the sidebar controls"""

            self.edit_element_name_line_edit.setText(
                str(self.current_element.name))
            self.edit_element_area_line_edit.setText(
                str(self.current_element.area))
            self.edit_element_type_line_edit.setText(
                str(self.current_element.construction_type))

            """ Displaying layer in the list of layers in the main frame """

            self.layer_model.clear()
            for layer in self.current_element.layer:
                item = TrackableItem("Name:\t".expandtabs(8) +
                                     str(layer.id) + "\n" +
                                     "Material:\t".expandtabs(11) +
                                     str(layer.material.name) +
                                     "\n Thickness:\t".expandtabs(11) +
                                     str(layer.thickness), layer.internal_id)
                self.layer_model.appendRow(item)

    def display_current_layer(self):
        '''Displays the current layer

        transfers all relevant values of the current layer to gui text fields.
        '''

        if (self.current_layer):

            self.edit_layer_name_line_edit.setText(
                str(self.current_layer.id))
            self.edit_layer_thickness_line_edit.setText(
                str(self.current_layer.thickness))
            self.edit_layer_material_name_line_edit.setText(
                str(self.current_layer.material.name))
            self.edit_layer_density_line_edit.setText(
                str(self.current_layer.material.density))
            self.edit_layer_thermal_conduct_line_edit.setText(
                str(self.current_layer.material.thermal_conduc))
            self.edit_layer_heat_capacity_line_edit.setText(
                str(self.current_layer.material.heat_capac))
            self.edit_layer_solar_absorp_line_edit.setText(
                str(self.current_layer.material.solar_absorp))
            self.edit_layer_ir_emissivity_line_edit.setText(
                str(self.current_layer.material.ir_emissivity))
            self.edit_layer_transmittance_line_edit.setText(
                str(self.current_layer.material.transmittance))

    def click_save_current_project(self):
        '''Saves the project

        opens a dialog window for the user to input a path then issues the
        controller to create and save the file.
        '''

        path = QtGui.QFileDialog.getSaveFileName(
            caption='Choose Filepath',
            directory=utilitis.get_default_path()+"/"+self.project.name,
            filter="Teaser File (*.teaserXML);; GML (*.gml)")
        last_name = path.split('/')
        length = len(last_name)
        last_part = str(last_name[length-1])
        if last_part.endswith("teaserXML"):
            self.project.name = last_part[:-10]
        elif last_part.endswith("gml"):
            self.project.name = last_part[:-4]
        Controller.click_save_button(self.project, str(path))

    def click_export_button(self):
        '''Executes the export

        execute model after export is clicked, differentiate between current
        and all buildings.
        '''

        # path in GUI, which is need for the output
        path_output_folder = str(self.export_save_template_lineedit.text())

        list_of_building_name = []
        for i in range(self.side_bar_buildings_combo_box.count()):
            list_of_building_name.append(
                self.side_bar_buildings_combo_box.itemText(i))

        if self.export_create_library_combobox.currentText() == "AixLib":
            sender = self.sender()
            building_model = \
                self.export_create_template_model_combobox.currentText()
            zone_model = \
                self.export_create_template_zone_combobox.currentText()
            if self.radio_button_corG_1.isChecked():
                corG = True
            elif self.radio_button_corG_2.isChecked():
                corG = False
            elemInCombobox = \
                self.export_create_template_model_combobox.currentText()

            if(sender.text() == self.export_button.text()):
                Controller.click_export_button(self.project, building_model,
                                               zone_model, corG, None,
                                               path_output_folder)
                QtGui.QMessageBox.information(self, 'Message',
                                              "Export Modelica " +
                                              "record " + elemInCombobox +
                                              " all building finished ")
            elif(sender.text() == self.export_button_one.text()):
                Controller.click_export_button(self.project, building_model,
                                               zone_model, corG,
                                               self.current_building.internal_id,
                                               path_output_folder)
                QtGui.QMessageBox.information(self, 'Message',
                                              "Export Modelica " +
                                              "record " + elemInCombobox +
                                              " for current building " +
                                              "finished ")

        elif self.export_create_library_combobox.currentText() == "Annex60":
            sender = self.sender()
            num_of_elem = int(
                self.annex_create_number_of_elements_combobox.currentText())
            if self.annex_create_merge_windows_combobox.currentText() == \
               "True":
                    merge_win = True
            else:
                    merge_win = False

            if(sender.text() == self.export_button.text()):
                Controller.click_export_button_annex(
                                               self.project, num_of_elem,
                                               merge_win, None,
                                               path_output_folder)
                QtGui.QMessageBox.information(self, 'Message',
                                              "Export Modelica " +
                                              "record " + "Annex" +
                                              " all building finished ")
            elif(sender.text() == self.export_button_one.text()):
                Controller.click_export_button_annex(
                                               self.project, num_of_elem,
                                               merge_win,
                                               self.current_building.internal_id,
                                               path_output_folder)
                QtGui.QMessageBox.information(self, 'Message',
                                              "Export Modelica " +
                                              "record " + "Annex" +
                                              " for current building " +
                                              "finished ")

        utilitis.create_path(str(self.file_path))

    def click_browse_button(self):
        '''Browses beetween the Directory

        opens a dialog window for the user to search the location for the 
        output files.
        '''

        self.export_save_template_lineedit.setText(QtGui.QFileDialog.
                                                   getExistingDirectory())
        if self.export_save_template_lineedit.text() != "":
            utilitis.create_path(self.export_save_template_lineedit.text())
            self.file_path = self.export_save_template_lineedit.text()
        else:
            self.export_save_template_lineedit.setText(self.file_path)
            
    def click_update_building(self):
        ''' Updates a existing building 
            
        '''
        sender = self.sender()
        if(sender.text() == self.warning_window_save_button.text()):
            update_archtertype = False
        elif(sender.text() == self.warning_window_update_button.text()):
            update_archtertype = True   
            
        self.project = Controller.click_update_building_button(
                        self.project,
                        self.current_building,
                        str(self.side_bar_id_line_edit.text()),
                        str(self.side_bar_construction_year_line_edit.text()),
                        float(self.side_bar_number_of_floors_line_edit.text()),
                        float(self.side_bar_height_of_floors_line_edit.text()),
                        float(self.side_bar_net_leased_area_line_edit.text()),
                        str(self.side_bar_street_line_edit.text()),
                        str(self.side_bar_location_line_edit.text()),
                        update_archtertype)
        self.display_current_building()

    def click_browse_button_xml(self):
        '''Browses beetween the Directory

        opens a dialog window for the user to search the location.
        '''

        self.generate_new_xml_ui_path_line_edit.setText(QtGui.QFileDialog.getOpenFileName())

    def switch_building(self):
        '''Handles the buildings combobox

        updates the displayed details of the selected building after the
        building is switched.
        '''

        cIndex = self.side_bar_buildings_combo_box.currentIndex()
        for building in self.project.buildings:
            fIndex = self.side_bar_buildings_combo_box.findData(
                str(building.internal_id))
            if fIndex == cIndex:
                self.current_building = building
                self.display_current_building()

    def switch_type_building(self):
        '''Switches between the type buildings

        after changing the index of the combobox this function replaces the
        controls to fit the current type building.
        '''

        cIndex = self.window_construct_building_combo_box.currentText()
        self.current_type_building = str(cIndex)
        self.construct_type_building_button.setText(
            u"Generate " + self.current_type_building + " Building ...")
        if self.current_type_building == "SingleFamilyDwelling":
            self.group_box_type_building_right_office.setVisible(False)
            self.group_box_type_building_right_residential.setVisible(True)
            self.group_box_office_architecture.setVisible(False)
            self.group_box_residential_architecture.setVisible(True)
            self.construct_type_building_button.clicked.disconnect()
            self.connect(self.construct_type_building_button, SIGNAL(
                "clicked()"), self.check_inputs_typebuilding)
            self.connect(self.construct_type_building_button, SIGNAL(
                "clicked()"), self.popup_window_type_building,
                QtCore.SLOT("close()"))
        elif self.current_type_building == "Office" or self.current_type_building ==\
            "Institute 4" or self.current_type_building == "Institute 8" or\
                self.current_type_building == "Institute General":
            self.group_box_type_building_right_office.setVisible(True)
            self.group_box_type_building_right_residential.setVisible(False)
            self.group_box_office_architecture.setVisible(True)
            self.group_box_residential_architecture.setVisible(False)
            self.construct_type_building_button.clicked.disconnect()
            self.connect(self.construct_type_building_button, SIGNAL(
                "clicked()"), self.check_inputs_typebuilding)
            self.connect(self.construct_type_building_button, SIGNAL(
                "clicked()"), self.popup_window_type_building,
                QtCore.SLOT("close()"))

    def switch_current_zone_type(self):
        '''Switches between the types of a zone

        if the type of the current zone is swapped, this gets the values for
        the new type and updates the window.
        '''

        zone_type = self.zone_type_combobox.currentText()
        self.project = Controller.switch_zone_type(
            zone_type, self.project, self.current_zone.internal_id)
        self.update_zone_details()

    def switch_current_zone(self):
        '''Switches between the zones

        switches the current zone if the user clicks on it used for things
        like delete_thermal_zone.
        '''

        current_item = self.zone_model.itemFromIndex(
            self.edit_zone_list.currentIndex())
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == current_item.internal_id:
                self.current_zone = zone
        self.display_current_zone()

    def switch_current_element(self):
        '''Switch between the elements #

        switches the current element if the user clicks on it used for things
        like delete_current_element.
        '''

        current_item = self.element_model.itemFromIndex(
            self.edit_element_list.currentIndex())
        for element in self.current_zone.outer_walls:
            if element.internal_id == current_item.internal_id:
                self.current_element = element
        for element in self.current_zone.inner_walls:
            if element.internal_id == current_item.internal_id:
                self.current_element = element
        for element in self.current_zone.windows:
            if element.internal_id == current_item.internal_id:
                self.current_element = element
        self.display_current_element()

    def switch_lib(self):
        if self.export_create_library_combobox.currentText() == "AixLib":
            # self.export_model_groupbox = self.aixlib_groupbox
            self.annex_groupbox.setVisible(False)
            self.aixlib_groupbox.setVisible(True)
        else:
            # self.export_model_groupbox = self.annex_groupbox
            self.aixlib_groupbox.setVisible(False)
            self.annex_groupbox.setVisible(True)
        """
        if self.export_create_library_combobox.currentText() == "AixLib":

        else:
            self.aixlib_groupbox.setVisible(False)
            self.annex_groupbox.setVisible(True)
        """

    def switch_current_layer(self):
        '''Switches between the layers

        switches the current layer if the user clicks on it  used for things
        like delete_current_layer.
        '''

        current_item = self.layer_model.itemFromIndex(
            self.edit_current_layer_list.currentIndex())
        for layer in self.current_element.layer:
            if layer.internal_id == current_item.internal_id:
                self.current_layer = layer
        self.display_current_layer()

    def switch_constr_type(self):
        '''changes the construction type

        after changing the index of the combobox this function disconnects the
        layers of the element and after pressing the save button it updates
        the layers.
        '''

        try:
            self.construction_type_switched = True
            self.element_material_list_view.doubleClicked.disconnect()
        except:
            pass

    def switch_material(self):
        '''Switches between the materials

        if the current material is swapped, this gets the values for the new
        type and updates the window
        '''

        if self.is_switchable:
            cIndex = self.material_combobox.currentText()
            for material in self.materials:
                fIndex = material.name
                if fIndex == cIndex:
                    self.current_layer.material.name = material.name
                    self.current_layer.material.density = material.density
                    self.current_layer.material.thermal_conduc = \
                        material.thermal_conduc
                    self.current_layer.material.heat_capac = \
                        material.heat_capac
                    self.material_density_textbox.setText(
                        str(self.current_layer.material.density))
                    self.material_thermal_conduc_textbox.setText(
                        str(self.current_layer.material.thermal_conduc))
                    self.material_heat_capac_textbox.setText(
                        str(self.current_layer.material.heat_capac))

    def add_thermal_zone(self):
        '''Adds a new thermal zone

        checks if a building exists, if it does opens a window to create
        a new zone.
        '''

        if(self.current_building == 0):
            QtGui.QMessageBox.warning(self,
                                      u"No building error!",
                                      u"You need to specify a building first.")
        else:
            self.generate_zone_ui()

    def warning_delete_building(self):
        '''Warning message

        Warning message, which checks if user really want to delete a building.
        '''

        message_box = QtGui.QMessageBox()
        message_box.setWindowIcon(self.teaser_icon)
        message_box.setWindowTitle("Warning")
        message_box.setText("Are you really want to detele it?")

        message_box.addButton(QtGui.QPushButton('Delete'),
                              QtGui.QMessageBox.YesRole)
        message_box.addButton(QtGui.QPushButton('Cancel'),
                              QtGui.QMessageBox.RejectRole)
        message_box.buttonClicked.connect(self.delete_building_message_box)
        message_box.exec_()

    def delete_building_message_box(self, button):
        '''checks if the delete button is pressed if it is deletes selected
        building'''

        if button.text() == "Delete":
            self.delete_building()

    def delete_building(self):
        '''Checks if a building exists, if it does the currently
        selected building is deleted from the Project.
        '''

        if (self.current_building == 0):
            QtGui.QMessageBox.warning(self, u"No building error!",
                                      u"You need to specify a building first.")
        else:
                for building in self.project.buildings:
                    if building.internal_id == self.current_building.internal_id:
                        ind = self.project.buildings.index(building)
                self.project.buildings.pop(ind)
                self.current_building = 0
                self.current_zone = 0
                self.current_element = 0
                self.current_layer = 0
                self.zone_model.clear()
                self.outer_elements_model.clear()
                self.element_model.clear()
                self.layer_model.clear()
                self.buildings_combo_box_model.removeColumn(ind+1)
                self.side_bar_buildings_combo_box.removeItem(ind)
                self.side_bar_construction_year_line_edit.clear()
                self.side_bar_height_of_floors_line_edit.clear()
                self.side_bar_id_line_edit.clear()
                self.side_bar_location_line_edit.clear()
                self.side_bar_net_leased_area_line_edit.clear()
                self.side_bar_number_of_floors_line_edit.clear()
                self.side_bar_street_line_edit.clear()
                self.display_current_building()

    def delete_thermal_zone(self):
        '''Deletes a thermal zone

        checks if a building exists, if it does the currentlyselected zone
        is deleted from the current building.
        '''

        if (self.current_building == 0):
            QtGui.QMessageBox.warning(self, u"No building error!",
                                      u"You need to specify a building first.")
        else:
            try:
                item = self.zone_model.itemFromIndex(
                    self.zones_list_view.currentIndex())
                for building in self.project.buildings:
                    for zone in building.thermal_zones:
                        if (zone.internal_id == item.internal_id):
                            ind = building.thermal_zones.index(zone)
                            building.thermal_zones[ind].delete()
                            self.display_current_building()
            except (ValueError, AttributeError):
                QtGui.QMessageBox.warning(self,
                                          u"No zone selected",
                                          u"You need to select a"
                                          "thermal zone first.")

    def delete_current_element(self):
        '''Deletes an element

        checks if an element is currently selected and deletes the selected
        element.
        '''

        try:
            item = self.element_model.itemFromIndex(
                self.zone_element_list_view.currentIndex())
            for building in self.project.buildings:
                for zone in building.thermal_zones:
                    for element in zone.outer_walls:
                        if (element.internal_id == item.internal_id):
                            ind = zone.outer_walls.index(element)
                            del zone.outer_walls[ind]
                            self.update_zone_details()
                    for element in zone.inner_walls:
                        if (element.internal_id == item.internal_id):
                            ind = zone.inner_walls.index(element)
                            del zone.inner_walls[ind]
                            self.update_zone_details()
                    for element in zone.windows:
                        if (element.internal_id == item.internal_id):
                            ind = zone.windows.index(element)
                            del zone.windows[ind]
                            self.update_zone_details()
        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No element selected",
                                      u"You need to select an element first.")

    def delete_wall_in_xml(self):
        '''Deletes a wall

        checks if a wall is currently selected and deletes the selected wall.
        '''

        try:
            item = self.element_model_update_xml.itemFromIndex(
                    self.xml_ui_wall_list_view.currentIndex())
            zone = self.thermalZoneFromXML
            for wall in self.thermalZoneFromXML.inner_walls:
                if wall.internal_id == item.internal_id:
                    self.deleted_wall = wall
                    ind = zone.inner_walls.index(wall)
                    del zone.inner_walls[ind]
                    self.update_wall_details()
            for wall in zone.outer_walls:
                if wall.internal_id == item.internal_id:
                    self.deleted_wall = wall
                    ind = zone.outer_walls.index(wall)
                    del zone.outer_walls[ind]
                    self.update_wall_details()
            for wall in self.thermalZoneFromXML.windows:
                if wall.internal_id == item.internal_id:
                    self.deleted_wall = wall
                    ind = zone.windows.index(wall)
                    del zone.windows[ind]
                    self.update_wall_details()

        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No element selected",
                                      u"You need to select an element first.")

    def delete_selected_layer(self):
        '''Deletes a layer

        checks if a layer is currently selected and deletes the selected layer.
        '''

        try:
            item = self.element_layer_model.itemFromIndex(
                self.element_material_list_view.currentIndex())
            for building in self.project.buildings:
                for zone in building.thermal_zones:
                    for element in zone.outer_walls:
                        for current_layer in element.layer:
                            if (current_layer.internal_id == item.internal_id):
                                ind = element.layer.index(current_layer)
                                del element.layer[ind]
                                self.update_element_details()
                    for element in zone.inner_walls:
                        for current_layer in element.layer:
                            if (current_layer.internal_id == item.internal_id):
                                ind = element.layer.index(current_layer)
                                del element.layer[ind]
                                self.update_element_details()
                    for element in zone.windows:
                        for current_layer in element.layer:
                            if (current_layer.internal_id == item.internal_id):
                                ind = element.layer.index(current_layer)
                                del element.layer[ind]
                                self.update_element_details()
        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No layer selected",
                                      u"You need to select a layer first.")

    def delete_selected_layer_set_all_constr(self):
        '''Deletes a layer in set all construction window

        this function only operates in the set all construction window.
        It checks if a layer is currently selected and deletes the selected
        layer.
        '''

        try:
            item = self.element_layer_model_set_all_constr.itemFromIndex(
                self.set_all_constr_element_material_list_view.currentIndex())
            for current_layer in self.all_constr_layer_list:
                if (current_layer.internal_id == item.internal_id):

                    ind = self.all_constr_layer_list.index(current_layer)
                    del self.all_constr_layer_list[ind]
                    self.update_set_all_construction()

        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No layer selected",
                                      u"You need to select a layer first.")

    def delete_selected_layer_xml_window(self):
        '''Deletes a layer in xml window

        this function only operates in the xml window.
        Checks if a layer is selected and deletes it.
        '''

        try:
            item = self.element_layer_model_update_xml.itemFromIndex(
                self.generate_new_xml_ui_material_list_view.currentIndex())
            for current_layer in self.xml_layer_list:
                if (current_layer.internal_id == item.internal_id):
                    ind = self.xml_layer_list.index(current_layer)
                    del self.xml_layer_list[ind]
                    self.update_xml_window()

        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No layer selected",
                                      u"You need to select a layer first.")
            
    def delete_selected_layer_xml__modify_window(self):
        '''Deletes a layer in xml modify window

        this function only operates in the xml modify window.
        Checks if a layer is selected and deletes it.
        '''

        try:
            item = self.wall_layer_model.itemFromIndex(
                self.wall_material_list_view.currentIndex())

            for layer in self.current_wall.layer:
                if (layer.id == item.internal_id):
                    ind = self.current_wall.layer.index(layer)
                    del self.current_wall.layer[ind]
                    self.update_xml_window_modify()
        except (ValueError, AttributeError):
            QtGui.QMessageBox.warning(self,
                                      u"No layer selected",
                                      u"You need to select a layer first.")

    def delete_elements_in_lists(self, check):
        if (str(platform.python_version())).startswith('2'):
            if check == "Set all construction window":
                self.element_layer_model_set_all_constr = []
                self.all_constr_layer_list = []
            elif check == "Update XML":
                self.xml_layer_list = []
                self.element_layer_model_update_xml = []
        elif (str(platform.python_version())).startswith('3'):
            if check == "Set all construction window":
                self.element_layer_model_set_all_constr.clear()
                self.all_constr_layer_list.clear()
            elif check == "Update XML":
                self.xml_layer_list.clear()
                self.element_layer_model_update_xml.clear()


    def edit_building(self):
        '''Switch to an edit mode

        goes into edit mode and darkens the uneditable parts.
        '''

        # TODO: Ok das Design hat sich nicht wirklich durchgesetzt und
        # es funktioniert grad nicht besonders, Vorschlag: stattdessen
        # einfach ein Pop-Up Fenster wie bei Create-Type-Building, in dem
        # man building attribute die links am rand stehen ändern kann.
        if self.current_building:
            self.side_bar_construction_year_line_edit.setReadOnly(False)
            self.side_bar_height_of_floors_line_edit.setReadOnly(False)
            self.side_bar_id_line_edit.setReadOnly(False)
            self.side_bar_location_line_edit.setReadOnly(False)
            self.side_bar_net_leased_area_line_edit.setReadOnly(False)
            self.side_bar_number_of_floors_line_edit.setReadOnly(False)
            self.side_bar_street_line_edit.setReadOnly(False)
            self.saved_values_for_edit["year"] = \
                self.side_bar_construction_year_line_edit.text()
            self.saved_values_for_edit["height"] = \
                self.side_bar_height_of_floors_line_edit.text()
            self.saved_values_for_edit["id"] = \
                self.side_bar_id_line_edit.text()
            self.saved_values_for_edit["location"] = \
                self.side_bar_location_line_edit.text()
            self.saved_values_for_edit["area"] = \
                self.side_bar_net_leased_area_line_edit.text()
            self.saved_values_for_edit["number"] = \
                self.side_bar_number_of_floors_line_edit.text()
            self.saved_values_for_edit["street"] = \
                self.side_bar_street_line_edit.text()

            self.mask_label_0.setVisible(True)
            self.mask_label_0.raise_()
            self.mask_label_1.setVisible(True)
            self.mask_label_1.raise_()
            self.mask_label_2.setVisible(True)
            self.mask_label_2.raise_()
            self.mask_label_3.setVisible(True)
            self.mask_label_3.raise_()
            self.mask_label_4.setVisible(True)
            self.mask_label_4.raise_()
            self.mask_label_5.setVisible(True)
            self.mask_label_5.raise_()
            self.mask_label_6.setVisible(True)
            self.mask_label_6.raise_()
            self.mask_label_7.setVisible(True)
            self.mask_label_7.raise_()
            self.mask_label_8.setVisible(True)
            self.mask_label_8.raise_()

            self.mask_label_9.setVisible(True)
            self.mask_label_9.raise_()
            self.mask_button_1.setVisible(True)
            self.mask_button_1.raise_()
            self.mask_button_2.setVisible(True)
            self.mask_button_2.raise_()
            self.current_transformation = "ebui"
        else:
            QtGui.QMessageBox.warning(self,
                                      u"No building error!",
                                      u"You need to specify a building first.")

    def edit_building_save(self):
        '''Disables edit mode after saving

        changes the program back after saving changes.
        '''

        # TODO: Siehe TODO in edit_building

        self.mask_label_0.setVisible(False)
        self.mask_label_1.setVisible(False)
        self.mask_label_2.setVisible(False)
        self.mask_label_3.setVisible(False)
        self.mask_label_4.setVisible(False)
        self.mask_label_5.setVisible(False)
        self.mask_label_6.setVisible(False)
        self.mask_label_7.setVisible(False)
        self.mask_label_8.setVisible(False)
        self.mask_label_9.setVisible(False)
        self.mask_button_1.setVisible(False)
        self.mask_button_2.setVisible(False)
        self.side_bar_construction_year_line_edit.setReadOnly(True)
        self.side_bar_height_of_floors_line_edit.setReadOnly(True)
        self.side_bar_id_line_edit.setReadOnly(True)
        self.side_bar_location_line_edit.setReadOnly(True)
        self.side_bar_net_leased_area_line_edit.setReadOnly(True)
        self.side_bar_number_of_floors_line_edit.setReadOnly(True)
        self.side_bar_street_line_edit.setReadOnly(True)
        self.current_building.year_of_construction = \
            self.side_bar_construction_year_line_edit.text()
        self.current_building.height_of_floors = \
            self.side_bar_height_of_floors_line_edit.text()
        self.current_building.name = self.side_bar_id_line_edit.text()
        self.current_building.city = self.side_bar_location_line_edit.text()
        self.current_building.net_leased_area = \
            self.side_bar_net_leased_area_line_edit.text()
        self.current_building.number_of_floors = \
            self.side_bar_number_of_floors_line_edit.text()
        self.current_building.street_name = \
            self.side_bar_street_line_edit.text()
        self.display_current_building()

    def edit_building_cancel(self):
        '''Cancels edit mode 

        changes the program back after cancelling changes.
        '''

        # TODO: Siehe TODO in edit_building

        self.mask_label_0.setVisible(False)
        self.mask_label_1.setVisible(False)
        self.mask_label_2.setVisible(False)
        self.mask_label_3.setVisible(False)
        self.mask_label_4.setVisible(False)
        self.mask_label_5.setVisible(False)
        self.mask_label_6.setVisible(False)
        self.mask_label_7.setVisible(False)
        self.mask_label_8.setVisible(False)
        self.mask_label_9.setVisible(False)
        self.mask_button_1.setVisible(False)
        self.mask_button_2.setVisible(False)
        self.side_bar_construction_year_line_edit.setReadOnly(True)
        self.side_bar_height_of_floors_line_edit.setReadOnly(True)
        self.side_bar_id_line_edit.setReadOnly(True)
        self.side_bar_location_line_edit.setReadOnly(True)
        self.side_bar_net_leased_area_line_edit.setReadOnly(True)
        self.side_bar_number_of_floors_line_edit.setReadOnly(True)
        self.side_bar_street_line_edit.setReadOnly(True)
        self.side_bar_construction_year_line_edit.setText(
            self.saved_values_for_edit["year"])
        self.side_bar_height_of_floors_line_edit.setText(
            self.saved_values_for_edit["height"])
        self.side_bar_id_line_edit.setText(
            self.saved_values_for_edit["id"])
        self.side_bar_location_line_edit.setText(
            self.saved_values_for_edit["location"])
        self.side_bar_net_leased_area_line_edit.setText(
            self.saved_values_for_edit["area"])
        self.side_bar_number_of_floors_line_edit.setText(
            self.saved_values_for_edit["number"])
        self.side_bar_street_line_edit.setText(
            self.saved_values_for_edit["street"])

    def update_building(self):
        '''Updates building

        Updates all attributes of selected building, that are changed.
        '''

        index = self.side_bar_buildings_combo_box.currentIndex()
        self.check_inputs_typebuilding()

        self.project = Controller.click_update_building(self.project, index)

        self.buildings_combo_box_model.clear()
        self.side_bar_buildings_combo_box.clear()
        for building in self.project.buildings:
            self.side_bar_buildings_combo_box.addItem(
                building.name,
                str(building.internal_id))
        self.side_bar_buildings_combo_box.setCurrentIndex(index)
        self.display_current_building()

    def load_material(self):
        '''loads material

        if the current material is swapped, this gets the values for the new
        type and updates the window.
        '''

        try:
            cIndex = self.new_layerX_material_combobox.currentText()
            check = 0
        except:
            cIndex = self.new_layer_material_combobox.currentText()
            check = 1
        for material in self.materials:
            fIndex = material.name
            if fIndex == cIndex:

                if check == 0:
                    self.new_layerX_material_density_textbox.setText(
                        str(material.density))
                    self.new_layerX_material_thermal_conduc_textbox.setText(
                        str(material.thermal_conduc))
                    self.new_layerX_material_heat_capac_textbox.setText(
                        str(material.heat_capac))
                else:
                    self.new_layer_material_density_textbox.setText(
                        str(material.density))
                    self.new_layer_material_thermal_conduc_textbox.setText(
                        str(material.thermal_conduc))
                    self.new_layer_material_heat_capac_textbox.setText(
                        str(material.heat_capac))

    def load_building_button(self):
        '''Loads a building

        loads the chosen building from a dialog window and puts it on display.
        '''

        # click_save_current_project
        path = QtGui.QFileDialog.getOpenFileName(
            self, caption='Choose Filepath', directory='')
        if path:
            self.project = Controller.click_load_button(
                 self.project, str(path))
            self.project.modelica_info = ModelicaInfo()

            self.current_building = self.project.buildings[-1]
            self.display_current_building()

    def load_constr_type(self):
        '''loads a construction type

        the currently construction type and year of construction will be taken
        over to the element, after saving it.
        '''

        if self.construction_type_switched is True:
            self.current_element.load_type_element(
                int(self.element_year_of_construction_textbox.text()),
                str(self.element_construction_type_combobox.currentText()))

        self.construction_type_switched = False

    def fill_random_parameters(self):
        '''Fills attributes

        helper function which fills parameters with random values in generate
        office window.
        '''

        import random
        self.window_construct_building_name_line_edit.setText("Random")
        self.window_construct_building_street_line_edit.setText(
            "Random Street")
        self.window_construct_building_location_line_edit.setText(
            "Random City")
        value = str(random.randint(1900, 2015))
        self.window_construct_building_year_line_edit.setText(value)
        value = str(random.randint(1, 10))
        self.window_construct_building_number_of_floors_line_edit.setText(
            value)
        value = str(round(random.uniform(2.5, 5.5), 2))
        self.window_construct_building_height_of_floors_line_edit.setText(
            value)
        value = str(round(random.uniform(100, 10000), 2))
        self.window_construct_building_area_line_edit.setText(value)

    def fill_building_informations(self):
        '''Fills attributes

        function which fills parameters from the current building
        '''

        if(self.current_building == 0):
            QtGui.QMessageBox.warning(self,
                                      u"No building error!",
                                      u"You need to specify a building first.")
        else:
            if self.current_building.type_of_building == "Institute4":
                index = int(self.window_construct_building_combo_box.findText(
                            "Institute 4"))
            elif self.current_building.type_of_building == "Institute8":
                index = int(self.window_construct_building_combo_box.findText(
                            "Institute 8"))
            elif self.current_building.type_of_building == "Institute":
                index = int(self.window_construct_building_combo_box.findText(
                            "Institute General"))
            else:
                index = int(self.window_construct_building_combo_box.findText(
                            self.current_building.type_of_building))
            self.window_construct_building_combo_box.setCurrentIndex(index)
            self.window_construct_building_name_line_edit.setText(
                str(self.current_building.name))
            self.window_construct_building_street_line_edit.setText(
                str(self.current_building.street_name))
            self.window_construct_building_location_line_edit.setText(
                str(self.current_building.city))
            self.window_construct_building_year_line_edit.setText(
                str(self.current_building.year_of_construction))
            self.window_construct_building_number_of_floors_line_edit.setText(
                str(self.current_building.number_of_floors))
            self.window_construct_building_height_of_floors_line_edit.setText(
                str(self.current_building.height_of_floors))
            self.window_construct_building_area_line_edit.setText(
                str(self.current_building.net_leased_area))

            text = self.window_construct_building_combo_box.currentText()

            if text == "Office" or text == "Institute 4" or text ==\
                    "Institute 8" or text == "Institute General":
                if self.type_building_ind_att['layoutArea'] == 1:
                    self.radio_button_office_layout_1.setChecked(True)
                elif self.type_building_ind_att['layoutArea'] == 2:
                    self.radio_button_office_layout_2.setChecked(True)
                elif self.type_building_ind_att['layoutArea'] == 3:
                    self.radio_button_office_layout_3.setChecked(True)

                if self.type_building_ind_att['layoutWindowArea'] == 0:
                    self.radio_button_window_area_office_1.setChecked(True)
                elif self.type_building_ind_att['layoutWindowArea'] == 1:
                    self.radio_button_window_area_office_2.setChecked(True)
                elif self.type_building_ind_att['layoutWindowArea'] == 2:
                    self.radio_button_window_area_office_3.setChecked(True)
                elif self.type_building_ind_att['layoutWindowArea'] == 3:
                    self.radio_button_window_area_office_4.setChecked(True)

                if self.type_building_ind_att['constructionType'] == "heavy":
                    self.radio_button_architecture_office_1.setChecked(True)

                elif self.type_building_ind_att['constructionType'] == "light":
                    self.radio_button_architecture_office_2.setChecked(True)

            if text == "SingleFamilyDwelling":
                if self.type_building_ind_att['layoutArea'] == 0:
                    self.radio_button_residential_layout_1.setChecked(True)
                elif self.type_building_ind_att['layoutArea'] == 1:
                    self.radio_button_residential_layout_2.setChecked(True)
                elif self.type_building_ind_att['layoutArea'] == 2:
                    self.radio_button_residential_layout_3.setChecked(True)

                if self.type_building_ind_att['neighbour_building'] == 0:
                    self.radio_button_neighbour_1.setChecked(True)
                elif self.type_building_ind_att['neighbour_building'] == 1:
                    self.radio_button_neighbour_2.setChecked(True)
                elif self.type_building_ind_att['neighbour_building'] == 2:
                    self.radio_button_neighbour_3.setChecked(True)

                if self.type_building_ind_att['layout_attic'] == 0:
                    self.radio_button_residential_roof_1.setChecked(True)
                elif self.type_building_ind_att['layout_attic'] == 1:
                    self.radio_button_residential_roof_2.setChecked(True)
                elif self.type_building_ind_att['layout_attic'] == 2:
                    self.radio_button_residential_roof_3.setChecked(True)
                elif self.type_building_ind_att['layout_attic'] == 3:
                    self.radio_button_residential_roof_4.setChecked(True)

                if self.type_building_ind_att['layout_cellar'] == 0:
                    self.radio_button_residential_basement_1.setChecked(True)
                elif self.type_building_ind_att['layout_cellar'] == 1:
                    self.radio_button_residential_basement_2.setChecked(True)
                elif self.type_building_ind_att['layout_cellar'] == 2:
                    self.radio_button_residential_basement_3.setChecked(True)
                elif self.type_building_ind_att['layout_cellar'] == 3:
                    self.radio_button_residential_basement_4.setChecked(True)

                if self.type_building_ind_att['dormer'] == 1:
                    self.check_box_button_roof.setChecked(True)
                elif self.type_building_ind_att['dormer'] == 0:
                    self.check_box_button_roof.setChecked(False)

                if self.type_building_ind_att['constructionType'] == "heavy":
                    self.radio_button_residential_architecture_1.setChecked(
                                                                True)
                elif self.type_building_ind_att['constructionType'] == "light":
                    self.radio_button_residential_architecture_2.setChecked(
                                                                True)

    def fill_typebuilding_attributes(self):
        '''Fills type building attributes

        fills in values for type buildings from the comboboxes next to the
        pictures in the Create Type Building window.
        '''

        text = self.window_construct_building_combo_box.currentText()

        if text == "Office" or text == "Institute 4" or text ==\
                "Institute 8" or text == "Institute General":
            if self.radio_button_office_layout_1.isChecked():
                self.type_building_ind_att['layoutArea'] = 1
            if self.radio_button_office_layout_2.isChecked():
                self.type_building_ind_att['layoutArea'] = 2
            if self.radio_button_office_layout_3.isChecked():
                self.type_building_ind_att['layoutArea'] = 3
            if self.radio_button_window_area_office_1.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 0
            if self.radio_button_window_area_office_2.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 1
            if self.radio_button_window_area_office_3.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 2
            if self.radio_button_window_area_office_4.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 3
            if self.radio_button_architecture_office_1.isChecked():
                self.type_building_ind_att['constructionType'] = "heavy"
            if self.radio_button_architecture_office_2.isChecked():
                self.type_building_ind_att['constructionType'] = "light"
        if text == "SingleFamilyDwelling":
            if self.radio_button_residential_layout_1.isChecked():
                self.type_building_ind_att['layoutArea'] = 0
            if self.radio_button_residential_layout_2.isChecked():
                self.type_building_ind_att['layoutArea'] = 1
            if self.radio_button_neighbour_1.isChecked():
                self.type_building_ind_att['neighbour_building'] = 0
            if self.radio_button_neighbour_2.isChecked():
                self.type_building_ind_att['neighbour_building'] = 1
            if self.radio_button_neighbour_3.isChecked():
                self.type_building_ind_att['neighbour_building'] = 2
            if self.radio_button_residential_roof_1.isChecked():
                self.type_building_ind_att['layout_attic'] = 0
            if self.radio_button_residential_roof_2.isChecked():
                self.type_building_ind_att['layout_attic'] = 1
            if self.radio_button_residential_roof_3.isChecked():
                self.type_building_ind_att['layout_attic'] = 2
            if self.radio_button_residential_roof_4.isChecked():
                self.type_building_ind_att['layout_attic'] = 3
            if self.radio_button_residential_basement_1.isChecked():
                self.type_building_ind_att['layout_cellar'] = 0
            if self.radio_button_residential_basement_2.isChecked():
                self.type_building_ind_att['layout_cellar'] = 1
            if self.radio_button_residential_basement_3.isChecked():
                self.type_building_ind_att['layout_cellar'] = 2
            if self.radio_button_residential_basement_4.isChecked():
                self.type_building_ind_att['layout_cellar'] = 3
            if self.check_box_button_roof.isChecked():
                self.type_building_ind_att['dormer'] = 1
            else:
                self.type_building_ind_att['dormer'] = 0
            if self.radio_button_residential_architecture_1.isChecked():
                self.type_building_ind_att['constructionType'] = "heavy"
            if self.radio_button_residential_architecture_2.isChecked():
                self.type_building_ind_att['constructionType'] = "light"

    def key_press_event(self, event):
        ''' Implements shortcuts for the most important buttons
        '''

        # TODO: Ok also das hier funktioniert generell und tut auch schon
        # Problem: Der User muss die Shortcuts auch mitbekommen, also
        # am besten den jeweiligen shortcut-Buchstaben im Label unter dem
        # Button/ auf dem Button etwas hervorheben (unterstreichen oder fett machen)
        # Der Modifier ist STRG also müssten für die buttons bspw. STRG+C gedrückt werden.

        key = event.key()
        if key == QtCore.Qt.Key_C and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.generate_type_building_ui("Office")
        if key == QtCore.Qt.Key_E and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.create_new_building_ui()
        if key == QtCore.Qt.Key_P and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.create_new_project_ui()
        if key == QtCore.Qt.Key_Z and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.add_thermal_zone()
        if key == QtCore.Qt.Key_D and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.delete_thermal_zone()
        if key == QtCore.Qt.Key_L and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.load_building_button()
        if key == QtCore.Qt.Key_B and\
                QtGui.QApplication.keyboardModifiers() == \
                QtCore.Qt.ControlModifier:
            self.edit_building()

    def set_text_color(self, qObject, color):
        '''Sets the color of text

        switches the color of text between red and black.
        '''
        # werden soll, beim Löschen auf weitere Abhängigkeiten überprüfen!
        palette = QtGui.QPalette()
        if (color == "red"):
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
        if (color == "black"):
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.black)
        qObject.setPalette(palette)
        return qObject

class WizardPage(QtGui.QWizardPage):
    '''WizardPage class

    '''

    def closeEvent(self, evnt, elem_layer=None, layer_list=None):
        '''Describes a close event
        
        close event describes what is supposed to happen if a window is closed.
        In this case, all layers in set all construction window will cleared.
        '''

        if(elem_layer is not None or layer_list is not None):
            if (str(platform.python_version())).startswith('2'):
                elem_layer = []
                layer_list = []
            elif (str(platform.python_version())).startswith('3'):
                elem_layer.clear()
                layer_list.clear()


class EmittingStream(QtCore.QObject):
    '''Display the console

    part of the package to display the console in the project.
    '''

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass
