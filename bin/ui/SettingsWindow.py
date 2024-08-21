from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, 
    QRadioButton, QButtonGroup, QLineEdit, 
    QHBoxLayout, QVBoxLayout, QSpacerItem, 
    QSizePolicy, QGridLayout, QSizeGrip, 
    QComboBox, QCheckBox, QMessageBox
)
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtCore import Qt, QRect, QSize

from settings import CFG_PATH
from bin.ui.styles import MAIN_WINDOW
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.handlers.Serial import SerialH


class SettingsWindowUI(QWidget):

    def __init__(self):
        super().__init__()
        self.old_pos = None
        self.default_font = QFont('Sans Serif', 16)
        self.cfg_handler = ConfigurationFileH(CFG_PATH)
    
    def setup_ui(self):
        # --- настройки окна ---
        self.setWindowTitle('Настройки')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setMinimumSize(QSize(350, 310))
        self.setObjectName('SettingsWindowUI')

        # --- верхняя панель ---
        self.widget_top_bar_frame = QWidget()
        self.widget_top_bar_frame.setFixedHeight(30)
        self.widget_top_bar_frame.setObjectName('widget_top_bar_frame')

        # --- основная область ---
        self.widget_central_area = QWidget()
        self.widget_central_area.setObjectName('widget_central_area')

        # --- выбор темы ---
        self.lbl_theme = QLabel()
        self.lbl_theme.setFont(self.default_font)
        self.lbl_theme.setText('Тема:')
        self.lbl_theme.setMinimumSize(QSize(150, 50))
        self.lbl_theme.setObjectName('lbl_theme')

        self.cb_theme = QComboBox()
        self.cb_theme.setFont(self.default_font)
        self.cb_theme.setMinimumSize(QSize(100, 50))
        self.cb_theme_items = ['Dark', 'Light']
        self.cb_theme.addItems(self.cb_theme_items)
        self.cb_theme.setCurrentIndex(self.cb_theme_items.index(
            self.cfg_handler.cfg_reader.get('app')['theme']))
        self.cb_theme.setObjectName('cb_theme')

        self.hlayout_theme = QHBoxLayout()
        self.hlayout_theme.setContentsMargins(0, 0, 0, 0)
        self.hlayout_theme.setSpacing(0)
        self.hlayout_theme.addWidget(self.lbl_theme)
        self.hlayout_theme.addWidget(self.cb_theme)

        # --- выбор com порта ---
        self.lbl_com_port = QLabel()
        self.lbl_com_port.setFont(self.default_font)
        self.lbl_com_port.setText('COM порт:')
        self.lbl_com_port.setMinimumSize(QSize(150, 50))
        self.lbl_com_port.setObjectName('lbl_com_port')

        self.cb_com_port = QComboBox()
        self.cb_com_port.setFont(self.default_font)
        self.cb_com_port.setMinimumSize(QSize(100, 50))
        self.cb_com_port.addItems(SerialH.get_com_ports())
        self.cb_com_port.setCurrentIndex(SerialH.get_default_com_port())
        self.cb_com_port.setMaxVisibleItems(5)
        self.cb_com_port.setObjectName('cb_com_port')

        self.hlayout_com_port = QHBoxLayout()
        self.hlayout_com_port.setContentsMargins(0, 0, 0, 0)
        self.hlayout_com_port.setSpacing(0)
        self.hlayout_com_port.addWidget(self.lbl_com_port)
        self.hlayout_com_port.addWidget(self.cb_com_port)

        # --- выбор baud rate ---
        self.lbl_baud_rate = QLabel()
        self.lbl_baud_rate.setFont(self.default_font)
        self.lbl_baud_rate.setText('BAUD:')
        self.lbl_baud_rate.setMinimumSize(QSize(150, 50))
        self.lbl_baud_rate.setObjectName('lbl_baud_rate')

        self.cb_baud_rate = QComboBox()
        self.cb_baud_rate.setFont(self.default_font)
        self.cb_baud_rate.setMinimumSize(QSize(100, 50))
        self.cb_baud_rate.addItems(SerialH.get_baud_rates())
        self.cb_baud_rate.setCurrentIndex(SerialH.get_default_baud_rate())
        self.cb_baud_rate.setMaxVisibleItems(5)
        self.cb_baud_rate.setObjectName('cb_baud_rate')

        self.hlayout_baud_rate = QHBoxLayout()
        self.hlayout_baud_rate.setContentsMargins(0, 0, 0, 0)
        self.hlayout_baud_rate.setSpacing(0)
        self.hlayout_baud_rate.addWidget(self.lbl_baud_rate)
        self.hlayout_baud_rate.addWidget(self.cb_baud_rate)

        # --- использование весов ---
        self.chb_use_weights = QCheckBox()
        self.chb_use_weights.setFont(self.default_font)
        self.chb_use_weights.setText('Использовать весы?')
        self.chb_use_weights.setMinimumSize(QSize(250, 50))
        self.chb_use_weights.setChecked(
            self.cfg_handler.cfg_reader.get('weigher')['use_weigher'])
        self.chb_use_weights.setObjectName('chb_use_weights')
        self.chb_use_weights.stateChanged.connect(self._show_more_settings)

        # --- выбор com порта для весов ---
        self.lbl_weights_com_port = QLabel()
        self.lbl_weights_com_port.setFont(self.default_font)
        self.lbl_weights_com_port.setText('COM порт:')
        self.lbl_weights_com_port.setMinimumSize(QSize(150, 50))
        self.lbl_weights_com_port.setVisible(self.chb_use_weights.isChecked())
        self.lbl_weights_com_port.setObjectName('lbl_weights_com_port')

        self.cb_weights_com_port = QComboBox()
        self.cb_weights_com_port.setFont(self.default_font)
        self.cb_weights_com_port.setMinimumSize(QSize(100, 50))
        self.cb_weights_com_port.addItems(SerialH.get_com_ports())
        self.cb_weights_com_port.setCurrentIndex(
            SerialH.get_default_weigher_com_port())
        self.cb_weights_com_port.setVisible(self.chb_use_weights.isChecked())
        self.cb_weights_com_port.setObjectName('cb_weights_com_port')

        self.hlayout_weights_com_port = QHBoxLayout()
        self.hlayout_weights_com_port.setContentsMargins(0, 0, 0, 0)
        self.hlayout_weights_com_port.setSpacing(0)
        self.hlayout_weights_com_port.addWidget(self.lbl_weights_com_port)
        self.hlayout_weights_com_port.addWidget(self.cb_weights_com_port)

        # --- выбор baud rate для весов ---
        self.lbl_weights_baud_rate = QLabel()
        self.lbl_weights_baud_rate.setFont(self.default_font)
        self.lbl_weights_baud_rate.setText('BAUD:')
        self.lbl_weights_baud_rate.setMinimumSize(QSize(150, 50))
        self.lbl_weights_baud_rate.setVisible(self.chb_use_weights.isChecked())
        self.lbl_weights_baud_rate.setObjectName('lbl_weights_baud_rate')

        self.cb_weights_baud_rate = QComboBox()
        self.cb_weights_baud_rate.setFont(self.default_font)
        self.cb_weights_baud_rate.setMinimumSize(QSize(100, 50))
        self.cb_weights_baud_rate.addItems(SerialH.get_baud_rates())
        self.cb_weights_baud_rate.setCurrentIndex(
            SerialH.get_default_weigher_baud_rate())
        self.cb_weights_baud_rate.setVisible(self.chb_use_weights.isChecked())
        self.cb_weights_baud_rate.setObjectName('cb_weights_baud_rate')

        self.hlayout_weights_baud_rate = QHBoxLayout()
        self.hlayout_weights_baud_rate.setContentsMargins(0, 0, 0, 0)
        self.hlayout_weights_baud_rate.setSpacing(0)
        self.hlayout_weights_baud_rate.addWidget(self.lbl_weights_baud_rate)
        self.hlayout_weights_baud_rate.addWidget(self.cb_weights_baud_rate)

        # --- кнопка: сброс настроек ---
        self.btn_to_default = QPushButton()
        self.btn_to_default.setFont(self.default_font)
        self.btn_to_default.setText('Сбросить настройки')
        self.btn_to_default.setMinimumSize(QSize(250, 50))
        self.btn_to_default.setObjectName('btn_to_default')
        self.btn_to_default.clicked.connect(self._to_default_clicked)

        # --- вертикальный layout для параметров ---
        self.central_vlayout = QVBoxLayout(self.widget_central_area)
        self.central_vlayout.setContentsMargins(10, 10, 10, 10)
        self.central_vlayout.setSpacing(0)

        # --- вертикальный layout для параметров: зависимости ---
        self.central_vlayout.addLayout(self.hlayout_theme)
        self.central_vlayout.addLayout(self.hlayout_com_port)
        self.central_vlayout.addLayout(self.hlayout_baud_rate)
        self.central_vlayout.addWidget(self.chb_use_weights)
        self.central_vlayout.addLayout(self.hlayout_weights_com_port)
        self.central_vlayout.addLayout(self.hlayout_weights_baud_rate)
        self.central_vlayout.addWidget(self.btn_to_default)

        # --- кнопка: ок ---
        self.btn_ok = QPushButton()
        self.btn_ok.setFont(self.default_font)
        self.btn_ok.setText('ОК')
        self.btn_ok.setFixedSize(QSize(70, 30))
        self.btn_ok.setObjectName('btn_ok')
        self.btn_ok.clicked.connect(self._ok_clicked)

        # --- кнопка: отмена ---
        self.btn_cancel = QPushButton()
        self.btn_cancel.setFont(self.default_font)
        self.btn_cancel.setText('ОТМЕНА')
        self.btn_cancel.setFixedSize(QSize(70, 30))
        self.btn_cancel.setObjectName('btn_cancel')
        self.btn_cancel.clicked.connect(self._cancel_clicked)

        # --- кнопка: применить ---
        self.btn_apply = QPushButton()
        self.btn_apply.setFont(self.default_font)
        self.btn_apply.setText('ПРИМЕНИТЬ')
        self.btn_apply.setFixedSize(QSize(70, 30))
        self.btn_apply.setObjectName('btn_apply')
        self.btn_apply.clicked.connect(self._apply_clicked)

        # --- горизонтальный layout для кнопок ---
        self.buttons_hlayout = QHBoxLayout()
        self.buttons_hlayout.setContentsMargins(0, 0, 0, 0)
        self.buttons_hlayout.setSpacing(0)

        # --- горизонтальный layout для кнопок: зависимости ---
        self.buttons_hlayout.addWidget(self.btn_ok)
        self.buttons_hlayout.addWidget(self.btn_cancel)
        self.buttons_hlayout.addWidget(self.btn_apply)

        # --- вертикальный layout для всего окна ---
        self.general_vlayout = QVBoxLayout(self)
        self.general_vlayout.setContentsMargins(0, 0, 0, 0)
        self.general_vlayout.setSpacing(0)

        # --- вертикальный layout для всего окна: зависимости ---
        self.general_vlayout.addWidget(self.widget_top_bar_frame)
        self.general_vlayout.addWidget(self.widget_central_area)
        self.general_vlayout.addLayout(self.buttons_hlayout)

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
                    self.widget_top_bar_frame.geometry().height()
                    ):
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

    def _show_more_settings(self):
        self.check_state = self.chb_use_weights.isChecked()
        self.lbl_weights_com_port.setVisible(self.check_state)
        self.cb_weights_com_port.setVisible(self.check_state)
        self.lbl_weights_baud_rate.setVisible(self.check_state)
        self.cb_weights_baud_rate.setVisible(self.check_state)

    def _ok_clicked(self):
        self.close()

    def _cancel_clicked(self):
        cfg_data = self.cfg_handler.cfg_reader.fetch()

        self.cb_theme.setCurrentText(cfg_data['app']['theme'])
        self.cb_com_port.setCurrentText(cfg_data['serial']['COM'])
        self.cb_baud_rate.setCurrentText(str(cfg_data['serial']['BAUD']))
        self.cb_weights_com_port.setCurrentText(cfg_data['weigher']['COM'])
        self.cb_weights_baud_rate.setCurrentText(str(cfg_data['weigher']['BAUD']))

    def _apply_clicked(self):
        theme = self.cb_theme.currentText()
        com_port = self.cb_com_port.currentText()
        baud_rate = self.cb_baud_rate.currentText()
        use_weights = self.chb_use_weights.isChecked()
        weights_com_port = self.cb_weights_com_port.currentText()
        weights_baud_rate = self.cb_weights_baud_rate.currentText()

        self.cfg_handler.cfg_reader.set('app', {'theme': theme})
        self.cfg_handler.cfg_reader.set('serial', {'COM': com_port, 
                                        'BAUD': baud_rate})
        self.cfg_handler.cfg_reader.set('weigher', {'use_weigher': use_weights, 
                                         'COM': weights_com_port, 
                                         'BAUD': weights_baud_rate})

    def _to_default_clicked(self):
        self.answer = QMessageBox.question(self, 
            'Внимание!', 'Вы действительно хотите сбросить настройки?', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if self.answer == QMessageBox.Yes:
            self.cfg_handler.set_default()
            self.close()
