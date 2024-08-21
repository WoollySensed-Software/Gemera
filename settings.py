import os

from pathlib import Path


__version__ = '1.0.0'  # global.major.minor
__app_name__ = 'Gemera'
__author__ = 'WoollySensed Software'

DEBUG = True
ROOT_DIR = Path(os.getcwd()).resolve()  # корневая директория проекта
CFG_PATH = Path(f'{ROOT_DIR}/cfg/config.cfg').resolve()

# Необходимые файлы проекта
middle_path = 'bin/resources' if DEBUG else 'resources'
INCLUDES = {
    'app.ico': [
        Path(f'{ROOT_DIR}/{middle_path}/app.ico').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ]
}
# Файл конфигурации по умолчанию
DEFAULT_CFG = {
    'serial': {
        'COM': 'COM1', 
        'BAUD': 9600
    }, 
    'app': {
        'theme': 'Dark'
    }, 
    'weigher': {
        'use_weigher': False, 
        'COM': 'COM1', 
        'BAUD': 115200
    }, 
    'graph': {
        'background': 'white', 
        'foreground': 'black', 
        'name': 'Line', 
        'pen': 'r'
    }
}
