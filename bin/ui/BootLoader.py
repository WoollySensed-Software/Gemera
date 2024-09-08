from sys import exit
from pathlib import Path

from PySide6.QtWidgets import (
    QWidget, QTextEdit, QPushButton, 
    QVBoxLayout, QApplication
)
from PySide6.QtCore import (
    Qt, QSize, QTimer, 
    QPoint
)
from PySide6.QtGui import QFont

from bin.handlers.types import *
from bin.handlers.ConfigurationFile import ConfigurationFileH
from bin.ui.MainWindow import MainWindowUI


class BootLoaderUI(QWidget):

    def __init__(self, cfg_path: Path, includes: Includes, /, app: QApplication):
        super().__init__()
        self.app = app
        self.cfg_path = cfg_path
        self.includes = includes
        self.default_font = QFont('Sans Serif', 16)
        self.cfg_handler = ConfigurationFileH(self.cfg_path, use_exists_check=False)
    
    def setup_ui(self):
        # --- настройка окна ---
        self.setWindowOpacity(0.8)  # прозрачность окна
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                            Qt.WindowType.WindowStaysOnTopHint)
        self.setMinimumSize(QSize(640, 300))
        self.setObjectName('BootLoaderUI')

        # --- вывод состояния проверок ---
        self.ted_processing = QTextEdit()
        self.ted_processing.setMinimumSize(QSize(590, 260))
        self.ted_processing.setFont(self.default_font)
        self.ted_processing.insertPlainText(
            'Проверяем целостность программы перед запуском...'
        )
        self.ted_processing.setReadOnly(True)
        self.ted_processing.setObjectName('Processing')

        # --- кнопка выхода ---
        self.btn_exit = QPushButton()
        self.btn_exit.setMinimumSize(QSize(590, 30))
        self.btn_exit.setFont(self.default_font)
        self.btn_exit.setText('Закрыть приложение'.upper())
        self.btn_exit.setObjectName('BtnExit')
        self.btn_exit.hide()
        self.btn_exit.clicked.connect(exit)

        # --- вертикальный layout для всего окна ---
        self.general_vlayout = QVBoxLayout(self)
        self.general_vlayout.setContentsMargins(10, 10, 10, 10)
        self.general_vlayout.addSpacing(10)

        # --- вертикальный layout для всего окна: зависимости ---
        self.general_vlayout.addWidget(self.ted_processing)
        self.general_vlayout.addWidget(self.btn_exit)

        self.move(self.screen().availableGeometry().center() - 
                  QPoint(self.width() // 2, self.height() // 2))

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
        self.main_win = MainWindowUI(self.app)
        self.main_win.setup_ui()
        self.main_win.show()
        self.close()
