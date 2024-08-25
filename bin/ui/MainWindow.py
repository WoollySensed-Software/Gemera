from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, 
    QRadioButton, QButtonGroup, QLineEdit, 
    QHBoxLayout, QVBoxLayout, QSpacerItem, 
    QSizePolicy, QSizeGrip
)
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtCore import Qt, QSize, QPoint

from settings import __app_name__, CFG_PATH, INCLUDES, middle_path
from bin.ui.styles import MAIN_WINDOW
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.handlers.Graph import GraphH
from bin.ui.SettingsWindow import SettingsWindowUI
from bin.ui.WeighersWindow import WeighersWindowUI


class MainWindowUI(QWidget):

    def __init__(self):
        super().__init__()
        self.old_pos = None
        self.full_screen_flag = False
        self.default_font = QFont('Sans Serif', 16)
        self.spec_font = QFont('Sans Serif', 14)
        self.cfg_handler = ConfigurationFileH(CFG_PATH)
        self.default_width = self.cfg_handler.get('app')['display_w']
        self.default_height = self.cfg_handler.get('app')['display_h']
    
    def setup_ui(self):
        # --- настройки окна ---
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setMinimumHeight(740)
        self.resize(self.default_width, self.default_height)
        self.setStyleSheet(MAIN_WINDOW)
        self.setObjectName('MainWindowUI')

        """TopBarWidget"""
        # --- верхняя панель ---
        self.widget_top_bar_frame = QWidget()
        self.widget_top_bar_frame.setFixedHeight(30)
        self.widget_top_bar_frame.setObjectName('widget_top_bar_frame')

        # --- изменение размера окна ---
        self.top_left_size_grip = QSizeGrip(self.widget_top_bar_frame)
        self.top_left_size_grip.setFixedSize(QSize(30, 30))

        # --- название окна ---
        self.lbl_tb_title = QLabel()
        self.lbl_tb_title.setFont(self.spec_font)
        self.lbl_tb_title.setText(__app_name__)
        self.lbl_tb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_tb_title.setFixedWidth(200)
        self.lbl_tb_title.setObjectName('lbl_tb_title')
        
        # --- кнопка настроек ---
        self.btn_tb_settings = QPushButton()
        # self.btn_tb_settings.setFont(self.spec_font)
        # self.btn_tb_settings.setText('⚒')  # TODO: использовать иконку
        # self.btn_tb_settings.setIcon(QIcon('bin/resources/gear.png'))
        self.btn_tb_settings.setIcon(QIcon(INCLUDES['gear.png'][2]))
        self.btn_tb_settings.setIconSize(QSize(20, 20))
        self.btn_tb_settings.setFixedSize(QSize(30, 30))
        self.btn_tb_settings.setObjectName('top_bar_buttons')
        self.btn_tb_settings.clicked.connect(self._show_settings)

        # --- кнопка минимизации ---
        self.btn_tb_minimize = QPushButton()
        # self.btn_tb_minimize.setFont(self.spec_font)
        # self.btn_tb_minimize.setText('▬')  # TODO: использовать иконку
        # self.btn_tb_minimize.setIcon(QIcon('bin/resources/minus.png'))
        self.btn_tb_minimize.setIcon(QIcon(INCLUDES['minus.png'][2]))
        self.btn_tb_minimize.setIconSize(QSize(20, 20))
        self.btn_tb_minimize.setFixedSize(QSize(30, 30))
        self.btn_tb_minimize.setObjectName('top_bar_buttons')
        self.btn_tb_minimize.clicked.connect(self.showMinimized)

        # --- кнопка полного экрана ---
        self.btn_tb_full_screen = QPushButton()
        # self.btn_tb_full_screen.setFont(self.spec_font)
        # self.btn_tb_full_screen.setText('[]')
        # self.btn_tb_full_screen.setIcon(QIcon('bin/resources/fullscreen.png'))
        self.btn_tb_full_screen.setIcon(QIcon(INCLUDES['fullscreen.png'][2]))
        self.btn_tb_full_screen.setIconSize(QSize(20, 20))
        self.btn_tb_full_screen.setFixedSize(QSize(30, 30))
        self.btn_tb_full_screen.setObjectName('top_bar_buttons')
        self.btn_tb_full_screen.clicked.connect(self._full_screen)

        # --- кнопка выхода ---
        self.btn_tb_exit = QPushButton(self.widget_top_bar_frame)
        # self.btn_tb_exit.setFont(self.spec_font)
        # self.btn_tb_exit.setText('✖')  # TODO: использовать иконку
        # self.btn_tb_exit.setIcon(QIcon('bin/resources/close.png'))
        self.btn_tb_exit.setIcon(QIcon(INCLUDES['close.png'][2]))
        self.btn_tb_exit.setIconSize(QSize(15, 15))
        self.btn_tb_exit.setFixedSize(QSize(30, 30))
        self.btn_tb_exit.setObjectName('top_bar_buttons')
        self.btn_tb_exit.clicked.connect(self._exit)

        # --- горизонтальный layout для верхней панели ---
        self.top_bar_hlayout = QHBoxLayout(self.widget_top_bar_frame)
        self.top_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_hlayout.setSpacing(0)
        
        # --- горизонтальный layout для верхней панели: зависимости ---
        self.top_bar_hlayout.addWidget(self.top_left_size_grip)
        self.top_bar_hlayout.addWidget(self.lbl_tb_title)
        self.top_bar_hlayout.addSpacerItem(QSpacerItem(50, 30, 
                                                       QSizePolicy.Policy.Expanding, 
                                                       QSizePolicy.Policy.Minimum))
        self.top_bar_hlayout.addWidget(self.btn_tb_settings)
        self.top_bar_hlayout.addWidget(self.btn_tb_minimize)
        self.top_bar_hlayout.addWidget(self.btn_tb_full_screen)
        self.top_bar_hlayout.addWidget(self.btn_tb_exit)
        """/TopBarWidget"""

        """CentralAreaWidget"""
        # --- основная обаласть ---
        self.widget_central_area = QWidget()
        self.widget_central_area.setObjectName('widget_central_area')

        """область режимов ванны"""
        # --- область режимов ванны ---
        self.widget_modes_frame = QWidget()
        self.widget_modes_frame.setMinimumWidth(350)
        self.widget_modes_frame.setObjectName('widget_modes_frame')

        # --- область режимов ванны: название ---
        self.lbl_modes_title = QLabel()
        self.lbl_modes_title.setFont(self.default_font)
        self.lbl_modes_title.setText('Режимы ванны')
        self.lbl_modes_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_modes_title.setMaximumHeight(50)
        self.lbl_modes_title.setMinimumSize(QSize(350, 50))
        self.lbl_modes_title.setObjectName('lbl_modes_title')

        # --- режим ванны: очистка ---
        self.rb_mode_1 = QRadioButton()
        self.rb_mode_1.setFont(self.default_font)
        self.rb_mode_1.setText('Очистка')
        self.rb_mode_1.setObjectName('rb_modes')

        # --- режим ванны: нанесение ---
        self.rb_mode_2 = QRadioButton()
        self.rb_mode_2.setFont(self.default_font)
        self.rb_mode_2.setText('Нанесение')
        self.rb_mode_2.setObjectName('rb_modes')

        # --- режим ванны: движение ---
        self.rb_mode_3 = QRadioButton()
        self.rb_mode_3.setFont(self.default_font)
        self.rb_mode_3.setText('Движение')
        self.rb_mode_3.setChecked(True)
        self.rb_mode_3.setObjectName('rb_modes')

        # --- режим ванны: π-А изотерма ---
        self.rb_mode_4 = QRadioButton()
        self.rb_mode_4.setFont(self.default_font)
        self.rb_mode_4.setText('π-А изотерма')
        self.rb_mode_4.setObjectName('rb_modes')

        # --- группа кнопок ---
        self.rb_group = QButtonGroup()
        self.rb_group.addButton(self.rb_mode_1)
        self.rb_group.addButton(self.rb_mode_2)
        self.rb_group.addButton(self.rb_mode_3)
        self.rb_group.addButton(self.rb_mode_4)

        # --- вертикальный layout для режимов ванны ---
        self.modes_vlayout = QVBoxLayout(self.widget_modes_frame)
        self.modes_vlayout.setContentsMargins(0, 0, 0, 0)
        self.modes_vlayout.setSpacing(5)

        # --- вертикальный layout для режимов ванны: зависимости ---
        self.modes_vlayout.addWidget(self.lbl_modes_title)
        self.modes_vlayout.addWidget(self.rb_mode_1)
        self.modes_vlayout.addWidget(self.rb_mode_2)
        self.modes_vlayout.addWidget(self.rb_mode_3)
        self.modes_vlayout.addWidget(self.rb_mode_4)
        """/область режимов ванны"""

        """область вводимых параметров"""
        # --- область вводимых параметров ---
        self.widget_input_data_frame = QWidget()
        self.widget_input_data_frame.setMinimumWidth(350)
        self.widget_input_data_frame.setObjectName('widget_input_data_frame')

        # --- область вводимых параметров: название ---
        self.lbl_input_data_title = QLabel()
        self.lbl_input_data_title.setFont(self.default_font)
        self.lbl_input_data_title.setText('Вводимые параметры')
        self.lbl_input_data_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_input_data_title.setMaximumHeight(50)
        self.lbl_input_data_title.setMinimumSize(QSize(350, 50))
        self.lbl_input_data_title.setObjectName('lbl_input_data_title')

        # --- параметр: значение концентрации ---
        self.lbl_input_data_1 = QLabel()
        self.lbl_input_data_1.setFont(self.default_font)
        self.lbl_input_data_1.setText('С, моль/л:')
        self.lbl_input_data_1.setMinimumSize(QSize(150, 50))
        self.lbl_input_data_1.setObjectName('lbl_input_data')

        self.ted_input_data_1 = QLineEdit()
        self.ted_input_data_1.setFont(self.default_font)
        self.ted_input_data_1.setPlaceholderText('1E-4')
        self.ted_input_data_1.setMinimumSize(QSize(200, 50))
        self.ted_input_data_1.setObjectName('ted_input_data')

        self.hlayout_input_data_1 = QHBoxLayout()
        self.hlayout_input_data_1.setContentsMargins(0, 0, 0, 0)
        self.hlayout_input_data_1.setSpacing(0)
        self.hlayout_input_data_1.addWidget(self.lbl_input_data_1)
        self.hlayout_input_data_1.addWidget(self.ted_input_data_1)

        # --- параметр: значение объема ---
        self.lbl_input_data_2 = QLabel()
        self.lbl_input_data_2.setFont(self.default_font)
        self.lbl_input_data_2.setText('V, мкл:')
        self.lbl_input_data_2.setMinimumSize(QSize(150, 50))
        self.lbl_input_data_2.setObjectName('lbl_input_data')

        self.ted_input_data_2 = QLineEdit()
        self.ted_input_data_2.setFont(self.default_font)
        self.ted_input_data_2.setPlaceholderText('230')
        self.ted_input_data_2.setMinimumSize(QSize(200, 50))
        self.ted_input_data_2.setObjectName('ted_input_data')

        self.hlayout_input_data_2 = QHBoxLayout()
        self.hlayout_input_data_2.setContentsMargins(0, 0, 0, 0)
        self.hlayout_input_data_2.setSpacing(0)
        self.hlayout_input_data_2.addWidget(self.lbl_input_data_2)
        self.hlayout_input_data_2.addWidget(self.ted_input_data_2)

        # --- параметр: значение скорости сжатия ---
        self.lbl_input_data_3 = QLabel()
        self.lbl_input_data_3.setFont(self.default_font)
        self.lbl_input_data_3.setText('r, см2/мин:')
        self.lbl_input_data_3.setMinimumSize(QSize(150, 50))
        self.lbl_input_data_3.setObjectName('lbl_input_data')

        self.ted_input_data_3 = QLineEdit()
        self.ted_input_data_3.setFont(self.default_font)
        self.ted_input_data_3.setPlaceholderText('55')
        self.ted_input_data_3.setMinimumSize(QSize(200, 50))
        self.ted_input_data_3.setObjectName('ted_input_data')

        self.hlayout_input_data_3 = QHBoxLayout()
        self.hlayout_input_data_3.setContentsMargins(0, 0, 0, 0)
        self.hlayout_input_data_3.setSpacing(0)
        self.hlayout_input_data_3.addWidget(self.lbl_input_data_3)
        self.hlayout_input_data_3.addWidget(self.ted_input_data_3)

        # --- параметр: значение кол-ва циклов ---
        self.lbl_input_data_4 = QLabel()
        self.lbl_input_data_4.setFont(self.default_font)
        self.lbl_input_data_4.setText('n, раз:')
        self.lbl_input_data_4.setMinimumSize(QSize(150, 50))
        self.lbl_input_data_4.setObjectName('lbl_input_data')

        self.ted_input_data_4 = QLineEdit()
        self.ted_input_data_4.setFont(self.default_font)
        self.ted_input_data_4.setPlaceholderText('1')
        self.ted_input_data_4.setMinimumSize(QSize(200, 50))
        self.ted_input_data_4.setObjectName('ted_input_data')

        self.hlayout_input_data_4 = QHBoxLayout()
        self.hlayout_input_data_4.setContentsMargins(0, 0, 0, 0)
        self.hlayout_input_data_4.setSpacing(0)
        self.hlayout_input_data_4.addWidget(self.lbl_input_data_4)
        self.hlayout_input_data_4.addWidget(self.ted_input_data_4)

        # --- вертикальный layout для вводимых параметров ---
        self.input_data_vlayout = QVBoxLayout(self.widget_input_data_frame)
        self.input_data_vlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_data_vlayout.setContentsMargins(0, 0, 0, 0)
        self.input_data_vlayout.setSpacing(0)

        # --- вертикальный layout для вводимых параметров: зависимости ---
        self.input_data_vlayout.addWidget(self.lbl_input_data_title)
        self.input_data_vlayout.addLayout(self.hlayout_input_data_1)
        self.input_data_vlayout.addLayout(self.hlayout_input_data_2)
        self.input_data_vlayout.addLayout(self.hlayout_input_data_3)
        self.input_data_vlayout.addLayout(self.hlayout_input_data_4)
        """/область вводимых параметров"""

        """область кнопок управления"""
        # --- область кнопок управления ---
        self.widget_butttons_frame = QWidget()
        self.widget_butttons_frame.setMinimumWidth(350)
        self.widget_butttons_frame.setObjectName('widget_butttons_frame')

        # --- кнопка: увеличение площади ---
        self.btn_increase_area = QPushButton()
        self.btn_increase_area.setFont(self.default_font)
        self.btn_increase_area.setText('ПЛЮС')
        self.btn_increase_area.setFixedSize(QSize(100, 100))
        self.btn_increase_area.setObjectName('triple_buttons')

        # --- кнопка: старт/стоп ---
        self.btn_start_stop = QPushButton()
        self.btn_start_stop.setFont(self.default_font)
        self.btn_start_stop.setText('СТАРТ\nСТОП')
        self.btn_start_stop.setFixedSize(QSize(100, 100))
        self.btn_start_stop.setObjectName('triple_buttons')

        # --- кнопка: уменьшить область ---
        self.btn_decrease_area = QPushButton()
        self.btn_decrease_area.setFont(self.default_font)
        self.btn_decrease_area.setText('МИНУС')
        self.btn_decrease_area.setFixedSize(QSize(100, 100))
        self.btn_decrease_area.setObjectName('triple_buttons')

        # --- горизонтальный layout для кнопок ---
        self.butttons_hlayout = QHBoxLayout(self.widget_butttons_frame)
        self.butttons_hlayout.setContentsMargins(0, 0, 0, 0)
        self.butttons_hlayout.setSpacing(0)

        # --- горизонтальный layout для кнопок: зависимости ---
        self.butttons_hlayout.addWidget(self.btn_increase_area)
        self.butttons_hlayout.addWidget(self.btn_start_stop)
        self.butttons_hlayout.addWidget(self.btn_decrease_area)
        """/область кнопок управления"""

        """область графика"""
        # --- область графика ---
        self.widget_graph_frame = QWidget()
        self.widget_graph_frame.setMinimumSize(QSize(470, 470))
        self.widget_graph_frame.setObjectName('widget_graph_frame')

        # --- конфигурация графика ---
        data = self.cfg_handler.get('graph')
        GraphH.setCfgOption(('background', data['background']))
        GraphH.setCfgOption(('foreground', data['foreground']))

        # --- график ---
        self.graph_handler = GraphH(self.widget_graph_frame)
        self.graph_handler.plotGraph(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                                      [0.1, 0.5, 0.9, 1.3, 0.5, 
                                       1.7, 2.1, 3.0, 2.5, 2.9]))
        """/область графика"""

        """область выводимых параметров"""
        # --- область выводимых параметров ---
        self.widget_output_data_frame = QWidget()
        self.widget_output_data_frame.setMinimumWidth(350)
        self.widget_output_data_frame.setObjectName('widget_output_data_frame')

        # --- область выводимых параметров: название ---
        self.lbl_output_data_title = QLabel()
        self.lbl_output_data_title.setFont(self.default_font)
        self.lbl_output_data_title.setText('Выводимые параметры')
        self.lbl_output_data_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_output_data_title.setMaximumHeight(50)
        self.lbl_output_data_title.setMinimumSize(QSize(350, 50))
        self.lbl_output_data_title.setObjectName('lbl_output_data_title')

        # --- параметр: значение поверхностного давления ---
        self.lbl_output_data_1 = QLabel()
        self.lbl_output_data_1.setFont(self.default_font)
        self.lbl_output_data_1.setText('π, мН/м:')
        self.lbl_output_data_1.setMinimumSize(QSize(150, 50))
        self.lbl_output_data_1.setObjectName('lbl_output_data')

        self.ted_output_data_1 = QLineEdit()
        self.ted_output_data_1.setFont(self.default_font)
        self.ted_output_data_1.setPlaceholderText('None')
        self.ted_output_data_1.setReadOnly(True)
        self.ted_output_data_1.setMinimumSize(QSize(100, 50))
        self.ted_output_data_1.setObjectName('ted_output_data')

        self.hlayout_output_data_1 = QHBoxLayout()
        self.hlayout_output_data_1.setContentsMargins(0, 0, 0, 0)
        self.hlayout_output_data_1.setSpacing(0)
        self.hlayout_output_data_1.addWidget(self.lbl_output_data_1)
        self.hlayout_output_data_1.addWidget(self.ted_output_data_1)

        # --- параметр: значение площади ванны ---
        self.lbl_output_data_2 = QLabel()
        self.lbl_output_data_2.setFont(self.default_font)
        self.lbl_output_data_2.setText('S, см2:')
        self.lbl_output_data_2.setMinimumSize(QSize(150, 50))
        self.lbl_output_data_2.setObjectName('lbl_output_data')

        self.ted_output_data_2 = QLineEdit()
        self.ted_output_data_2.setFont(self.default_font)
        self.ted_output_data_2.setPlaceholderText('None')
        self.ted_output_data_2.setReadOnly(True)
        self.ted_output_data_2.setMinimumSize(QSize(100, 50))
        self.ted_output_data_2.setObjectName('ted_output_data')

        self.hlayout_output_data_2 = QHBoxLayout()
        self.hlayout_output_data_2.setContentsMargins(0, 0, 0, 0)
        self.hlayout_output_data_2.setSpacing(0)
        self.hlayout_output_data_2.addWidget(self.lbl_output_data_2)
        self.hlayout_output_data_2.addWidget(self.ted_output_data_2)

        # --- кнопка: зануления значения поверхностного давления ---
        self.btn_reset_pressure = QPushButton()
        self.btn_reset_pressure.setFont(self.default_font)
        self.btn_reset_pressure.setText('π=0')
        self.btn_reset_pressure.setFixedSize(QSize(90, 90))
        self.btn_reset_pressure.setObjectName('btn_reset_pressure')
        self.btn_reset_pressure.clicked.connect(None)  # TODO: реализовать метод

        # --- вертикальный layout для параметров ---
        self.vlayout_output_data = QVBoxLayout()
        self.vlayout_output_data.setContentsMargins(0, 0, 0, 0)
        self.vlayout_output_data.setSpacing(0)
        self.vlayout_output_data.addLayout(self.hlayout_output_data_1)
        self.vlayout_output_data.addLayout(self.hlayout_output_data_2)

        # --- горизонтальный layout для параметров и кнопки
        self.hlayout_output_data = QHBoxLayout()
        self.hlayout_output_data.setContentsMargins(0, 0, 0, 0)
        self.hlayout_output_data.setSpacing(0)
        self.hlayout_output_data.addLayout(self.vlayout_output_data)
        self.hlayout_output_data.addWidget(self.btn_reset_pressure)

        # --- вертикальный layout для выводимых параметров ---
        self.output_data_vlayout = QVBoxLayout(self.widget_output_data_frame)
        self.output_data_vlayout.setContentsMargins(0, 0, 0, 0)
        self.output_data_vlayout.setSpacing(0)

        # --- вертикальный layout для выводимых параметров: зависимости ---
        self.output_data_vlayout.addWidget(self.lbl_output_data_title)
        self.output_data_vlayout.addLayout(self.hlayout_output_data)
        """/область выводимых параметров"""

        # --- вертикальный layout для режимов работы ванны, 
        # вводимых параметров и кнопок ---
        self.vlayout_1 = QVBoxLayout()
        self.vlayout_1.setContentsMargins(5, 5, 5, 5)
        self.vlayout_1.setSpacing(20)
        self.vlayout_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # --- вертикальный layout для режимов ...: зависимости ---
        self.vlayout_1.addWidget(self.widget_modes_frame)
        self.vlayout_1.addWidget(self.widget_input_data_frame)
        self.vlayout_1.addSpacerItem(QSpacerItem(50, 50, QSizePolicy.Policy.Expanding, 
                                                 QSizePolicy.Policy.Expanding))
        self.vlayout_1.addWidget(self.widget_butttons_frame)

        # --- вертикальный layout для графика и выводимых параметров ---
        self.vlayout_2 = QVBoxLayout()
        self.vlayout_2.setContentsMargins(5, 5, 5, 5)
        self.vlayout_2.setSpacing(20)

        # --- вертикальный layout для режимов ...: зависимости ---
        self.vlayout_2.addWidget(self.graph_handler.view)
        self.vlayout_2.addWidget(self.widget_output_data_frame)

        # --- горизонтальный layout для центральной области ---
        self.central_hlayout = QHBoxLayout(self.widget_central_area)
        self.central_hlayout.setContentsMargins(10, 10, 10, 10)
        self.central_hlayout.setSpacing(0)

        # --- горизонтальный layout для центральной области: зависимости ---
        self.central_hlayout.addLayout(self.vlayout_1)
        self.central_hlayout.addLayout(self.vlayout_2)
        """/CentralAreaWidget"""

        """BottomBarWidget"""
        # --- нижняя панель ---
        self.widget_bottom_bar_frame = QWidget(self)
        self.widget_bottom_bar_frame.setFixedHeight(30)
        self.widget_bottom_bar_frame.setObjectName('widget_bottom_bar_frame')

        # --- индикатор COM порта ---
        self.lbl_com_port_status = QLabel()
        self.lbl_com_port_status.setFont(self.spec_font)
        self.lbl_com_port_status.setText('')
        self.lbl_com_port_status.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.lbl_com_port_status.setStyleSheet('background: red; border-radius: 10%;')
        self.lbl_com_port_status.setFixedSize(QSize(20, 20))
        self.lbl_com_port_status.setObjectName('lbl_com_port_status')

        # --- кнопка открытия COM порта ---
        self.btn_open_com_port = QPushButton()
        self.btn_open_com_port.setFont(QFont('Sans Serif', 10))
        self.btn_open_com_port.setText('ОТКРЫТЬ')
        self.btn_open_com_port.setFixedSize(QSize(120, 20))
        self.btn_open_com_port.setObjectName('btn_open_close_com_port')
        self.btn_open_com_port.clicked.connect(self._open_port_clicked)

        # --- кнопка закрытия COM порта ---
        self.btn_close_com_port = QPushButton()
        self.btn_close_com_port.setFont(QFont('Sans Serif', 10))
        self.btn_close_com_port.setText('ЗАКРЫТЬ')
        self.btn_close_com_port.setFixedSize(QSize(120, 20))
        self.btn_close_com_port.setObjectName('btn_open_close_com_port')
        self.btn_close_com_port.hide()
        self.btn_close_com_port.clicked.connect(self._close_port_clicked)
        
        # --- кнопка открытия меню весов ---
        self.btn_open_weighers_menu = QPushButton()
        self.btn_open_weighers_menu.setFont(QFont('Sans Serif', 10))
        self.btn_open_weighers_menu.setText('МЕНЮ ВЕСОВ')
        self.btn_open_weighers_menu.setFixedSize(QSize(120, 20))
        self.btn_open_weighers_menu.setEnabled(
            self.cfg_handler.get('weighers')['use_weighers'])
        self.btn_open_weighers_menu.setObjectName('btn_open_weighers_menu')
        self.btn_open_weighers_menu.clicked.connect(self._show_weighers_menu)

        # --- изменение размера окна ---
        self.bottom_right_size_grip = QSizeGrip(self.widget_bottom_bar_frame)
        self.bottom_right_size_grip.setFixedSize(QSize(30, 30))

        # --- горизонтальный layout для нижней панели ---
        self.bottom_bar_hlayout = QHBoxLayout(self.widget_bottom_bar_frame)
        self.bottom_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.bottom_bar_hlayout.setSpacing(0)

        # --- горизонтальный layout для нижней панели: зависимости ---
        self.bottom_bar_hlayout.addWidget(self.lbl_com_port_status)
        self.bottom_bar_hlayout.addWidget(self.btn_open_com_port)
        self.bottom_bar_hlayout.addWidget(self.btn_close_com_port)
        self.bottom_bar_hlayout.addSpacerItem(QSpacerItem(50, 30, 
                                                          QSizePolicy.Policy.Expanding, 
                                                          QSizePolicy.Policy.Minimum))
        self.bottom_bar_hlayout.addWidget(self.btn_open_weighers_menu)
        self.bottom_bar_hlayout.addWidget(self.bottom_right_size_grip)
        """/BottomBarWidget"""

        """GeneralLayout"""
        # --- вертикальный layout для всего окна ---
        self.general_vlayout = QVBoxLayout(self)
        self.general_vlayout.setContentsMargins(0, 0, 0, 0)
        self.general_vlayout.addSpacing(0)

        # --- вертикальный layout для всего окна: зависимости ---
        self.general_vlayout.addWidget(self.widget_top_bar_frame)
        self.general_vlayout.addWidget(self.widget_central_area)
        self.general_vlayout.addWidget(self.widget_bottom_bar_frame)
        """/GeneralLayout"""

    # вызывается при нажатии кнопки мыши по форме
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # получаем координаты окна относительно экрана
            x_main = self.geometry().x()
            y_main = self.geometry().y()
            # получаем координаты курсора относительно окна программы
            cursor_x = QCursor.pos().x()
            cursor_y = QCursor.pos().y()
            # проверяем, чтобы курсор был внутри виджета self.toolBar
            if x_main <= cursor_x <= x_main + self.geometry().width():
                if (y_main <= cursor_y <= y_main + 
                    self.widget_top_bar_frame.geometry().height()):
                    self.old_pos = event.pos()
                else: self.old_pos = None
        elif event.button() == Qt.MouseButton.RightButton: self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton: self.old_pos = None

    # вызыватся при перемещении мыши
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
            
            if hasattr(self, 'settings_win'):
                self.settings_win.move(
                    self.pos() + delta + QPoint(
                        self.geometry().width() - self.settings_win.width() - 90, 
                        self.widget_top_bar_frame.height()
                    ))
            
            if hasattr(self, 'weighers_win'):
                self.weighers_win.move(
                    self.pos() + delta + QPoint(
                        self.geometry().width() - self.weighers_win.width(), 
                        self.geometry().height() - self.weighers_win.height() - 30
                    ))

    def _show_settings(self):
        self.settings_win = SettingsWindowUI(self.btn_open_weighers_menu)
        self.settings_win.setup_ui()
        self.settings_win.show()

        # перемещение окна к позиции под кнопкой настроек
        self.settings_win_x = (self.geometry().left() + self.geometry().width() - 
                               self.settings_win.width() - 90)
        self.settings_win_y = (self.geometry().top() + 
                               self.widget_top_bar_frame.height())
        self.settings_win.move(self.settings_win_x, self.settings_win_y)

    def _exit(self):
        # TODO: сделать проверку состояния COM порта
        # exit()
        self.close()

    def _show_weighers_menu(self):
        self.weighers_win = WeighersWindowUI()
        self.weighers_win.setup_ui()
        self.weighers_win.show()

        # перемещение окна к позиции над кнопкой меню весов
        self.weighers_win_x = (self.geometry().left() + self.geometry().width() - 
                               self.weighers_win.width())
        self.weighers_win_y = (self.geometry().top() + self.geometry().height() - 
                               self.weighers_win.height() - 30)
        self.weighers_win.move(self.weighers_win_x, self.weighers_win_y)

    def _open_port_clicked(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())

    def _close_port_clicked(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())

    def __change_com_port_status(self, status: bool):
        if status:
            self.btn_open_com_port.hide()
            self.btn_close_com_port.show()
            self.lbl_com_port_status.setStyleSheet(
                'background: green; border-radius: 10%;'
            )
        else:
            self.btn_open_com_port.show()
            self.btn_close_com_port.hide()
            self.lbl_com_port_status.setStyleSheet(
                'background: red; border-radius: 10%;'
            )

    def _full_screen(self):
        if not self.full_screen_flag:
            self.last_window_size = self.size()
            self.last_window_pos = self.pos()
            self.move(0, 0)
            self.resize(self.screen().geometry().width(), 
                        self.screen().geometry().height())
        else:
            self.resize(self.last_window_size)
            self.move(self.last_window_pos)

        self.full_screen_flag = not self.full_screen_flag
