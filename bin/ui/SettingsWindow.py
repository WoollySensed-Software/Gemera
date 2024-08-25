from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QComboBox, 
    QCheckBox, QMessageBox
)
from PySide6.QtGui import QCursor, QFont
from PySide6.QtCore import Qt, QSize

from settings import CFG_PATH
from bin.ui.styles import SETTINGS_WINDOW
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.handlers.Serial import SerialH


class SettingsWindowUI(QWidget):

    def __init__(self, btn_weighers_menu: QPushButton):
        super().__init__()
        self.btn_weighers_menu = btn_weighers_menu
        self.old_pos = None
        self.default_font = QFont('Sans Serif', 16)
        self.cfg_handler = ConfigurationFileH(CFG_PATH)
    
    def setup_ui(self):
        # --- настройки окна ---
        self.setWindowTitle('Настройки')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.WindowStaysOnTopHint)
        self.setMinimumSize(QSize(350, 470))
        self.setStyleSheet(SETTINGS_WINDOW)
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
        self.lbl_theme.setObjectName('labels_name')

        self.cb_theme = QComboBox()
        self.cb_theme.setFont(self.default_font)
        self.cb_theme.setMinimumSize(QSize(100, 50))
        self.cb_theme_items = ['Dark', 'Light']
        self.cb_theme.addItems(self.cb_theme_items)
        self.cb_theme.setCurrentIndex(self.cb_theme_items.index(
            self.cfg_handler.get('app')['theme']))
        self.cb_theme.setObjectName('comboboxes')

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
        self.lbl_com_port.setObjectName('labels_name')

        self.cb_com_port = QComboBox()
        self.cb_com_port.setFont(self.default_font)
        self.cb_com_port.setMinimumSize(QSize(100, 50))
        self.cb_com_port.addItems(SerialH.get_com_ports())
        self.cb_com_port.setCurrentIndex(SerialH.get_default_com_port())
        self.cb_com_port.setMaxVisibleItems(5)
        self.cb_com_port.setObjectName('comboboxes')

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
        self.lbl_baud_rate.setObjectName('labels_name')

        self.cb_baud_rate = QComboBox()
        self.cb_baud_rate.setFont(self.default_font)
        self.cb_baud_rate.setMinimumSize(QSize(100, 50))
        self.cb_baud_rate.addItems(SerialH.get_baud_rates())
        self.cb_baud_rate.setCurrentIndex(SerialH.get_default_baud_rate())
        self.cb_baud_rate.setMaxVisibleItems(5)
        self.cb_baud_rate.setObjectName('comboboxes')

        self.hlayout_baud_rate = QHBoxLayout()
        self.hlayout_baud_rate.setContentsMargins(0, 0, 0, 0)
        self.hlayout_baud_rate.setSpacing(0)
        self.hlayout_baud_rate.addWidget(self.lbl_baud_rate)
        self.hlayout_baud_rate.addWidget(self.cb_baud_rate)

        # --- использование весов ---
        self.chb_use_weighers = QCheckBox()
        self.chb_use_weighers.setFont(self.default_font)
        self.chb_use_weighers.setText('Использовать весы?')
        self.chb_use_weighers.setMinimumSize(QSize(250, 50))
        self.chb_use_weighers.setChecked(self.cfg_handler.get('weighers')['use_weighers'])
        self.chb_use_weighers.setObjectName('chb_use_weighers')
        self.chb_use_weighers.stateChanged.connect(self._show_more_settings)

        # --- выбор com порта для весов ---
        self.lbl_weighers_com_port = QLabel()
        self.lbl_weighers_com_port.setFont(self.default_font)
        self.lbl_weighers_com_port.setText('COM порт:')
        self.lbl_weighers_com_port.setMinimumSize(QSize(150, 50))
        self.lbl_weighers_com_port.setEnabled(self.chb_use_weighers.isChecked())
        self.lbl_weighers_com_port.setObjectName('labels_name')

        self.cb_weighers_com_port = QComboBox()
        self.cb_weighers_com_port.setFont(self.default_font)
        self.cb_weighers_com_port.setMinimumSize(QSize(100, 50))
        self.cb_weighers_com_port.addItems(SerialH.get_com_ports())
        self.cb_weighers_com_port.setCurrentIndex(
            SerialH.get_default_weighers_com_port())
        self.cb_weighers_com_port.setEnabled(self.chb_use_weighers.isChecked())
        self.cb_weighers_com_port.setObjectName('comboboxes')

        self.hlayout_weighers_com_port = QHBoxLayout()
        self.hlayout_weighers_com_port.setContentsMargins(0, 0, 0, 0)
        self.hlayout_weighers_com_port.setSpacing(0)
        self.hlayout_weighers_com_port.addWidget(self.lbl_weighers_com_port)
        self.hlayout_weighers_com_port.addWidget(self.cb_weighers_com_port)

        # --- выбор baud rate для весов ---
        self.lbl_weighers_baud_rate = QLabel()
        self.lbl_weighers_baud_rate.setFont(self.default_font)
        self.lbl_weighers_baud_rate.setText('BAUD:')
        self.lbl_weighers_baud_rate.setMinimumSize(QSize(150, 50))
        self.lbl_weighers_baud_rate.setEnabled(self.chb_use_weighers.isChecked())
        self.lbl_weighers_baud_rate.setObjectName('labels_name')

        self.cb_weighers_baud_rate = QComboBox()
        self.cb_weighers_baud_rate.setFont(self.default_font)
        self.cb_weighers_baud_rate.setMinimumSize(QSize(100, 50))
        self.cb_weighers_baud_rate.addItems(SerialH.get_baud_rates())
        self.cb_weighers_baud_rate.setCurrentIndex(
            SerialH.get_default_weighers_baud_rate())
        self.cb_weighers_baud_rate.setEnabled(self.chb_use_weighers.isChecked())
        self.cb_weighers_baud_rate.setMaxVisibleItems(5)
        self.cb_weighers_baud_rate.setObjectName('comboboxes')

        self.hlayout_weighers_baud_rate = QHBoxLayout()
        self.hlayout_weighers_baud_rate.setContentsMargins(0, 0, 0, 0)
        self.hlayout_weighers_baud_rate.setSpacing(0)
        self.hlayout_weighers_baud_rate.addWidget(self.lbl_weighers_baud_rate)
        self.hlayout_weighers_baud_rate.addWidget(self.cb_weighers_baud_rate)

        # --- кнопка: сброс настроек ---
        self.btn_to_default = QPushButton()
        self.btn_to_default.setFont(self.default_font)
        self.btn_to_default.setText('Сбросить настройки')
        self.btn_to_default.setMinimumSize(QSize(250, 30))
        self.btn_to_default.setObjectName('btn_to_default')
        self.btn_to_default.clicked.connect(self._to_default_clicked)

        # --- вертикальный layout для параметров ---
        self.central_vlayout = QVBoxLayout(self.widget_central_area)
        self.central_vlayout.setContentsMargins(10, 10, 10, 10)
        self.central_vlayout.setSpacing(5)

        # --- вертикальный layout для параметров: зависимости ---
        self.central_vlayout.addLayout(self.hlayout_theme)
        self.central_vlayout.addLayout(self.hlayout_com_port)
        self.central_vlayout.addLayout(self.hlayout_baud_rate)
        self.central_vlayout.addWidget(self.chb_use_weighers)
        self.central_vlayout.addLayout(self.hlayout_weighers_com_port)
        self.central_vlayout.addLayout(self.hlayout_weighers_baud_rate)
        self.central_vlayout.addWidget(self.btn_to_default)

        # --- кнопка: ок ---
        self.btn_ok = QPushButton()
        self.btn_ok.setFont(self.default_font)
        self.btn_ok.setText('Ок')
        self.btn_ok.setFixedSize(QSize(50, 30))
        self.btn_ok.setObjectName('buttons')
        self.btn_ok.clicked.connect(self._ok_clicked)

        # --- кнопка: отмена ---
        self.btn_cancel = QPushButton()
        self.btn_cancel.setFont(self.default_font)
        self.btn_cancel.setText('Отмена')
        self.btn_cancel.setFixedSize(QSize(100, 30))
        self.btn_cancel.setObjectName('buttons')
        self.btn_cancel.clicked.connect(self._cancel_clicked)

        # --- кнопка: применить ---
        self.btn_apply = QPushButton()
        self.btn_apply.setFont(self.default_font)
        self.btn_apply.setText('Применить')
        self.btn_apply.setFixedSize(QSize(150, 30))
        self.btn_apply.setObjectName('buttons')
        self.btn_apply.clicked.connect(self._apply_clicked)

        # --- горизонтальный layout для кнопок ---
        self.buttons_hlayout = QHBoxLayout()
        self.buttons_hlayout.setContentsMargins(0, 0, 0, 10)
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

    def _show_more_settings(self):
        self.check_state = self.chb_use_weighers.isChecked()

        self.lbl_weighers_com_port.setEnabled(self.check_state)
        self.cb_weighers_com_port.setEnabled(self.check_state)
        self.lbl_weighers_baud_rate.setEnabled(self.check_state)
        self.cb_weighers_baud_rate.setEnabled(self.check_state)
        self.btn_weighers_menu.setEnabled(self.check_state)

        if not self.check_state:
            self.lbl_weighers_com_port.setStyleSheet('[enabled="false"]{color: gray;}')
            self.cb_weighers_com_port.setStyleSheet('[enabled="false"]{color: gray;}')
            self.lbl_weighers_baud_rate.setStyleSheet('[enabled="false"]{color: gray;}')
            self.cb_weighers_baud_rate.setStyleSheet('[enabled="false"]{color: gray;}')

            self.btn_weighers_menu.setStyleSheet('[enabled="false"]{color: gray;}')
        else:
            self.lbl_weighers_com_port.setStyleSheet('[enabled="true"]{color: white;}')
            self.cb_weighers_com_port.setStyleSheet('[enabled="true"]{color: white;}')
            self.lbl_weighers_baud_rate.setStyleSheet('[enabled="true"]{color: white;}')
            self.cb_weighers_baud_rate.setStyleSheet('[enabled="true"]{color: white;}')

            self.btn_weighers_menu.setStyleSheet('[enabled="true"]{color: red;}')

    def _ok_clicked(self):
        self.close()

    def _cancel_clicked(self):
        cfg_data = self.cfg_handler.fetch()

        self.chb_use_weighers.setChecked(cfg_data['weighers']['use_weighers'])
        self.cb_theme.setCurrentText(cfg_data['app']['theme'])
        self.cb_com_port.setCurrentText(cfg_data['serial']['COM'])
        self.cb_baud_rate.setCurrentText(str(cfg_data['serial']['BAUD']))
        self.cb_weighers_com_port.setCurrentText(cfg_data['weighers']['COM'])
        self.cb_weighers_baud_rate.setCurrentText(str(cfg_data['weighers']['BAUD']))

    def _apply_clicked(self):
        theme = self.cb_theme.currentText()
        com_port = self.cb_com_port.currentText()
        baud_rate = self.cb_baud_rate.currentText()
        use_weighers = self.chb_use_weighers.isChecked()
        weighers_com_port = self.cb_weighers_com_port.currentText()
        weighers_baud_rate = self.cb_weighers_baud_rate.currentText()

        self.cfg_handler.set('app', {'theme': theme})
        self.cfg_handler.set('serial', {'COM': com_port, 
                                        'BAUD': baud_rate})
        self.cfg_handler.set('weighers', {'use_weighers': use_weighers, 
                                         'COM': weighers_com_port, 
                                         'BAUD': weighers_baud_rate})

    def _to_default_clicked(self):
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle('Внимание!')
        self.msg.setFont(self.default_font)
        self.msg.setText('Вы действительно хотите сбросить настройки?')

        self.btn_aceptar = self.msg.addButton('ДА', QMessageBox.YesRole)
        self.btn_aceptar.setFixedSize(QSize(100, 30))
        self.btn_cancelar = self.msg.addButton('НЕТ', QMessageBox.NoRole)
        self.btn_cancelar.setFixedSize(QSize(100, 30))

        self.msg.setDefaultButton(self.btn_cancelar)
        self.msg.exec()
        
        if self.msg.clickedButton() == self.btn_aceptar:
            self.cfg_handler.set_default()
            self.close()
