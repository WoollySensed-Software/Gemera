from PySide6.QtSerialPort import QSerialPortInfo

from settings import CFG_PATH
from bin.handlers.ConfigurationFile import ConfigurationFileH


class SerialH:

    @staticmethod
    def get_com_ports() -> list:
        return [el.portName() for el in QSerialPortInfo.availablePorts()]
    
    @staticmethod
    def get_baud_rates() -> list:
        return [str(el) for el in QSerialPortInfo.standardBaudRates()]
    
    @staticmethod
    def get_default_com_port() -> int:
        cfg = ConfigurationFileH(CFG_PATH, use_exists_check=False)
        cfg.exists()
        data = cfg.get('serial')['COM']
        return SerialH.get_com_ports().index(str(data))
    
    @staticmethod
    def get_default_baud_rate() -> int:
        cfg = ConfigurationFileH(CFG_PATH, use_exists_check=False)
        cfg.exists()
        data = cfg.get('serial')['BAUD']
        return SerialH.get_baud_rates().index(str(data))
    
    @staticmethod
    def get_default_weighers_com_port() -> int:
        cfg = ConfigurationFileH(CFG_PATH, use_exists_check=False)
        cfg.exists()
        data = cfg.get('weighers')['COM']
        return SerialH.get_com_ports().index(str(data))
    
    @staticmethod
    def get_default_weighers_baud_rate() -> int:
        cfg = ConfigurationFileH(CFG_PATH, use_exists_check=False)
        cfg.exists()
        data = cfg.get('weighers')['BAUD']
        return SerialH.get_baud_rates().index(str(data))
