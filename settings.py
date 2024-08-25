import os

from pathlib import Path


__version__ = '1.6.0'  # global.major.minor
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
    ], 
    'close.png': [
        Path(f'{ROOT_DIR}/{middle_path}/close.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ], 
    'fullscreen.png': [
        Path(f'{ROOT_DIR}/{middle_path}/fullscreen.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ], 
    'gear.png': [
        Path(f'{ROOT_DIR}/{middle_path}/gear.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ], 
    'minus.png': [
        Path(f'{ROOT_DIR}/{middle_path}/minus.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ], 
    'switch-off.png': [
        Path(f'{ROOT_DIR}/{middle_path}/switch-off.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ], 
    'switch-on.png': [
        Path(f'{ROOT_DIR}/{middle_path}/switch-on.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve()
    ]
}
# Файл конфигурации по умолчанию
DEFAULT_CFG = {
    'app': {
        'theme': 'Dark', 
        'display_w': 640, 
        'display_h': 740
    }, 
    'serial': {
        'COM': 'COM1', 
        'BAUD': 9600
    }, 
    'weighers': {
        'use_weighers': False, 
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
