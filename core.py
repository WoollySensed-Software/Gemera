"""
Python 3.12.0
PySide6 6.7.2
utf-8
"""

from sys import argv, exit
try:
    from ctypes import windll
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError: pass

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from bin.ui.BootLoader import BootLoaderUI
from settings import (__version__, __app_name__, __author__, 
                      CFG_PATH, INCLUDES)


def main():
    with open('bin/ui/styles.qss', 'r') as f:
        styles = f.read()

    app = QApplication(argv)
    app.setApplicationVersion(__version__)
    app.setApplicationName(__app_name__)
    app.setOrganizationName(__author__)
    app.setWindowIcon(QIcon(f'{INCLUDES['app.ico'][0]}'.replace('\\', '/')))
    app.setStyleSheet(styles)

    boot_loader = BootLoaderUI(CFG_PATH, INCLUDES)
    boot_loader.setup_ui()
    boot_loader.show()

    exit(app.exec())


if __name__ == '__main__':
    main()
