from sys import exit
from pathlib import Path

from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton
from PySide6.QtCore import Qt, QSize, QRect, QTimer
from PySide6.QtGui import QFont

from bin.handlers.types import *
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.ui.MainWindow import MainWindowUI
from bin.ui.styles import BOOT_LOADER


class BootLoaderUI(QWidget):

    def __init__(self, cfg_path: Path, includes: Includes, /):
        super().__init__()
        self.cfg_path = cfg_path
        self.includes = includes
        self.default_font = QFont('Sans Serif', 16)
        self.spec_font = QFont('Sans Serif', 12)
        self.cfg_handler = ConfigurationFileH(self.cfg_path)
    
    def setup_ui(self):
        self.setFixedSize(QSize(600, 300))
        self.setWindowOpacity(0.8)  # прозрачность окна
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet(BOOT_LOADER)
        self.setObjectName('BootLoaderUI')

        self.ted_processing = QTextEdit(self)
        self.ted_processing.setGeometry(QRect(5, 5, 590, 260))
        self.ted_processing.setFont(self.default_font)
        self.ted_processing.insertPlainText(
            'Проверяем целостность программы перед запуском...'
        )
        self.ted_processing.setReadOnly(True)
        self.ted_processing.setObjectName('ted_processing')

        self.btn_exit = QPushButton(self)
        self.btn_exit.setGeometry(QRect(5, 265, 590, 30))
        self.btn_exit.setFont(self.default_font)
        self.btn_exit.setText('Закрыть приложение'.upper())
        self.btn_exit.setObjectName('btn_exit')
        self.btn_exit.hide()
        self.btn_exit.clicked.connect(exit)

        # Нужно для корректной работы программы
        if self._check_program_structure():
            QTimer.singleShot(0, self._open_main_window)

    def _check_program_structure(self) -> bool:
        self.cfg_handler.exists()  # создаст файл cfg, если его не существует

        errors = []
        for file, path in self.includes.items():
            self.ted_processing.insertPlainText(f'\nПроверяем наличие: {file}')

            if not path[0].exists():
                self.ted_processing.insertPlainText('\tОшибка!')
                errors.append(f'Файл {file} отсутствует в директории: {path[1]}')
            else: self.ted_processing.insertPlainText('\tУспех!')

        if errors:
            self.btn_exit.show()
            self.ted_processing.insertPlainText('\n\nОшибки:')

            for error, i in zip(errors, range(1, len(errors)+1)):
                self.ted_processing.insertPlainText(f'\n{i}. {error}')

            return False

        return True

    def _open_main_window(self):
        self.main_win = MainWindowUI()
        self.main_win.setup_ui()
        self.main_win.show()
        self.close()
