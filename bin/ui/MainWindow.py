from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QButtonGroup, QLineEdit
from PySide6.QtGui import QCursor, QFont
from PySide6.QtCore import Qt, QRect, QSize

from settings import __app_name__, CFG_PATH
from bin.ui.styles import MAIN_WINDOW
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.handlers.Graph import GraphH


class MainWindowUI(QWidget):

    def __init__(self):
        super().__init__()
        self.old_pos = None
        self.default_font = QFont('Sans Serif', 16)
        self.spec_font = QFont('Sans Serif', 14)

        self.cfg_handler = ConfigurationFileH(CFG_PATH)
    
    def setup_ui(self):
        # --- настройки окна ---
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(QSize(1280, 600))
        self.setStyleSheet(MAIN_WINDOW)
        self.setObjectName('MainWindowUI')

        # --- верхняя панель ---
        self.widget_top_bar_frame = QWidget(self)
        self.widget_top_bar_frame.setGeometry(QRect(0, 0, 1280, 30))
        self.widget_top_bar_frame.setObjectName('widget_top_bar_frame')

        # --- название окна ---
        self.lbl_tb_title = QLabel(self.widget_top_bar_frame)
        self.lbl_tb_title.setFont(self.spec_font)
        self.lbl_tb_title.setText(__app_name__)
        self.lbl_tb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_tb_title.setGeometry(QRect(0, 0, 200, 30))
        self.lbl_tb_title.setObjectName('lbl_tb_title')

        # --- кнопка настроек ---
        self.btn_tb_settings = QPushButton(self.widget_top_bar_frame)
        self.btn_tb_settings.setFont(self.spec_font)
        self.btn_tb_settings.setText('⚒')  # TODO: использовать иконку
        self.btn_tb_settings.setGeometry(QRect(1190, 0, 30, 30))
        self.btn_tb_settings.setObjectName('top_bar_buttons')
        self.btn_tb_settings.clicked.connect(self._show_settings)

        # --- кнопка минимизации ---
        self.btn_tb_minimize = QPushButton(self.widget_top_bar_frame)
        self.btn_tb_minimize.setFont(self.spec_font)
        self.btn_tb_minimize.setText('▬')  # TODO: использовать иконку
        self.btn_tb_minimize.setGeometry(QRect(1220, 0, 30, 30))
        self.btn_tb_minimize.setObjectName('top_bar_buttons')
        self.btn_tb_minimize.clicked.connect(self.showMinimized)

        # --- кнопка выхода ---
        self.btn_tb_exit = QPushButton(self.widget_top_bar_frame)
        self.btn_tb_exit.setFont(self.spec_font)
        self.btn_tb_exit.setText('✖')  # TODO: использовать иконку
        self.btn_tb_exit.setGeometry(QRect(1250, 0, 30, 30))
        self.btn_tb_exit.setObjectName('top_bar_buttons')
        self.btn_tb_exit.clicked.connect(self._show_exit)

        # --- основная обаласть ---
        self.widget_central_widget = QWidget(self)
        self.widget_central_widget.setGeometry(QRect(5, 35, 1270, 530))
        self.widget_central_widget.setObjectName('widget_central_widget')

        # --- область режимов ванны ---
        self.widget_modes_frame = QWidget(self.widget_central_widget)
        self.widget_modes_frame.setGeometry(QRect(0, 0, 350, 250))
        self.widget_modes_frame.setObjectName('widget_modes_frame')

        # --- область режимов ванны: название ---
        self.lbl_modes_title = QLabel(self.widget_modes_frame)
        self.lbl_modes_title.setFont(self.default_font)
        self.lbl_modes_title.setText('Режимы ванны')
        self.lbl_modes_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_modes_title.setGeometry(QRect(0, 0, 350, 50))
        self.lbl_modes_title.setObjectName('lbl_modes_title')

        # --- режим ванны: очистка ---
        self.rb_mode_1 = QRadioButton(self.widget_modes_frame)
        self.rb_mode_1.setFont(self.default_font)
        self.rb_mode_1.setText('Очистка')
        self.rb_mode_1.setGeometry(QRect(0, 50, 350, 50))
        self.rb_mode_1.setObjectName('rb_modes')

        # --- режим ванны: нанесение ---
        self.rb_mode_2 = QRadioButton(self.widget_modes_frame)
        self.rb_mode_2.setFont(self.default_font)
        self.rb_mode_2.setText('Нанесение')
        self.rb_mode_2.setGeometry(QRect(0, 100, 350, 50))
        self.rb_mode_2.setObjectName('rb_modes')

        # --- режим ванны: движение ---
        self.rb_mode_3 = QRadioButton(self.widget_modes_frame)
        self.rb_mode_3.setFont(self.default_font)
        self.rb_mode_3.setText('Движение')
        self.rb_mode_3.setGeometry(QRect(0, 150, 350, 50))
        self.rb_mode_3.setObjectName('rb_modes')

        # --- режим ванны: π-А изотерма ---
        self.rb_mode_4 = QRadioButton(self.widget_modes_frame)
        self.rb_mode_4.setFont(self.default_font)
        self.rb_mode_4.setText('π-А изотерма')
        self.rb_mode_4.setGeometry(QRect(0, 200, 350, 50))
        self.rb_mode_4.setObjectName('rb_modes')

        # --- группа кнопок ---
        self.rb_group = QButtonGroup()
        self.rb_group.addButton(self.rb_mode_1)
        self.rb_group.addButton(self.rb_mode_2)
        self.rb_group.addButton(self.rb_mode_3)
        self.rb_group.addButton(self.rb_mode_4)

        # --- область вводимых параметров ---
        self.widget_input_data_frame = QWidget(self.widget_central_widget)
        self.widget_input_data_frame.setGeometry(QRect(400, 0, 350, 250))
        self.widget_input_data_frame.setObjectName('widget_input_data_frame')

        # --- область вводимых параметров: название ---
        self.lbl_input_data_title = QLabel(self.widget_input_data_frame)
        self.lbl_input_data_title.setFont(self.default_font)
        self.lbl_input_data_title.setText('Вводимые параметры')
        self.lbl_input_data_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_input_data_title.setGeometry(QRect(0, 0, 350, 50))
        self.lbl_input_data_title.setObjectName('lbl_input_data_title')

        # --- параметр: значение концентрации ---
        self.lbl_input_data_1 = QLabel(self.widget_input_data_frame)
        self.lbl_input_data_1.setFont(self.default_font)
        self.lbl_input_data_1.setText('С, моль/л:')
        self.lbl_input_data_1.setGeometry(QRect(0, 50, 150, 50))
        self.lbl_input_data_1.setObjectName('lbl_input_data')

        self.ted_input_data_1 = QLineEdit(self.widget_input_data_frame)
        self.ted_input_data_1.setFont(self.default_font)
        self.ted_input_data_1.setPlaceholderText('1E-4')
        self.ted_input_data_1.setGeometry(QRect(150, 50, 200, 50))
        self.ted_input_data_1.setObjectName('ted_input_data')

        # --- параметр: значение объема ---
        self.lbl_input_data_2 = QLabel(self.widget_input_data_frame)
        self.lbl_input_data_2.setFont(self.default_font)
        self.lbl_input_data_2.setText('V, мкл:')
        self.lbl_input_data_2.setGeometry(QRect(0, 100, 150, 50))
        self.lbl_input_data_2.setObjectName('lbl_input_data')

        self.ted_input_data_2 = QLineEdit(self.widget_input_data_frame)
        self.ted_input_data_2.setFont(self.default_font)
        self.ted_input_data_2.setPlaceholderText('230')
        self.ted_input_data_2.setGeometry(QRect(150, 100, 200, 50))
        self.ted_input_data_2.setObjectName('ted_input_data')

        # --- параметр: значение скорости сжатия ---
        self.lbl_input_data_3 = QLabel(self.widget_input_data_frame)
        self.lbl_input_data_3.setFont(self.default_font)
        self.lbl_input_data_3.setText('r, см2/мин:')
        self.lbl_input_data_3.setGeometry(QRect(0, 150, 150, 50))
        self.lbl_input_data_3.setObjectName('lbl_input_data')

        self.ted_input_data_3 = QLineEdit(self.widget_input_data_frame)
        self.ted_input_data_3.setFont(self.default_font)
        self.ted_input_data_3.setPlaceholderText('55')
        self.ted_input_data_3.setGeometry(QRect(150, 150, 200, 50))
        self.ted_input_data_3.setObjectName('ted_input_data')

        # --- параметр: значение кол-ва циклов ---
        self.lbl_input_data_4 = QLabel(self.widget_input_data_frame)
        self.lbl_input_data_4.setFont(self.default_font)
        self.lbl_input_data_4.setText('n, раз:')
        self.lbl_input_data_4.setGeometry(QRect(0, 200, 150, 50))
        self.lbl_input_data_4.setObjectName('lbl_input_data')

        self.ted_input_data_4 = QLineEdit(self.widget_input_data_frame)
        self.ted_input_data_4.setFont(self.default_font)
        self.ted_input_data_4.setPlaceholderText('1')
        self.ted_input_data_4.setGeometry(QRect(150, 200, 200, 50))
        self.ted_input_data_4.setObjectName('ted_input_data')

        # --- область кнопок управления ---
        self.widget_butttons_frame = QWidget(self.widget_central_widget)
        self.widget_butttons_frame.setGeometry(QRect(0, 325, 350, 100))
        self.widget_butttons_frame.setObjectName('widget_butttons_frame')

        # --- кнопка: увеличение площади ---
        self.btn_increase_area = QPushButton(self.widget_butttons_frame)
        self.btn_increase_area.setFont(self.default_font)
        self.btn_increase_area.setText('ПЛЮС')
        self.btn_increase_area.setGeometry(QRect(0, 0, 100, 100))
        self.btn_increase_area.setObjectName('triple_buttons')

        # --- кнопка: старт/стоп ---
        self.btn_start_stop = QPushButton(self.widget_butttons_frame)
        self.btn_start_stop.setFont(self.default_font)
        self.btn_start_stop.setText('СТАРТ\nСТОП')
        self.btn_start_stop.setGeometry(QRect(125, 0, 100, 100))
        self.btn_start_stop.setObjectName('triple_buttons')

        # --- кнопка: уменьшить область ---
        self.btn_decrease_area = QPushButton(self.widget_butttons_frame)
        self.btn_decrease_area.setFont(self.default_font)
        self.btn_decrease_area.setText('МИНУС')
        self.btn_decrease_area.setGeometry(QRect(250, 0, 100, 100))
        self.btn_decrease_area.setObjectName('triple_buttons')

        # --- область-рамка для графика ---
        self.widget_graph = QWidget(self.widget_central_widget)
        self.widget_graph.setGeometry(QRect(800, 30, 470, 470))
        self.widget_graph.setObjectName('widget_graph')

        # --- область графика ---
        self.widget_graph_frame = QWidget(self.widget_graph)
        self.widget_graph_frame.setGeometry(QRect(5, 5, 460, 460))
        self.widget_graph_frame.setObjectName('widget_graph_frame')

        # --- конфигурация графика ---
        data = self.cfg_handler.get('graph')
        GraphH.setCfgOption(('background', data['background']))
        GraphH.setCfgOption(('foreground', data['foreground']))

        self.graph_handler = GraphH(self.widget_graph_frame)
        self.graph_handler.plotGraph((
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            [0.1, 0.5, 0.9, 0.13*10, 0.5, 0.17*10, 
             0.21*10, 0.30*10, 0.25*10, 0.29*10]
        ))

        # --- область выводимых параметров ---
        self.widget_output_data_frame = QWidget(self.widget_central_widget)
        self.widget_output_data_frame.setGeometry(QRect(400, 300, 350, 150))
        self.widget_output_data_frame.setObjectName('widget_output_data_frame')

        # --- область выводимых параметров: название ---
        self.lbl_output_data_title = QLabel(self.widget_output_data_frame)
        self.lbl_output_data_title.setFont(self.default_font)
        self.lbl_output_data_title.setText('Выводимые показания')
        self.lbl_output_data_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_output_data_title.setGeometry(QRect(0, 0, 350, 50))
        self.lbl_output_data_title.setObjectName('lbl_output_data_title')

        # --- параметр: значение поверхностного давления ---
        self.lbl_output_data_1 = QLabel(self.widget_output_data_frame)
        self.lbl_output_data_1.setFont(self.default_font)
        self.lbl_output_data_1.setText('π, мН/м:')
        self.lbl_output_data_1.setGeometry(QRect(0, 50, 150, 50))
        self.lbl_output_data_1.setObjectName('lbl_output_data')

        self.ted_output_data_1 = QLineEdit(self.widget_output_data_frame)
        self.ted_output_data_1.setFont(self.default_font)
        self.ted_output_data_1.setPlaceholderText('None')
        self.ted_output_data_1.setReadOnly(True)
        self.ted_output_data_1.setGeometry(QRect(150, 50, 100, 50))
        self.ted_output_data_1.setObjectName('ted_output_data')

        # --- параметр: значение площади ванны ---
        self.lbl_output_data_2 = QLabel(self.widget_output_data_frame)
        self.lbl_output_data_2.setFont(self.default_font)
        self.lbl_output_data_2.setText('S, см2:')
        self.lbl_output_data_2.setGeometry(QRect(0, 100, 150, 50))
        self.lbl_output_data_2.setObjectName('lbl_output_data')

        self.ted_output_data_2 = QLineEdit(self.widget_output_data_frame)
        self.ted_output_data_2.setFont(self.default_font)
        self.ted_output_data_2.setPlaceholderText('None')
        self.ted_output_data_2.setReadOnly(True)
        self.ted_output_data_2.setGeometry(QRect(150, 100, 100, 50))
        self.ted_output_data_2.setObjectName('ted_output_data')

        # --- кнопка: зануления значения поверхностного давления ---
        self.btn_reset_pressure = QPushButton(self.widget_output_data_frame)
        self.btn_reset_pressure.setFont(self.default_font)
        self.btn_reset_pressure.setText('π=0')
        self.btn_reset_pressure.setGeometry(QRect(250, 55, 90, 90))
        self.btn_reset_pressure.setObjectName('btn_reset_pressure')
        self.btn_reset_pressure.clicked.connect(None)  # TODO: реализовать метод

        # --- нижняя панель ---
        self.widget_bottom_bar_frame = QWidget(self)
        self.widget_bottom_bar_frame.setGeometry(QRect(0, 570, 1280, 30))
        self.widget_bottom_bar_frame.setObjectName('widget_bottom_bar_frame')

        # --- индикатор COM порта ---
        self.lbl_com_port_status = QLabel(self.widget_bottom_bar_frame)
        self.lbl_com_port_status.setFont(self.spec_font)
        self.lbl_com_port_status.setText('')
        self.lbl_com_port_status.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.lbl_com_port_status.setStyleSheet('background: red; border-radius: 10%;')
        self.lbl_com_port_status.setGeometry(QRect(15, 5, 20, 20))
        self.lbl_com_port_status.setObjectName('lbl_com_port_status')

        # --- кнопка открытия COM порта ---
        self.btn_open_com_port = QPushButton(self.widget_bottom_bar_frame)
        self.btn_open_com_port.setFont(QFont('Sans Serif', 10))
        self.btn_open_com_port.setText('ОТКРЫТЬ')
        self.btn_open_com_port.setGeometry(QRect(50, 5, 120, 20))
        self.btn_open_com_port.setObjectName('btn_open_close_com_port')
        self.btn_open_com_port.clicked.connect(self._open_port_clicked)

        # --- кнопка закрытия COM порта ---
        self.btn_close_com_port = QPushButton(self.widget_bottom_bar_frame)
        self.btn_close_com_port.setFont(QFont('Sans Serif', 10))
        self.btn_close_com_port.setText('ЗАКРЫТЬ')
        self.btn_close_com_port.setGeometry(QRect(50, 5, 120, 20))
        self.btn_close_com_port.setObjectName('btn_open_close_com_port')
        self.btn_close_com_port.hide()
        self.btn_close_com_port.clicked.connect(self._close_port_clicked)

        # --- кнопка открытия меню весов ---
        self.btn_open_weigher_menu = QPushButton(self.widget_bottom_bar_frame)
        self.btn_open_weigher_menu.setFont(QFont('Sans Serif', 10))
        self.btn_open_weigher_menu.setText('МЕНЮ ВЕСОВ')
        self.btn_open_weigher_menu.setGeometry(QRect(1145, 5, 120, 20))
        self.btn_open_weigher_menu.setObjectName('btn_open_weigher_menu')
        self.btn_open_weigher_menu.clicked.connect(self._show_weigher_menu)

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

    def _show_settings(self):
        pass

    def _show_exit(self):
        # TODO: сделать проверку состояния COM порта
        exit()

    def _show_weigher_menu(self):
        pass

    def _open_port_clicked(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())
        pass

    def _close_port_clicked(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())
        pass

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
