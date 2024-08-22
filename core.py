"""
Python 3.12.0
PySide6 6.7.2
utf-8
"""

from sys import argv, exit

from PySide6.QtWidgets import QApplication

from bin.ui.BootLoader import BootLoaderUI
from settings import (__version__, __app_name__, __author__, 
                      CFG_PATH, INCLUDES)


def main():
    app = QApplication(argv)
    app.setApplicationVersion(__version__)
    app.setApplicationName(__app_name__)
    app.setOrganizationName(__author__)

    boot_loader = BootLoaderUI(CFG_PATH, INCLUDES)
    boot_loader.setup_ui()
    boot_loader.show()

    exit(app.exec())


if __name__ == '__main__':
    main()
