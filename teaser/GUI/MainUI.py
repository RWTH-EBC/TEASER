# created June 2015
# by TEASER4 Development Team

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QDialog, QStandardItemModel
from PyQt4.Qt import Qt
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QStandardItem, QTabWidget, QPixmap, QTabBar
import teaser.Logic.Utilis as utilis
from teaser.GUI.GUIHelperClasses.PictureButton import PictureButton
from teaser.Project import Project
from teaser.Logic.Controller.Controller import Controller
from teaser.Logic.Simulation.ModelicaInfo import ModelicaInfo
from teaser.GUI.GUIHelperClasses.TrackableItem import TrackableItem
from teaser.GUI.GUIHelperClasses.ListViewZonesFiller import ListViewZonesFiller
from teaser.GUI.GUIHelperClasses.GUIInfo import GUIInfo
import sys
import os
from numpy.distutils.pathccompiler import PathScaleCCompiler


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

    # Constructor defines all elements in the GUI and sets the listModels for
    # the listViews
    def __init__(self, parent=None, gui=True, dir=None, file=None):
        super(MainUI, self).__init__(parent)

        """ General layout and gui-global variables """

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stdin = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinMaxButtonsHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dailyHoursRange = range(0, 23)
        self.current_building = 0
        self.current_zone = 0
        self.current_element = 0
        self.current_layer = 0
        self.current_transformation = "standard"
        self.is_switchable = False
        self.type_building_ind_att = dict(layout_area=0.0,
                                          layout_window_area=0.0,
                                          layout_roof=0.0,
                                          layout_basement=0.0,
                                          construction_type=0.0,
                                          neighbour_building=0.0)
        self.saved_values_for_edit = {"year": "", "height": "", "name": "",
                                      "location": "", "area": "", "number": "",
                                      "street": ""}
        self.temp_zones = {}
        self.zone_model = QStandardItemModel()
        self.outer_elements_model = QStandardItemModel()
        self.element_model = QStandardItemModel()
        self.layer_model = QStandardItemModel()
        self.element_layer_model = QStandardItemModel()
        self.project = Project()
        self.project.modelica_info = ModelicaInfo()
        self.guiinfo = GUIInfo()
        self.lVZF = ListViewZonesFiller()
        self.is_empty_building_button = False
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(900, 800)
        self.setMinimumSize(QtCore.QSize(900, 800))
        self.setMaximumSize(QtCore.QSize(900, 800))
        teaserVersion = "4.1.1"
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
        self.mask_button_1 = QtGui.QPushButton(self.main_widget)
        self.mask_button_1.setGeometry(QtCore.QRect(265, 155, 95, 30))
        self.mask_button_1.setText("Save\n(Enter)")
        self.mask_button_1.setVisible(False)
        self.mask_button_1.clicked.connect(self.edit_building_save)
        self.mask_button_2 = QtGui.QPushButton(self.main_widget)
        self.mask_button_2.setGeometry(QtCore.QRect(365, 155, 95, 30))
        self.mask_button_2.setText("Cancel\n(Escape)")
        self.mask_button_2.setVisible(False)
        self.mask_button_2.clicked.connect(self.edit_building_cancel)
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
        self.image_1.load(utilis.get_full_path("GUI\\GUIImages\\Bild1.png"))
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
            "currentIndexChanged(int)"), self.switchBuilding)
        self.side_bar_id_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_id_label.setGeometry(QtCore.QRect(5, 60, 90, 25))
        self.side_bar_id_label.setText("Name:")
        self.side_bar_id_line_edit = QtGui.QLineEdit(self.side_bar_group_box)
        self.side_bar_id_line_edit.setGeometry(QtCore.QRect(105, 60, 90, 25))
        self.side_bar_id_line_edit.setReadOnly(True)
        self.side_bar_street_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_street_label.setGeometry(QtCore.QRect(5, 95, 90, 25))
        self.side_bar_street_label.setText("Street/Nr.:")
        self.side_bar_street_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_street_line_edit.setGeometry(
            QtCore.QRect(105, 95, 90, 25))
        self.side_bar_street_line_edit.setReadOnly(True)
        self.side_bar_location_label = QtGui.QLabel(self.side_bar_group_box)
        self.side_bar_location_label.setGeometry(QtCore.QRect(5, 130, 90, 25))
        self.side_bar_location_label.setText("ZIP/City:")
        self.side_bar_location_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_location_line_edit.setGeometry(
            QtCore.QRect(105, 130, 90, 25))
        self.side_bar_location_line_edit.setReadOnly(True)
        self.side_bar_construction_year_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_construction_year_label.setGeometry(
            QtCore.QRect(5, 165, 90, 25))
        self.side_bar_construction_year_label.setText("Construction Year:")
        self.side_bar_construction_year_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_construction_year_line_edit.setGeometry(
            QtCore.QRect(105, 165, 90, 25))
        self.side_bar_construction_year_line_edit.setReadOnly(True)
        self.side_bar_number_of_floors_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_number_of_floors_label.setGeometry(
            QtCore.QRect(5, 200, 90, 25))
        self.side_bar_number_of_floors_label.setText("Number of Floors:")
        self.side_bar_number_of_floors_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_number_of_floors_line_edit.setGeometry(
            QtCore.QRect(105, 200, 90, 25))
        self.side_bar_number_of_floors_line_edit.setReadOnly(True)
        self.side_bar_height_of_floors_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_height_of_floors_label.setGeometry(
            QtCore.QRect(5, 235, 90, 25))
        self.side_bar_height_of_floors_label.setText("Height of Floors:")
        self.side_bar_height_of_floors_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_height_of_floors_line_edit.setGeometry(
            QtCore.QRect(105, 235, 90, 25))
        self.side_bar_height_of_floors_line_edit.setReadOnly(True)
        self.side_bar_net_leased_area_label = QtGui.QLabel(
            self.side_bar_group_box)
        self.side_bar_net_leased_area_label.setGeometry(
            QtCore.QRect(5, 270, 90, 25))
        self.side_bar_net_leased_area_label.setText("Net leased Area:")
        self.side_bar_net_leased_area_line_edit = QtGui.QLineEdit(
            self.side_bar_group_box)
        self.side_bar_net_leased_area_line_edit.setGeometry(
            QtCore.QRect(105, 270, 90, 25))
        self.side_bar_net_leased_area_line_edit.setReadOnly(True)

        """ All controls in the ribbon """

        self.mask_label_4 = QtGui.QLabel(self.ribbon_group_box)
        self.mask_label_4.setGeometry(QtCore.QRect(0, 0, 899, 109))
        self.mask_label_4.setVisible(False)
        self.mask_label_4.setStyleSheet("background-color:rgba(0,0,0,80)")
        self.new_type_building_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Haus1.png")),
            self.ribbon_widget)
        self.new_type_building_button.setGeometry(QtCore.QRect(10, 5, 70, 70))
        self.new_type_building_button.clicked.connect(
            self.check_window_slide_typebuilding)
        self.new_type_building_button.setToolTip(
            "Click to create a new typebuilding.")
        self.new_type_building_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_type_building_label.setGeometry(QtCore.QRect(10, 80, 70, 25))
        self.new_type_building_label.setText("C" + "reate Exa- \nmple Building")
        self.new_empty_building_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\NewEmptyBuilding.png")),
            self.ribbon_widget)
        self.new_empty_building_button.setGeometry(QtCore.QRect(95, 5, 70, 70))
        self.new_empty_building_button.clicked.connect(
            self.create_new_building_ui)
        self.new_empty_building_button.setToolTip(
            "Creates a new building without any zones or values.")
        self.new_empty_building_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_empty_building_label.setGeometry(QtCore.QRect(95, 80, 70, 25))
        self.new_empty_building_label.setText("Create Emp- \nty Building")
        self.add_zone_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\AddZone.png")),
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
            utilis.get_full_path("GUI\\GUIImages\\DeleteZone.png")),
            self.ribbon_widget)
        self.delete_zone_button.setGeometry(QtCore.QRect(265, 5, 70, 70))
        self.delete_zone_button.clicked.connect(self.delete_thermal_zone)
        self.delete_zone_button.setToolTip(
            "Deletes the currently selected zone from this building.")
        self.delete_label = QtGui.QLabel(self.ribbon_group_box)
        self.delete_label.setGeometry(QtCore.QRect(265, 80, 70, 25))
        self.delete_label.setText("Delete Cur- \nrent Zone")
        self.edit_building_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\EditBuilding.png")),
            self.ribbon_widget)
        self.edit_building_button.setGeometry(QtCore.QRect(350, 5, 70, 70))
        self.edit_building_button.clicked.connect(self.edit_building)
        self.edit_building_button.setToolTip(
            "Switches to edit-mode. Allows modification of general"
            "building values.")
        self.edit_label = QtGui.QLabel(self.ribbon_group_box)
        self.edit_label.setGeometry(QtCore.QRect(350, 80, 70, 25))
        self.edit_label.setText("Edit\nBuilding")
        self.load_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Load.png")),
            self.ribbon_widget)
        self.load_button.setGeometry(QtCore.QRect(435, 5, 70, 70))
        self.load_button.clicked.connect(self.load_building_button)
        self.load_button.setToolTip("Loads a building from a .xml file.")
        self.load_label = QtGui.QLabel(self.ribbon_group_box)
        self.load_label.setGeometry(QtCore.QRect(435, 80, 70, 25))
        self.load_label.setText("Load\nBuilding")
        self.new_project_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Project_manager.png")),
            self.ribbon_widget)
        self.new_project_button.setGeometry(QtCore.QRect(520, 5, 70, 70))
        self.new_project_button.clicked.connect(self.create_new_project_ui)
        self.new_project_button.setToolTip("Creates a new Project.")
        self.new_project_label = QtGui.QLabel(self.ribbon_group_box)
        self.new_project_label.setGeometry(QtCore.QRect(520, 80, 70, 25))
        self.new_project_label.setText("Create empty\nProject")
        self.open_simulation_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.open_simulation_button.setGeometry(QtCore.QRect(605, 5, 70, 70))
        self.open_simulation_button.clicked.connect(
            self.show_simulation_window)
        self.open_simulation_button.setToolTip("Opens the Simulation Tab.")
        self.open_simulation_label = QtGui.QLabel(self.ribbon_group_box)
        self.open_simulation_label.setGeometry(QtCore.QRect(605, 80, 70, 25))
        self.open_simulation_label.setText("Open Simu-\n lation Tab")
        self.open_export_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.open_export_button.setGeometry(QtCore.QRect(685, 5, 70, 70))
        self.open_export_button.clicked.connect(
            self.show_export_window)
        self.open_export_button.setToolTip("Opens the Export Tab.")
        self.open_export_label = QtGui.QLabel(self.ribbon_group_box)
        self.open_export_label.setGeometry(QtCore.QRect(685, 80, 70, 25))
        self.open_export_label.setText("Open Ex-\n port Tab")
        self.save_project_button = PictureButton(QtGui.QPixmap(
            utilis.get_full_path("GUI\\GUIImages\\Keyschedule_rc4.png")),
            self.ribbon_widget)
        self.save_project_button.setGeometry(QtCore.QRect(765, 5, 70, 70))
        self.save_project_button.clicked.connect(
            self.click_save_current_project)
        self.save_project_button.setToolTip("Saves the current project.")
        self.save_project_label = QtGui.QLabel(self.ribbon_group_box)
        self.save_project_label.setGeometry(QtCore.QRect(765, 80, 70, 25))
        self.save_project_label.setText("Save Pro-\n ject Tab")

        self.side_animation = QtCore.QPropertyAnimation(
            self.side_bar_widget, "geometry")
        self.main_animation = QtCore.QPropertyAnimation(
            self.main_widget, "geometry")

    def __del__(self):
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()

    def check_window_slide_typebuilding(self):
        # if self.slide_mode_radiobutton.isChecked():
        #    self.transform_ctbui()
        # elif self.window_mode_radiobutton.isChecked():
        self.generate_type_building_ui("Office")

    def save_changed_layer_values(self):
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

    def save_changed_simulation_values(self):
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
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == self.current_zone.internal_id:
                for element in zone.inner_walls:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.inner_walls.index(element)
                        zone.inner_walls[index].name = \
                            self.element_name_textbox.text()
                        zone.inner_walls[index].construction_type = \
                            self.element_construction_type_combobox.\
                            currentText()
                        zone.inner_walls[index].orientation = \
                            self.element_orientation_combobox.currentText()
                        zone.inner_walls[index].area = \
                            float(self.element_area_textbox.text())
                        zone.inner_walls[index].year_of_construction = \
                            self.element_year_of_construction_textbox.text()
                        zone.inner_walls[index].year_of_retrofit = \
                            self.element_year_of_retrofit_textbox.text()
                        zone.inner_walls[index].tilt = \
                            self.element_tilt_textbox.text()
                        zone.inner_walls[index].inner_convection = \
                            float(self.element_inner_convection_textbox.text())
                        zone.inner_walls[index].inner_radiation = \
                            float(self.element_inner_radiation_textbox.text())
                        zone.inner_walls[index].ua_value = \
                            float(self.element_uvalue_textbox.text())
                for element in zone.outer_walls:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.outer_walls.index(element)
                        zone.outer_walls[index].name = \
                            self.element_name_textbox.text()
                        zone.outer_walls[index].construction_type = \
                            self.element_construction_type_combobox.\
                            currentText()
                        zone.outer_walls[index].orientation = \
                            self.element_orientation_combobox.currentText()
                        zone.outer_walls[index].area = \
                            float(self.element_area_textbox.text())
                        zone.outer_walls[index].year_of_construction = \
                            self.element_year_of_construction_textbox.text()
                        zone.outer_walls[index].year_of_retrofit = \
                            self.element_year_of_retrofit_textbox.text()
                        zone.outer_walls[index].tilt = \
                            self.element_tilt_textbox.text()
                        zone.outer_walls[index].inner_convection = \
                            float(self.element_inner_convection_textbox.text())
                        zone.outer_walls[index].inner_radiation = \
                            float(self.element_inner_radiation_textbox.text())
                        zone.outer_walls[index].ua_value = \
                            float(self.element_uvalue_textbox.text())
                        break
                for element in zone.windows:
                    if element.internal_id == self.current_element.internal_id:
                        index = zone.windows.index(element)
                        zone.windows[index].name = \
                            self.element_name_textbox.text()
                        zone.windows[index].construction_type = \
                            self.element_construction_type_combobox.\
                            currentText()
                        zone.windows[index].orientation = \
                            self.element_orientation_combobox.currentText()
                        zone.windows[index].area = \
                            float(self.element_area_textbox.text())
                        zone.windows[index].year_of_construction = \
                            self.element_year_of_construction_textbox.text()
                        zone.windows[index].year_of_retrofit = \
                            self.element_year_of_retrofit_textbox.text()
                        zone.windows[index].tilt = \
                            self.element_tilt_textbox.text()
                        zone.windows[index].inner_convection = \
                            float(self.element_inner_convection_textbox.text())
                        zone.windows[index].inner_radiation = \
                            float(self.element_inner_radiation_textbox.text())
                        zone.windows[index].ua_value = \
                            float(self.element_uvalue_textbox.text())
                        break

    def check_inputs_new_zone(self):

        """ Checks if all necessary values to create a new zone have been
        put in """

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
                self.current_building, self.generate_zone_name_line_edit.text(),
                self.generate_zone_area_line_edit.text(),
                self.generate_zone_usage_combobox.currentText())
            self.display_current_building()

    def check_inputs_edit_element(self):

        """ Takes input when the Save button is clicked on the
        edit element view """

        self.current_element.name = self.edit_element_name_line_edit.text()
        self.current_element.area = float(
            self.edit_element_area_line_edit.text())
        self.display_current_element()

    def check_inputs_edit_zone(self):

        """ Checks if all necessary values to edit a given zone are still
        not empty """

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

    def check_inputs_typebuilding_office(self):
        self.fill_typebuilding_attributes()
        self.project, id = Controller.click_generate_type_building_button(
            self.project,
            self.window_construct_building_name_line_edit.text(),
            self.window_construct_building_year_line_edit.text(),
            self.window_construct_building_number_of_floors_line_edit.text(),
            self.window_construct_building_height_of_floors_line_edit.text(),
            "Office",
            self.window_construct_building_area_line_edit.text(),
            self.window_construct_building_street_line_edit.text(),
            self.window_construct_building_location_line_edit.text(),
            self.type_building_ind_att)
        for building in self.project.list_of_buildings:
            if building.internal_id == id:
                self.current_building = building
        self.display_current_building()

    def check_inputs_typebuilding_residential(self):
        self.fill_typebuilding_attributes()
        self.project = Controller.click_generate_type_building_button(
            self.project,
            self.window_construct_building_name_line_edit.text(),
            self.window_construct_building_year_line_edit.text(),
            self.window_construct_building_number_of_floors_line_edit.text(),
            self.window_construct_building_height_of_floors_line_edit.text(),
            "Residential",
            self.window_construct_building_area_line_edit.text(),
            self.window_construct_building_street_line_edit.text(),
            self.window_construct_building_location_line_edit.text())
        self.project.list_of_buildings.append(self.current_building)
        self.display_current_building()

    def update_zone_details(self):
        self.element_model.clear()
        if self.current_zone.inner_walls:
            for inner_wall in self.current_zone.inner_walls:
                if type(inner_wall).__name__ == \
                "InnerWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                        "\nType:\t".expandtabs(11) + 
                        "Inner Wall \n Area:\t".expandtabs(11) + 
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == \
                "Floor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                        "\nType:\t".expandtabs(11) + 
                        "Floor \n Area:\t".expandtabs(11) + 
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == \
                "Ceiling":
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
                        "Roof Top \n Area:\t".expandtabs(11) + 
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

    def update_element_details(self):
        self.element_layer_model.clear()
        for layer in self.current_element.layer:
            item = TrackableItem(
                "Material:\t".expandtabs(8) + str(layer.material.name) + 
                "\nThickness:\t".expandtabs(14) + str(layer.thickness) + 
                "\t", layer.internal_id)
            self.element_layer_model.appendRow(item)

    def display_current_zone(self):

        """ Displays the values of the currently selected zone in the
        line edits """

        if (self.current_zone):
            self.element_model.clear()
            self.edit_zone_area_line_edit.setText(str(self.current_zone.area))
            self.edit_zone_name_line_edit.setText(str(self.current_zone.name))
            self.edit_zone_volume_line_edit.setText(
                str(self.current_zone.volume))
            # TODO: Ceiling Area etc.

            # self.edit_usage_infiltration_rate_line_edit.setText(
            # str(self.current_zone.use_conditions.infiltration_rate))
            # self.edit_usage_cooling_time_line_edit
            # self.edit_usage_heating_time_line_edit
            # self.edit_usage_set_temp_heat_line_edit
            # self.edit_usage_set_temp_cool_line_edit
            # self.edit_usage_temp_set_back_line_edit
            # self.edit_usage_min_air_exchange_line_edit
            # self.edit_usage_min_ahu_line_edit
            # self.edit_usage_max_ahu_line_edit
            # self.edit_usage_with_ahu_line_edit
            # self.edit_usage_rel_humidity_line_edit
            # self.edit_usage_persons_line_edit
            # self.edit_usage_machines_line_edit
            for inner_wall in self.current_zone.inner_walls:
                if type(inner_wall).__name__ == \
                "InnerWall":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                        "\nType:\t".expandtabs(11) + 
                        "Inner Wall \n Area:\t".expandtabs(11) + 
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == \
                "Floor":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                        "\nType:\t".expandtabs(11) + 
                        "Floor \n Area:\t".expandtabs(11) + 
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
                if type(inner_wall).__name__ == \
                "Ceiling":
                    item = TrackableItem(
                        "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                        "\nType:\t".expandtabs(11) + 
                        "Ceiling \n Area:\t".expandtabs(11) + 
                        str(inner_wall.area), inner_wall.internal_id)
                    self.element_model.appendRow(item)
            for element in self.current_zone.outer_walls:
                if type(element).__name__ == \
                        "GroundFloor":
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
                if type(element).__name__ == \
                        "Rooftop":
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
                if type(element).__name__ == \
                        "OuterWall":
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

    def switchBuilding(self):

        """ Triggers when the combobox for all buildings is used and changes
        all controls to the new building's values """

        cIndex = self.side_bar_buildings_combo_box.currentIndex()
        for building in self.project.list_of_buildings:
            fIndex = self.side_bar_buildings_combo_box.findData(
                str(building.internal_id))
            if fIndex == cIndex:
                self.current_building = building
                self.display_current_building_after_switching()

    def display_current_building_after_switching(self):

        """ Fills all text fields and lists with the buildings values
            Prevents an endless loop """

        if (self.current_building):

            """ Displaying values on the sidebar controls"""

            self.side_bar_id_line_edit.setText(str(self.current_building.name))
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

            """ Displaying zones in the two list views in the main frame """

            self.zone_model.clear()
            self.element_model.clear()
            for zone in self.project.\
                list_of_buildings[self.project.list_of_buildings.index(
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
                                "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                                "\nType:\t".expandtabs(11) + 
                                "Inner Wall \n Area:\t".expandtabs(11) + 
                                str(inner_wall.area), inner_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(inner_wall).__name__ == \
                        "Floor":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                                "\nType:\t".expandtabs(11) + 
                                "Floor \n Area:\t".expandtabs(11) + 
                                str(inner_wall.area), inner_wall.internal_id)
                            self.element_model.appendRow(item)
                        if type(inner_wall).__name__ == \
                        "Ceiling":
                            item = TrackableItem(
                                "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                                "\nType:\t".expandtabs(11) + 
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

    def display_current_building(self):

        """ Fills all text fields and lists with the buildings values """

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

            """ Updates the combobox displaying all buildings """

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
            for zone in self.project.\
                list_of_buildings[self.project.list_of_buildings.
                                  index(self.current_building)].thermal_zones:
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(zone.name) + 
                    "\n" + "Type:\t".expandtabs(11) + 
                    str(type(zone).__name__) + "\n Area:\t".expandtabs(11) + 
                    str(zone.area), zone.internal_id)
                self.zone_model.appendRow(item)

            for orientation in self.guiinfo.orientations_numbers.keys():
                if self.current_building.get_outer_wall_area(orientation) != 0:
                    item1 = QStandardItem(
                        "Outer Wall Orientation: " + 
                        str(self.guiinfo.orientations_numbers[orientation]) + 
                        "\t".expandtabs(12) + "\n" + " Area: " + 
                        str(self.current_building.
                            get_outer_wall_area(orientation)))
                    self.outer_elements_model.appendRow(item1)
                if self.current_building.get_window_area(orientation) != 0:
                    item2 = QStandardItem(
                        "Window Orientation: " + 
                        str(self.guiinfo.orientations_numbers[orientation]) + 
                        "\t".expandtabs(16) + "\n" + " Area: " + 
                        str(self.current_building.
                            get_window_area(orientation)))
                    self.outer_elements_model.appendRow(item2)
                    
    def click_save_current_project(self):
        path = QtGui.QFileDialog.getSaveFileName(
            caption='Choose Filepath',
            directory=utilis.get_default_path()+"\\"+self.project.name,
            filter="Teaser File (*.teaserXML);; GML (*.gml)")
        last_name = path.split('/')
        length = len(last_name)
        last_part = last_name[length-1]
        if last_part.endswith("teaserXML"):
            self.project.name = last_part[:-10]
        elif last_part.endswith("gml"):
            self.project.name = last_part[:-4]
        Controller.click_save_button(self.project, path)

    def click_export_button(self):
        # path in GUI, which is need for the output
        path_output_folder = str(self.export_save_template_lineedit.text())
        template_folder = self.create_path_to_template_folder()
        os.chdir(template_folder)

        for template_name in (os.listdir(template_folder)):
            if(self.export_create_template_combobox.currentText()
               == template_name):
                path_template = template_folder + template_name
                # pathTemplate shows which template will be used

        list_of_building_name = []
        for i in range(self.side_bar_buildings_combo_box.count()):
            list_of_building_name.append(
                self.side_bar_buildings_combo_box.itemText(i))
        sender = self.sender()
        if(sender.text() == self.export_button.text()):
            building_id = -1
            export_project = self.controller.clickExportButton(
                self.project, path_template,
                path_output_folder, building_id, list_of_building_name)
            os.chdir(path_output_folder)

        else:
            current_building_id = \
                self.side_bar_buildings_combo_box.currentIndex()
            currentBuildingName = \
                str(self.side_bar_buildings_combo_box.currentText())
            export_project = self.controller.clickExportButton(
                self.project, path_template, path_output_folder,
                current_building_id, currentBuildingName)
            os.chdir(path_output_folder)

    def create_path_to_template_folder(self,):
        path = "InputData\\RecordTemplate\\"
        pathTemplate = utilis.get_default_path()
        leng = len(pathTemplate)
        fullPath = pathTemplate[:leng - 10] + path
        return(str(fullPath))

    def display_current_element(self):

        """ Fills all text fields and lists with the element values """

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

    def fill_typebuilding_attributes(self):

        """ Returns specific values for the selected combo boxes for the
        layouts during creation of a new type building """

        if self.window_construct_building_combo_box.currentText() == "Office":
            if self.radio_button_office_layout_1.isChecked():
                self.type_building_ind_att['layoutArea'] = 1
            if self.radio_button_office_layout_2.isChecked():
                self.type_building_ind_att['layoutArea'] = 2
            if self.radio_button_office_layout_3.isChecked():
                self.type_building_ind_att['layoutArea'] = 3
            if self.radio_button_office_layout_4.isChecked():
                self.type_building_ind_att['layoutArea'] = 4
            if self.radio_button_window_area_office_1.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 1
            if self.radio_button_window_area_office_2.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 2
            if self.radio_button_window_area_office_3.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 3
            if self.radio_button_window_area_office_4.isChecked():
                self.type_building_ind_att['layoutWindowArea'] = 4
            if self.radio_button_architecture_office_1.isChecked():
                self.type_building_ind_att['constructionType'] = "light"
            if self.radio_button_architecture_office_2.isChecked():
                self.type_building_ind_att['constructionType'] = "heavy"
            if self.radio_button_architecture_office_3.isChecked():
                self.type_building_ind_att['constructionType'] = "light"
        if self.window_construct_building_combo_box.currentText() == \
                "Residential":
            if self.radio_button_neighbour_1.isChecked():
                self.type_building_ind_att['neighbour_building'] = 1
            if self.radio_button_neighbour_2.isChecked():
                self.type_building_ind_att['neighbour_building'] = 2
            if self.radio_button_neighbour_3.isChecked():
                self.type_building_ind_att['neighbour_building'] = 3
            if self.radio_button_residential_layout_1.isChecked():
                self.type_building_ind_att['layoutArea'] = 1
            if self.radio_button_residential_layout_2.isChecked():
                self.type_building_ind_att['layoutArea'] = 2
            if self.radio_button_residential_roof_1.isChecked():
                self.type_building_ind_att['layout_roof'] = 1
            if self.radio_button_residential_roof_1.isChecked():
                self.type_building_ind_att['layout_roof'] = 2
            if self.radio_button_residential_roof_1.isChecked():
                self.type_building_ind_att['layout_roof'] = 3
            if self.radio_button_residential_roof_1.isChecked():
                self.type_building_ind_att['layout_roof'] = 4

    def set_text_color(self, qObject, color):

        """ Sets the text color for a label/button/etc. to color """

        palette = QtGui.QPalette()
        if (color == "red"):
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
        if (color == "black"):
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.black)
        qObject.setPalette(palette)
        return qObject

    def add_thermal_zone(self):

        """ Adds a new zone to the current building """

        if(self.current_building == 0):
            QtGui.QMessageBox.warning(self,
                                      u"No building error!",
                                      u"You need to specify a building first.")
        else:
            self.generate_zone_ui()

    def switch_material(self):
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

    def delete_thermal_zone(self):

        """ Deletes the currently selected zone,
        throws an error if no zone is selected """

        if (self.current_building == 0):
            QtGui.QMessageBox.warning(self, u"No building error!",
                                      u"You need to specify a building first.")
        else:
            try:
                item = self.zone_model.itemFromIndex(
                    self.zones_list_view.currentIndex())
                for building in self.project.list_of_buildings:
                    for zone in building.thermal_zones:
                        if (zone.internal_id == item.internal_id):
                            ind = building.thermal_zones.index(zone)
                            del building.thermal_zones[ind]
                            self.display_current_building()
            except (ValueError, AttributeError):
                QtGui.QMessageBox.warning(self,
                                          u"No zone selected",
                                          u"You need to select a"
                                          "thermal zone first.")

    def delete_current_element(self):
        try:
            item = self.element_model.itemFromIndex(
                self.zone_element_list_view.currentIndex())
            for building in self.project.list_of_buildings:
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

    def delete_selected_layer(self):
        try:
            item = self.element_layer_model.itemFromIndex(
                self.element_material_list_view.currentIndex())
            for building in self.project.list_of_buildings:
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

    def edit_building(self):

        """ Switches to edit-mode, text fields can be used and everything else
        is grayed out """

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

        """ Disables edit-mode while keeping changes """

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

        """ Disables edit-mode while reverting all changes back to before """

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

    def switch_current_zone(self):

        """ Switches the display of the current zone when a new zone is
        selected via the list """

        current_item = self.zone_model.itemFromIndex(
            self.edit_zone_list.currentIndex())
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == current_item.internal_id:
                self.current_zone = zone
        self.display_current_zone()

    def saveChangedZoneValues(self):

        self.current_zone.name = self.zone_id_textbox.text()
        self.current_zone.area = float(
            self.zone_net_leased_area_textbox.text())
        self.current_zone.use_conditions.usage =\
            self.zone_type_groupbox.currentText()
        if self.cooling_ahu_start_dropdown.currentText().startswith('0'):
            self.current_zone.use_conditions.cooling_time[0] = \
                int(self.cooling_ahu_start_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.cooling_time[0] = \
                int(self.cooling_ahu_start_dropdown.currentText()[0] + 
                    self.cooling_ahu_start_dropdown.currentText()[1])
        if self.cooling_ahu_end_dropdown.currentText().startswith('0'):
            self.current_zone.use_conditions.cooling_time[1] = \
                int(self.cooling_ahu_end_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.cooling_time[1] = \
                int(self.cooling_ahu_end_dropdown.currentText()[0] + 
                    self.cooling_ahu_end_dropdown.currentText()[1])
        if self.heating_ahu_start_dropdown.currentText().startswith('0'):
            self.current_zone.use_conditions.heating_time[0] = \
                int(self.heating_ahu_start_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.heating_time[0] = \
                int(self.heating_ahu_start_dropdown.currentText()[0] + 
                    self.heating_ahu_start_dropdown.currentText()[1])
        if self.heating_ahu_end_dropdown.currentText().startswith('0'):
            self.current_zone.use_conditions.heating_time[1] = \
                int(self.heating_ahu_end_dropdown.currentText()[1])
        else:
            self.current_zone.use_conditions.heating_time[1] = \
                int(self.heating_ahu_end_dropdown.currentText()[0] + 
                    self.heating_ahu_end_dropdown.currentText()[1])

        self.current_zone.use_conditions.set_temp_heat = float(
            self.set_temp_heat_line_edit.text())
        self.current_zone.use_conditions.set_temp_cool = float(
            self.set_temp_cool_line_edit.text())
        self.current_zone.use_conditions.temp_set_back = float(
            self.temp_set_back_line_edit.text())
        self.current_zone.use_conditions.min_air_exchange = float(
            self.min_air_flow_line_edit.text())
        self.current_zone.use_conditions.min_ahu = float(
            self.min_ahu_line_edit.text())
        self.current_zone.use_conditions.max_ahu = float(
            self.max_ahu_line_edit.text())
        if self.with_ahu_combobox.currentText() == 'True':
            self.current_zone.use_conditions.with_ahu = True
        else:
            self.current_zone.use_conditions.with_ahu = False
        self.current_zone.use_conditions.rel_humidity = float(
            self.re_humidity_line_edit.text())
        self.current_zone.use_conditions.persons = float(
            self.persons_line_edit.text())
        self.current_zone.use_conditions.machines = float(
            self.machines_line_edit.text())
        self.current_zone.use_conditions.maintained_illuminace = float(
            self.lighting_line_edit.text())
        try:
            self.current_zone.t_inside = utilis.celsius_to_kelvin(float(
                self.mean_temp_inner_line_edit.text()))
        except ValueError:
            print ("Please insert a value for Mean indoor temperature")
        try:
            self.current_zone.t_outside = utilis.celsius_to_kelvin(float(
                self.mean_temp_outer_line_edit.text()))
        except ValueError:
            print ("Please insert a value for Mean outdoor temperature")
        try:
            self.current_zone.infiltration_rate = float(
                self.infiltration_rate_line_edit.text())
        except ValueError:
            print ("Please insert a value for infiltration rate")

        for zone in self.current_building.thermal_zones:
            if zone.internal_id == self.current_zone.internal_id:
                self.current_building.thermal_zones[self.current_building.
                                                    thermal_zones.
                                                    index(zone)] = \
                    self.current_zone

        self.display_current_building()

    def switch_current_element(self):

        """ Switches the display of the current element when a new zone is
        selected via the list """

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

    def switch_current_layer(self):

        current_item = self.layer_model.itemFromIndex(
            self.edit_current_layer_list.currentIndex())
        for layer in self.current_element.layer:
            if layer.internal_id == current_item.internal_id:
                self.current_layer = layer
        self.display_current_layer()

    def load_building_button(self):

        """ Opens a file dialog and issues the controller to load a building
        from the .xml file """

        path = QtGui.QFileDialog.getOpenFileName(
            self, caption='Choose Filepath', directory='', filter=None)
        if path:
            loaded_project = Controller.click_load_button(path)
            self.merge_projects(loaded_project)

    def merge_projects(self, loaded_project):

        """ When loading a complete project from xml it has to be merged
        into the current project """

        for building in self.project.list_of_buildings:
            loaded_project.list_of_buildings.insert(0, building)
        self.project = loaded_project
        self.project.modelica_info = ModelicaInfo()

        self.current_building = self.project.list_of_buildings[-1]
        self.display_current_building()

    def check_new_building_inputs(self):
        self.current_building = Controller.click_add_new_building(
            self.project, "temp")
        self.current_building.name = \
            self.generate_new_building_id_line_edit.text()
        self.project.list_of_buildings.append(self.current_building)
        self.display_current_building()

    def check_new_element_inputs(self):
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
            if type(inner_wall).__name__ == \
                    "InnerWall":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                    "\nType:\t".expandtabs(11) + 
                    "Inner Wall \n Area:\t".expandtabs(11) + 
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
            if type(inner_wall).__name__ == \
                    "Floor":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                    "\nType:\t".expandtabs(11) + 
                    "Floor \n Area:\t".expandtabs(11) + 
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
            if type(inner_wall).__name__ == \
                    "Ceiling":
                item = TrackableItem(
                    "Name:\t".expandtabs(8) + str(inner_wall.name) + 
                    "\nType:\t".expandtabs(11) + 
                    "Ceiling \n Area:\t".expandtabs(11) + 
                    str(inner_wall.area), inner_wall.internal_id)
                self.element_model.appendRow(item)
        for element in self.current_zone.outer_walls:
            if type(element).__name__ == \
                    "GroundFloor":
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
            if type(element).__name__ == \
                    "Rooftop":
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
            if type(element).__name__ == \
                    "OuterWall":
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

    def keyPressEvent(self, event):
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

    def check_new_layer_inputs(self):

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
        self.current_element = Controller.click_add_new_layer(
            self.current_element,
            int(self.new_layer_position_combobox.currentText()),
            thick, self.new_layer_material_combobox.currentText(), dens,
            therm, heat, solar, ir, trans)

    def create_new_project(self):
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
        QtGui.QMessageBox.warning(
            self, u"Warning", u"When creating a new project,"
            "all Values in Teaser will be removed.")
        self.create_new_project_ui_page = QtGui.QWizardPage()
        self.create_new_project_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.create_new_project_ui_page.setWindowTitle("Create new Zone")
        self.create_new_project_ui_page.setFixedWidth(350)
        self.create_new_project_ui_page.setFixedHeight(200)
        self.create_new_project_window_layout = QtGui.QGridLayout()
        self.create_new_project_ui_page.setLayout(
            self.create_new_project_window_layout)
        self.create_new_project_save_button = QtGui.QPushButton()
        self.create_new_project_save_button.setText("Save")
        self.connect(self.create_new_project_save_button,
                     SIGNAL("clicked()"), self.create_new_project)
        self.connect(self.create_new_project_save_button,
                     SIGNAL("clicked()"), self.create_new_project_ui_page,
                     QtCore.SLOT("close()"))
        self.create_new_project_cancel_button = QtGui.QPushButton()
        self.create_new_project_cancel_button.setText("Cancel")
        self.connect(self.create_new_project_cancel_button,
                     SIGNAL("clicked()"), self.create_new_project_ui_page,
                     QtCore.SLOT("close()"))
        self.create_new_project_window_layout.addWidget(
            self.create_new_project_save_button, 2, 0)
        self.create_new_project_window_layout.addWidget(
            self.create_new_project_cancel_button, 2, 1)
        self.create_new_project_ui_page.setWindowModality(Qt.ApplicationModal)
        self.create_new_project_ui_page.show()

    def create_new_building_ui(self):
        self.generate_new_building_ui_page = QtGui.QWizardPage()
        self.generate_new_building_ui_page.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.generate_new_building_ui_page.setWindowTitle(
            "Create new Building")
        self.generate_new_building_ui_page.setFixedWidth(350)
        self.generate_new_building_ui_page.setFixedHeight(200)
        self.generate_new_building_window_layout = QtGui.QGridLayout()
        self.generate_new_building_ui_page.setLayout(
            self.generate_new_building_window_layout)

        self.no_building_warning_label = QtGui.QLabel(
            "You need to specify a building first")

        self.generate_new_building_id_label = QtGui.QLabel("Id: ")
        self.generate_new_building_id_line_edit = QtGui.QLineEdit()
        self.generate_new_building_id_line_edit.setObjectName(
            "generate_new_building_id_line_edit")

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
            self.no_building_warning_label, 0, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_id_label, 1, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_id_line_edit, 1, 1)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_save_button, 2, 0)
        self.generate_new_building_window_layout.addWidget(
            self.generate_new_building_cancel_button, 2, 1)
        self.generate_new_building_ui_page.setWindowModality(
            Qt.ApplicationModal)
        self.generate_new_building_ui_page.show()

    def create_new_element_ui(self):

        self.create_new_element_ui_page = QtGui.QWizardPage()
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

    def create_new_layer_ui(self):
        self.create_layer_ui = QtGui.QWizardPage()
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
        num_layers = len(self.current_element.layer) + 1
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

        self.new_layer_material_label = QtGui.QLabel("Material")
        self.new_layer_material_combobox = QtGui.QComboBox()
        temp_list = []
        for material in self.materials:
            if material.name not in temp_list:
                temp_list.append(material.name)
        self.new_layer_material_combobox.addItems(sorted(temp_list))
        self.is_switchable = True

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

        self.new_layer_save_button = QtGui.QPushButton()
        self.new_layer_save_button.setText("Save")
        self.connect(self.new_layer_save_button, SIGNAL(
            "clicked()"), self.check_new_layer_inputs)
        self.connect(self.new_layer_save_button, SIGNAL(
            "clicked()"), self.update_element_details)
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

    def show_layer_build_ui(self, item):
        self.layer_build_ui = QtGui.QWizardPage()
        self.layer_build_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.layer_build_ui.setWindowTitle("Layer Details")
        self.layer_build_ui.setFixedWidth(450)
        self.layer_build_ui.setFixedHeight(300)
        self.layer_build_ui_window_layout = QtGui.QGridLayout()
        self.layer_build_ui.setLayout(self.layer_build_ui_window_layout)
        self.layer_model = QtGui.QStandardItemModel()
        self.materials = Controller.get_materials_from_file(self.project)
        self.is_switchable = False

        current_item = self.element_layer_model.itemFromIndex(item)
        for layer in self.current_element.layer:
            if (layer.internal_id == current_item.internal_id):
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
        self.connect(self.layer_save_button, SIGNAL(
            "clicked()"), self.save_changed_layer_values)
        self.connect(self.layer_save_button, SIGNAL(
            "clicked()"), self.update_element_details)
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

    def change_zone_values_ui(self, item):
        self.zone_element_model = QStandardItemModel()
        current_item = self.zone_model.itemFromIndex(item)
        for zone in self.current_building.thermal_zones:
            if zone.internal_id == current_item.internal_id:
                self.current_zone = zone
                self.display_current_zone()

        self.zone_value_window = QtGui.QWizardPage()
        self.zone_value_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
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
        self.zone_type_groupbox = QtGui.QComboBox()
        self.zone_type_groupbox.setObjectName(_fromUtf8("ZoneTypeGroupBox"))
        for thermal_zone_type in self.guiinfo.thermal_zone_types:
            self.zone_type_groupbox.addItem(thermal_zone_type, userData=None)
        self.zone_type_groupbox.setCurrentIndex(
            self.zone_type_groupbox.findText(
                str(self.current_zone.use_conditions.usage)))

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
            self.zone_type_groupbox, 1, 1)
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
            "clicked()"), self.saveChangedZoneValues)
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
        self.set_temp_heat_label_2 = QtGui.QLabel("\u00B0C")

        self.set_temp_cool_label_1 = QtGui.QLabel("Set Temp Cooling: ")
        self.set_temp_cool_line_edit = QtGui.QLineEdit()
        self.set_temp_cool_line_edit.setText(str(
            self.current_zone.use_conditions.set_temp_cool))
        self.set_temp_cool_label_2 = QtGui.QLabel("\u00B0C")

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

        self.usagePicPixMap = QtGui.QPixmap("GUI\\sheep_PNG2186.png")
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
        self.mean_temp_outer_line_edit.setText(str(utilis.kelvin_to_celsius(
            self.current_zone.t_outside)))
        self.mean_temp_out_label_2 = QtGui.QLabel("\u00B0C")
        
        self.mean_temp_in_label_1 = QtGui.QLabel("Mean Indoor Temp: ")
        self.mean_temp_inner_line_edit = QtGui.QLineEdit()
        self.mean_temp_inner_line_edit.setText(str(utilis.kelvin_to_celsius(
            self.current_zone.t_inside)))
        self.mean_temp_in_label_2 = QtGui.QLabel("\u00B0C")
        
        self.infiltration_rate_label_1 = QtGui.QLabel("Infiltration Rate: ")
        self.infiltration_rate_line_edit = QtGui.QLineEdit()
        if self.current_zone.infiltration_rate is not None:
            self.infiltration_rate_line_edit.setText(str(
                self.current_zone.infiltration_rate))
        else:
            self.infiltration_rate_line_edit.setText("1")
        self.infiltration_rate_label_2 = QtGui.QLabel("1/h")
        
        self.space_label = QtGui.QLabel() # Cheat to group the other controls on top

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
        self.zone_usage_layout.addWidget(self.usage_pic_label, 2, 1)
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

    def generate_type_building_ui(self, building_type):

        self.popup_window_type_building = QtGui.QWizardPage()
        self.popup_window_type_building.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.popup_window_type_building.setAttribute(
            QtCore.Qt.WA_DeleteOnClose)
        self.popup_window_type_building.setWindowTitle(
            u"generate " + building_type + " ...")
        self.popup_window_type_building.setFixedWidth(500)
        self.popup_window_type_building.setFixedHeight(700)
        self.popup_layout_type_building = QtGui.QGridLayout()
        self.popup_window_type_building.setLayout(
            self.popup_layout_type_building)
        self.group_box_type_building_sidecontrols = QtGui.QGroupBox(
            u"General Information")

        self.window_construct_building_type_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_type_label.setGeometry(
            QtCore.QRect(10, 25, 90, 25))
        self.window_construct_building_type_label.setText("Example Building:")
        self.window_construct_building_combo_box = QtGui.QComboBox(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_combo_box.setGeometry(
            QtCore.QRect(110, 25, 120, 25))
        for type_building in self.guiinfo.type_buildings:
            self.window_construct_building_combo_box.addItem(type_building)
        self.window_construct_building_name_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_name_label.setGeometry(
            QtCore.QRect(10, 105, 90, 25))
        self.window_construct_building_name_label.setText("Name:")
        self.window_construct_building_name_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_name_line_edit.setGeometry(
            QtCore.QRect(110, 105, 120, 25))
        self.window_construct_building_street_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_street_label.setGeometry(
            QtCore.QRect(10, 185, 90, 25))
        self.window_construct_building_street_label.setText("Street/Nr.:")
        self.window_construct_building_street_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_street_line_edit.setGeometry(
            QtCore.QRect(110, 185, 120, 25))
        self.window_construct_building_location_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_location_label.setGeometry(
            QtCore.QRect(10, 265, 90, 25))
        self.window_construct_building_location_label.setText("ZIP/City:")
        self.window_construct_building_location_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_location_line_edit.setGeometry(
            QtCore.QRect(110, 265, 120, 25))
        self.window_construct_building_year_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_year_label.setGeometry(
            QtCore.QRect(10, 345, 90, 25))
        self.window_construct_building_year_label.setText("Construction Year:")
        self.window_construct_building_year_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_year_line_edit.setGeometry(
            QtCore.QRect(110, 345, 120, 25))
        self.window_construct_building_number_of_floors_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_number_of_floors_label.setGeometry(
            QtCore.QRect(10, 425, 90, 25))
        self.window_construct_building_number_of_floors_label.setText(
            "Number of Floors:")
        self.window_construct_building_number_of_floors_line_edit = \
            QtGui.QLineEdit(self.group_box_type_building_sidecontrols)
        self.window_construct_building_number_of_floors_line_edit.setGeometry(
            QtCore.QRect(110, 425, 120, 25))
        self.window_construct_building_height_of_floors_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_height_of_floors_label.setGeometry(
            QtCore.QRect(10, 505, 90, 25))
        self.window_construct_building_height_of_floors_label.setText(
            "Height of Floors:")
        self.window_construct_building_height_of_floors_line_edit = \
            QtGui.QLineEdit(self.group_box_type_building_sidecontrols)
        self.window_construct_building_height_of_floors_line_edit.setGeometry(
            QtCore.QRect(110, 505, 120, 25))
        self.window_construct_building_area_label = QtGui.QLabel(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_area_label.setGeometry(
            QtCore.QRect(10, 585, 90, 25))
        self.window_construct_building_area_label.setText("Net leased Area:")
        self.window_construct_building_area_line_edit = QtGui.QLineEdit(
            self.group_box_type_building_sidecontrols)
        self.window_construct_building_area_line_edit.setGeometry(
            QtCore.QRect(110, 585, 120, 25))

        # Differentiates between the different types of buildings from combobox
        if building_type == "Office":

            self.group_box_office_layout = QtGui.QGroupBox(u"Layout")
            self.group_box_office_window_area = QtGui.QGroupBox(u"Window area")
            self.group_box_office_architecture = QtGui.QGroupBox(
                u"Architecture")

            self.office_layout = QtGui.QGridLayout()
            self.office_layoutWindowArea = QtGui.QGridLayout()
            self.office_layout_architecture = QtGui.QGridLayout()

            self.group_box_office_layout.setLayout(self.office_layout)
            self.group_box_office_window_area.setLayout(
                self.office_layoutWindowArea)
            self.group_box_office_architecture.setLayout(
                self.office_layout_architecture)

            self.radio_button_office_layout_1 = QtGui.QRadioButton(
                u"Use basic values")
            self.radio_button_office_layout_2 = QtGui.QRadioButton(
                u"elongated, 1 floor")
            self.radio_button_office_layout_3 = QtGui.QRadioButton(
                u"elongated, 2 floors")
            self.radio_button_office_layout_4 = QtGui.QRadioButton(
                u"compact")
            self.radio_button_office_layout_1.setChecked(True)

            self.picture_layout_office_2 = QtGui.QLabel()
            self.picture_layout_office_3 = QtGui.QLabel()
            self.picture_layout_office_4 = QtGui.QLabel()
            self.picture_layout_office_2.setPixmap(
                QtGui.QPixmap(utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Zweibund.png")).scaled(
                        70, 70))
            self.picture_layout_office_3.setPixmap(
                QtGui.QPixmap(utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Dreibund.png")).scaled(
                        70, 70))
            self.picture_layout_office_4.setPixmap(QtGui.QPixmap(
                utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Kompakt.png")).scaled(
                        70, 70))
            self.office_layout.addWidget(
                self.radio_button_office_layout_1, 1, 0)
            self.office_layout.addWidget(
                self.radio_button_office_layout_2, 2, 0)
            self.office_layout.addWidget(
                self.radio_button_office_layout_3, 3, 0)
            self.office_layout.addWidget(
                self.radio_button_office_layout_4, 4, 0)
            self.office_layout.addWidget(
                self.picture_layout_office_2, 2, 1, Qt.AlignRight)
            self.office_layout.addWidget(
                self.picture_layout_office_3, 3, 1, Qt.AlignRight)
            self.office_layout.addWidget(
                self.picture_layout_office_4, 4, 1, Qt.AlignRight)

            self.radio_button_window_area_office_1 = QtGui.QRadioButton(
                u"average window area")
            self.radio_button_window_area_office_2 = QtGui.QRadioButton(
                u"Lochfassade")
            self.radio_button_window_area_office_3 = QtGui.QRadioButton(
                u"Bandfassade")
            self.radio_button_window_area_office_4 = QtGui.QRadioButton(
                u"Vollverglasung")
            self.radio_button_window_area_office_1.setChecked(True)

            self.picture_window_area_office_2 = QtGui.QLabel()
            self.picture_window_area_office_3 = QtGui.QLabel()
            self.picture_window_area_office_4 = QtGui.QLabel()
            self.picture_window_area_office_2.setPixmap(QtGui.QPixmap(
                utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Lochfassade.png"))
                .scaled(70, 70))
            self.picture_window_area_office_3.setPixmap(QtGui.QPixmap(
                utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Bandfassade.png"))
                .scaled(70, 70))
            self.picture_window_area_office_4.setPixmap(QtGui.QPixmap(
                utilis.get_full_path(
                    "GUI\\GUIImages\\OfficeBuildings\\Vollverglasung.png"))
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
                u"Standartwert nutzen")
            self.radio_button_architecture_office_2 = QtGui.QRadioButton(
                u"massiv")
            self.radio_button_architecture_office_3 = QtGui.QRadioButton(
                u"leicht")
            self.radio_button_architecture_office_1.setChecked(True)

            self.office_layout_architecture.addWidget(
                self.radio_button_architecture_office_1, 1, 0)
            self.office_layout_architecture.addWidget(
                self.radio_button_architecture_office_2, 2, 0)
            self.office_layout_architecture.addWidget(
                self.radio_button_architecture_office_3, 3, 0)
            # self.office_layout_architecture.addWidget(
            #     self.radio_button_architecture_office_4, 4, 0)

            self.construct_office_button = QtGui.QPushButton(
                u"Generate " + building_type + " Building ...")
            self.connect(self.construct_office_button, SIGNAL(
                "clicked()"), self.check_inputs_typebuilding_office)
            self.connect(self.construct_office_button, SIGNAL(
                "clicked()"), self.popup_window_type_building,
                QtCore.SLOT("close()"))
            self.popup_layout_type_building.addWidget(
                self.group_box_type_building_sidecontrols, 0, 0, 7, 2)
            self.popup_layout_type_building.addWidget(
                self.group_box_office_layout, 0, 2, 1, 1)
            self.popup_layout_type_building.addWidget(
                self.group_box_office_window_area, 3, 2, 1, 1)
            self.popup_layout_type_building.addWidget(
                self.group_box_office_architecture, 6, 2, 1, 1)
            self.popup_layout_type_building.addWidget(
                self.construct_office_button, 7, 0, 1, 3)
            self.popup_window_type_building.setLayout(
                self.popup_layout_type_building)

        elif building_type == "Residential":

            self.group_box_residential_neighbour_buildings = QtGui.QGroupBox(
                u"Direct neighbour buildings")
            self.group_box_residential_layout = QtGui.QGroupBox(u"Layout")
            self.group_box_residential_roof = QtGui.QGroupBox(u"Roof")
            self.group_box_residential_basement = QtGui.QGroupBox(u"Basement")
            self.group_box_residential_architecture = QtGui.QGroupBox(
                u"Architecture")

            self.layout_residential_neighbour_buildings = QtGui.QGridLayout()
            self.layout_residential_layout = QtGui.QGridLayout()
            self.layout_residential_layout = QtGui.QGridLayout()
            self.layout_residential_basement = QtGui.QGridLayout()
            self.layout_residential_architecture = QtGui.QGridLayout()

            self.group_box_residential_neighbour_buildings.setLayout(
                self.layout_residential_neighbour_buildings)
            self.group_box_residential_layout.setLayout(
                self.layout_residential_layout)
            self.group_box_residential_roof.setLayout(
                self.layout_residential_layout)
            self.group_box_residential_basement.setLayout(
                self.layout_residential_basement)
            self.group_box_residential_architecture.setLayout(
                self.layout_residential_architecture)

            self.radio_button_neighbour_1 = QtGui.QRadioButton(
                u"none (freestanding)")
            self.radio_button_neighbour_2 = QtGui.QRadioButton(
                u"annex to one side")
            self.radio_button_neighbour_3 = QtGui.QRadioButton(
                u"annex to both sides")
            self.radio_button_neighbour_1.setChecked(True)

            self.picture_neighbour_building_residential_1 = QtGui.QLabel()
            self.picture_neighbour_building_residential_2 = QtGui.QLabel()
            self.picture_neighbour_building_residential_3 = QtGui.QLabel()
            self.picture_neighbour_building_residential_1.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\\
                    freistehend.png")).scaled(29, 23))
            self.picture_neighbour_building_residential_2.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\\
                    einseitigangebaut.png")).scaled(46, 23))
            self.picture_neighbour_building_residential_3.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\\
                    beidseitigangebaut.png")).scaled(56, 23))
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
                u"kompakt")
            self.radio_button_residential_layout_2 = QtGui.QRadioButton(
                u"langgestreckt/ komplex")
            self.radio_button_residential_layout_1.setChecked(True)

            self.picture_layout_residential_1 = QtGui.QLabel()
            self.picture_layout_residential_2 = QtGui.QLabel()
            self.picture_layout_residential_1.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "kompakt.png")).scaled(28, 28))
            self.picture_layout_residential_2.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "laenglich.png")).scaled(28, 28))
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_layout_1, 1, 0)
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_layout_2, 2, 0)
            self.layout_residential_layout.addWidget(
                self.picture_layout_residential_1, 1, 1, Qt.AlignRight)
            self.layout_residential_layout.addWidget(
                self.picture_layout_residential_2, 2, 1, Qt.AlignRight)

            self.radio_button_residential_roof_1 = QtGui.QRadioButton(
                u"Flachdach")
            self.radio_button_residential_roof_2 = QtGui.QRadioButton(
                u"unbeheiztes Dachgeschoss")
            self.radio_button_residential_roof_3 = QtGui.QRadioButton(
                u"teilweise beheiztes Dachgeschoss")
            self.radio_button_residential_roof_4 = QtGui.QRadioButton(
                u"beheiztes Dachgeschoss")
            self.radio_button_residential_roof_1.setChecked(True)

            self.h_line_roof = QtGui.QFrame()
            self.h_line_roof.setFrameShape(QtGui.QFrame.HLine)
            self.h_line_roof.setFrameShadow(QtGui.QFrame.Sunken)
            self.check_box_button_roof = QtGui.QCheckBox(
                u"Dachgauben oder andere Dachaufbauten vorhanden")
            self.picture_roof_residential_1 = QtGui.QLabel()
            self.picture_roof_residential_2 = QtGui.QLabel()
            self.picture_roof_residential_3 = QtGui.QLabel()
            self.picture_roof_residential_4 = QtGui.QLabel()
            self.picture_roof_residential_1.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Flachdach.png")).scaled(32, 23))
            self.picture_roof_residential_2.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Satteldachunbeheizt.png")).
                scaled(34, 23))
            self.picture_roof_residential_3.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Satteldachteilweisebeheizt.png")).
                scaled(34, 23))
            self.picture_roof_residential_4.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Satteldachbeheizt.png")).scaled(34, 23))
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_roof_1, 1, 0)
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_roof_2, 2, 0)
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_roof_3, 3, 0)
            self.layout_residential_layout.addWidget(
                self.radio_button_residential_roof_4, 4, 0)
            self.layout_residential_layout.addWidget(
                self.picture_roof_residential_1, 1, 1, Qt.AlignRight)
            self.layout_residential_layout.addWidget(
                self.picture_roof_residential_2, 2, 1, Qt.AlignRight)
            self.layout_residential_layout.addWidget(
                self.picture_roof_residential_3, 3, 1, Qt.AlignRight)
            self.layout_residential_layout.addWidget(
                self.picture_roof_residential_4, 4, 1, Qt.AlignRight)
            self.layout_residential_layout.addWidget(
                self.h_line_roof, 5, 0, 1, 0)
            self.layout_residential_layout.addWidget(
                self.check_box_button_roof, 6, 0, 1, 1)

            self.radio_button_residential_basement_1 = QtGui.QRadioButton(
                u"nicht unterkellert")
            self.radio_button_residential_basement_2 = QtGui.QRadioButton(
                u"unbeheizter Keller")
            self.radio_button_residential_basement_3 = QtGui.QRadioButton(
                u"teilweise unbeheizter Keller")
            self.radio_button_residential_basement_4 = QtGui.QRadioButton(
                u"beheizter Keller")
            self.radio_button_residential_basement_1.setChecked(True)

            self.picture_residential_basement_1 = QtGui.QLabel()
            self.picture_residential_basement_2 = QtGui.QLabel()
            self.picture_residential_basement_3 = QtGui.QLabel()
            self.picture_residential_basement_4 = QtGui.QLabel()
            self.picture_residential_basement_1.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "keinKeller.png")).scaled(32, 28))
            self.picture_residential_basement_2.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Kellerunbeheizt.png")).scaled(32, 28))
            self.picture_residential_basement_3.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Kellerteilweisebeheizt.png")).
                scaled(32, 28))
            self.picture_residential_basement_4.setPixmap(QPixmap(
                utilis.get_full_path("GUI\\GUIImages\\Wohngebaeude\\"
                                     "Kellerbeheizt.png")).scaled(32, 28))
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
                u"Standardwert nutzen")
            self.radio_button_residential_architecture_2 = QtGui.QRadioButton(
                u"massiv")
            self.radio_button_residential_architecture_3 = QtGui.QRadioButton(
                u"leicht")
            self.radio_button_residential_architecture_1.setChecked(True)

            self.layout_residential_architecture.addWidget(
                self.radio_button_residential_architecture_1, 1, 0)
            self.layout_residential_architecture.addWidget(
                self.radio_button_residential_architecture_2, 2, 0)
            self.layout_residential_architecture.addWidget(
                self.radio_button_residential_architecture_3, 3, 0)

            self.construct_residential_button = QtGui.QPushButton(
                u"Generate " + building_type + " Building ...")
            self.connect(self.construct_residential_button, SIGNAL(
                "clicked()"), self.check_inputs_typebuilding_residential)
            self.connect(self.construct_residential_button, SIGNAL(
                "clicked()"), self.updateBuildingList)
            self.connect(self.construct_residential_button, SIGNAL(
                "clicked()"), self.popup_window_type_building, QtCore.SLOT(
                "close()"))
            self.popup_layout_type_building.addWidget(
                self.group_box_residential_neighbour_buildings, 2, 0, 1, 0)
            self.popup_layout_type_building.addWidget(
                self.group_box_residential_layout, 3, 0, 1, 0)
            self.popup_layout_type_building.addWidget(
                self.group_box_residential_roof, 4, 0, 1, 0)
            self.popup_layout_type_building.addWidget(
                self.group_box_residential_basement, 5, 0, 1, 0)
            self.popup_layout_type_building.addWidget(
                self.group_box_residential_architecture, 6, 0, 1, 0)
            self.popup_layout_type_building.addWidget(
                self.construct_residential_button, 7, 0, 1, 0)
            self.popup_window_type_building.setLayout(
                self.popup_layout_type_building)
        self.popup_window_type_building.setWindowModality(Qt.ApplicationModal)
        self.popup_window_type_building.show()

    def generate_zone_ui(self):
        self.generate_zone_ui_page = QtGui.QWizardPage()
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

    def show_element_build_ui(self, item):
        self.element_build_ui = QtGui.QWizardPage()
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
        if "Outer Wall" in current_item.text():
            for element in self.current_zone.outer_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Ground Floor" in current_item.text():
            for element in self.current_zone.outer_walls:
                if element.internal_id == current_item.internal_id:
                    self.current_element = element
        if "Roof Top" in current_item.text():
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

        self.element_orientation_label = QtGui.QLabel("Orientation")
        self.element_orientation_combobox = QtGui.QComboBox()
        self.element_orientation_combobox.setObjectName(
            _fromUtf8("ElementOrientationComboBox"))
        for orientation in self.guiinfo.orientations:
            self.element_orientation_combobox.addItem(
                orientation, userData=None)
        self.element_orientation_combobox.setCurrentIndex(
            self.element_orientation_combobox.findText(
                str(self.current_element.orientation)))

        self.element_name_label = QtGui.QLabel("Id")
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

        self.element_uvalue_label = QtGui.QLabel("U-Value (U/A)")
        self.element_uvalue_textbox = QtGui.QLineEdit()
        self.element_uvalue_textbox.setObjectName(
            _fromUtf8("ElementUValueTextBox"))
        self.element_uvalue_textbox.setText(str(self.current_element.ua_value))
        self.element_uvalue_textbox.setReadOnly(True)

        self.element_add_material_button = QtGui.QPushButton()
        self.element_add_material_button.setText("Add Layer")
        self.connect(self.element_add_material_button, SIGNAL("clicked()"),
                     self.create_new_layer_ui)

        self.element_delete_material_button = QtGui.QPushButton()
        self.element_delete_material_button.setText("Delete Layer")
        self.connect(self.element_delete_material_button, SIGNAL("clicked()"),
                     self.delete_selected_layer)

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
        
    def show_export_window(self):
        self.export_window_ui = QtGui.QWizardPage()
        self.export_window_ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.export_window_ui.setWindowTitle("Simulation")
        self.export_window_ui.setFixedWidth(380)
        self.export_window_ui.setFixedHeight(180)
        self.export_window_ui_layout = QtGui.QGridLayout()
        self.export_window_ui.setLayout(self.export_window_ui_layout)
        
        self.export_groupbox = QtGui.QGroupBox("Export")
        self.export_groupbox.setGeometry(QtCore.QRect(5, 5, 360, 160))
        self.export_groupbox.setMinimumSize(QtCore.QSize(360, 160))
        self.export_groupbox.setMaximumSize(QtCore.QSize(360, 160))
        self.export_groupbox.setObjectName(_fromUtf8("exportGroupBox"))
        self.export_button = QtGui.QPushButton(self.export_groupbox)
        self.export_button.setGeometry(QtCore.QRect(5, 20, 305, 25))
        self.export_button.clicked.connect(self.click_export_button)
        self.export_button.setText("Export template for all buildings")
        self.export_button_one = QtGui.QPushButton(self.export_groupbox)
        self.export_button_one.setGeometry(QtCore.QRect(5, 55, 305, 25))
        # self.export_button_one.clicked.connect(self.export_groupbox)
        self.export_button_one.setText("Export template for current building")
        self.export_template_label = QtGui.QLabel(self.export_groupbox)
        self.export_template_label.setGeometry(QtCore.QRect(5, 90, 120, 25))
        self.export_template_label.setText("Export template:")
        self.export_create_template_combobox = QtGui.QComboBox(
            self.export_groupbox)
        self.export_create_template_combobox.setGeometry(
            QtCore.QRect(130, 90, 215, 25))
        self.export_save_template_label = QtGui.QLabel(self.export_groupbox)
        self.export_save_template_label.setGeometry(
            QtCore.QRect(5, 125, 110, 25))
        self.export_save_template_label.setText("Export save template:")
        self.export_save_template_lineedit = QtGui.QLineEdit(
            self.export_groupbox)
        self.export_save_template_lineedit .setGeometry(
            QtCore.QRect(130, 125, 130, 25))
        self.export_save_template_button = QtGui.QPushButton(
            self.export_groupbox)
        self.export_save_template_button.setGeometry(
            QtCore.QRect(265, 125, 80, 25))
        self.export_save_template_button.setText("Browse")
        # self.export_save_template_button.clicked.connect(
        #    self.clickBrowseButton)
        for template_name in os.listdir(self.create_path_to_template_folder()):
            self.export_create_template_combobox.addItem(template_name)
        
        self.export_window_ui_layout.addWidget(
            self.export_groupbox, 1, 1)
        self.export_window_ui.setWindowModality(Qt.ApplicationModal)
        self.export_window_ui.show()

    def show_simulation_window(self):
        self.simulation_window_ui = QtGui.QWizardPage()
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
        self.project_name_lineedit = QtGui.QLineEdit(self.project_name_groupbox)
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
        self.connect(self.simulation_save_button, SIGNAL(
                "clicked()"), self.simulation_window_ui, QtCore.SLOT(
                "close()"))
        self.simulation_cancel_button = QtGui.QPushButton(
            self.simulation_save_cancel_groupbox)
        self.simulation_cancel_button.setText("Cancel")
        self.simulation_cancel_button.setGeometry(QtCore.QRect(100, 5, 80, 25))
        self.connect(self.simulation_cancel_button, SIGNAL(
                "clicked()"), self.simulation_window_ui, QtCore.SLOT(
                "close()"))

        self.simulation_window_ui_layout.addWidget(
            self.project_name_groupbox, 1, 1)
        self.simulation_window_ui_layout.addWidget(
            self.simulation_groupbox, 2, 1)
        self.simulation_window_ui_layout.addWidget(
            self.simulation_save_cancel_groupbox, 3, 1)
        self.simulation_window_ui.setWindowModality(Qt.ApplicationModal)
        self.simulation_window_ui.show()


class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass
