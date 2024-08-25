import os

from pathlib import Path


__version__ = '1.6.1'  # global.major.minor
__app_name__ = 'Gemera'
__author__ = 'WoollySensed Software'

ROOT_DIR = Path(os.getcwd()).resolve()  # корневая директория проекта
CFG_PATH = Path(f'{ROOT_DIR}/cfg/config.cfg').resolve()

# Необходимые файлы проекта
middle_path = 'bin/resources'
INCLUDES = {
    'app.ico': [
        Path(f'{ROOT_DIR}/{middle_path}/app.ico').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/app.ico'
    ], 
    'close.png': [
        Path(f'{ROOT_DIR}/{middle_path}/close.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/close.png'
    ], 
    'fullscreen.png': [
        Path(f'{ROOT_DIR}/{middle_path}/fullscreen.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/fullscreen.png'
    ], 
    'gear.png': [
        Path(f'{ROOT_DIR}/{middle_path}/gear.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/gear.png'
    ], 
    'minus.png': [
        Path(f'{ROOT_DIR}/{middle_path}/minus.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/minus.png'
    ], 
    'switch-off.png': [
        Path(f'{ROOT_DIR}/{middle_path}/switch-off.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/switch-off.png'
    ], 
    'switch-on.png': [
        Path(f'{ROOT_DIR}/{middle_path}/switch-on.png').resolve(), 
        Path(f'{ROOT_DIR}/{middle_path}').resolve(), 
        f'{middle_path}/switch-on.png'
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
