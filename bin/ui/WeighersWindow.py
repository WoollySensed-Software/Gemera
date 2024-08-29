from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QComboBox, 
    QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtCore import Qt, QSize

from settings import CFG_PATH, INCLUDES
from bin.handlers.ConfigurationFile import ConfigurationFileH


class WeighersWindowUI(QWidget):

    def __init__(self):
        super().__init__()
        self.old_pos = None
        self.default_font = QFont('Sans Serif', 16)
        self.spec_font = QFont('Sans Serif', 14)
        self.cfg_handler = ConfigurationFileH(CFG_PATH)
        self.commands = {
            # Команда проверки работоспособности датчика.
            '$MTM': None,
            # Запрос номера версии программного обеспечения датчика.
            '$MTM,FW': None,
            # Чтение серийного номера датчика.
            '$MTM,SER': None,
            # Перезагрузка контроллера датчика.
            '$MTM,RST': None,
            # Считывание сигнала АЦП.
            '$MTM,SENSOR': None,
            # Команда запуска передачи данных.
            r'START\n': None,
            # Команда остановки передачи данных.
            r'END\n': None
        }
    
    def setup_ui(self):
        # --- настройка окна ---
        self.setWindowTitle('Меню весов')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.WindowStaysOnTopHint)
        self.setMinimumSize(350, 200)
        self.setObjectName('WeighersWindowUI')

        # --- верхняя панель ---
        self.widget_top_bar_frame = QWidget()
        self.widget_top_bar_frame.setFixedHeight(30)
        self.widget_top_bar_frame.setObjectName('BarFrame')
        
        # --- основная область ---
        self.widget_central_area = QWidget()
        self.widget_central_area.setObjectName('widget_central_area')

        # --- название окна ---
        self.lbl_tb_title = QLabel()
        self.lbl_tb_title.setFont(self.spec_font)
        self.lbl_tb_title.setText('Меню весов | BETA')
        self.lbl_tb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_tb_title.setFixedWidth(200)
        self.lbl_tb_title.setObjectName('BF-Title')

        # --- кнопка минимизации ---
        self.btn_tb_minimize = QPushButton()
        self.btn_tb_minimize.setIcon(QIcon(
            f'{INCLUDES['minus.png'][0]}'.replace('\\', '/')))
        self.btn_tb_minimize.setIconSize(QSize(20, 20))
        self.btn_tb_minimize.setFixedSize(QSize(30, 30))
        self.btn_tb_minimize.setObjectName('BF-Buttons')
        self.btn_tb_minimize.clicked.connect(self.showMinimized)

        # --- кнопка выхода ---
        self.btn_tb_exit = QPushButton(self.widget_top_bar_frame)
        self.btn_tb_exit.setIcon(QIcon(
            f'{INCLUDES['close.png'][0]}'.replace('\\', '/')))
        self.btn_tb_exit.setIconSize(QSize(15, 15))
        self.btn_tb_exit.setFixedSize(QSize(30, 30))
        self.btn_tb_exit.setObjectName('BF-Buttons')
        self.btn_tb_exit.clicked.connect(self._exit)

        # --- горизонтальный layout для верхней панели ---
        self.top_bar_hlayout = QHBoxLayout(self.widget_top_bar_frame)
        self.top_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_hlayout.setSpacing(0)

        # --- горизонтальный layout для верхней панели: зависимости ---
        self.top_bar_hlayout.addWidget(self.lbl_tb_title)
        self.top_bar_hlayout.addSpacerItem(QSpacerItem(50, 30, 
                                                       QSizePolicy.Policy.Expanding, 
                                                       QSizePolicy.Policy.Minimum))
        self.top_bar_hlayout.addWidget(self.btn_tb_minimize)
        self.top_bar_hlayout.addWidget(self.btn_tb_exit)

        # --- выбор команды ---
        self.cb_command = QComboBox()
        self.cb_command.setFont(self.default_font)
        self.cb_command.setMinimumSize(QSize(200, 50))
        self.cb_command.addItems(self.commands.keys())
        self.cb_command.setMaxVisibleItems(5)
        self.cb_command.setObjectName('cb_command')

        # --- кнопка ввода команды ---
        self.btn_send_command = QPushButton()
        self.btn_send_command.setFont(self.default_font)
        self.btn_send_command.setText('Отправить')
        self.btn_send_command.setMinimumSize(QSize(200, 30))
        self.btn_send_command.setObjectName('buttons')
        self.btn_send_command.clicked.connect(self._send_command)

        # --- кнопка открытия com порта ---
        self.btn_open_com_port = QPushButton()
        self.btn_open_com_port.setFont(self.default_font)
        self.btn_open_com_port.setText('Открыть порт')
        self.btn_open_com_port.setMinimumSize(QSize(200, 30))
        self.btn_open_com_port.setObjectName('buttons')
        self.btn_open_com_port.clicked.connect(self._open_com_port)

        # --- кнопка закрытия com порта ---
        self.btn_close_com_port = QPushButton()
        self.btn_close_com_port.setFont(self.default_font)
        self.btn_close_com_port.setText('Закрыть порт')
        self.btn_close_com_port.setMinimumSize(QSize(200, 30))
        self.btn_close_com_port.setObjectName('buttons')
        self.btn_close_com_port.hide()
        self.btn_close_com_port.clicked.connect(self._close_com_port)

        # --- вертикальный layout для центральной области ---
        self.central_vlayout = QVBoxLayout(self.widget_central_area)
        self.central_vlayout.setContentsMargins(10, 10, 10, 10)
        self.central_vlayout.setSpacing(5)

        # --- вертикальный layout для центральной области: зависимости ---
        self.central_vlayout.addWidget(self.cb_command)
        self.central_vlayout.addWidget(self.btn_send_command)
        self.central_vlayout.addSpacerItem(QSpacerItem(50, 30, 
                                                       QSizePolicy.Policy.Minimum, 
                                                       QSizePolicy.Policy.Expanding))
        self.central_vlayout.addWidget(self.btn_open_com_port)
        self.central_vlayout.addWidget(self.btn_close_com_port)

        # --- вертикальный layout для всего окна ---
        self.general_vlayout = QVBoxLayout(self)
        self.general_vlayout.setContentsMargins(0, 0, 0, 0)
        self.general_vlayout.setSpacing(0)

        # --- вертикальный layout для всего окна: зависимости ---
        self.general_vlayout.addWidget(self.widget_top_bar_frame)
        self.general_vlayout.addWidget(self.widget_central_area)

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
        elif event.button() == Qt.MouseButton.RightButton:
            self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None

    # вызыватся при перемещении мыши
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

    def _exit(self):
        # TODO: реализовать закрытие com порта
        self.close()

    def _send_command(self):
        print(self.cb_command.currentText())  # TEST
        print(self.size())  # TEST

    def _open_com_port(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())

    def _close_com_port(self):
        self.__change_com_port_status(self.btn_open_com_port.isVisible())

    def __change_com_port_status(self, status: bool):
        if status:
            self.btn_open_com_port.hide()
            self.btn_close_com_port.show()
        else:
            self.btn_open_com_port.show()
            self.btn_close_com_port.hide()
