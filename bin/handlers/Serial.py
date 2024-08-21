from PySide6.QtSerialPort import QSerialPortInfo

from settings import CFG_PATH, DEFAULT_CFG
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
        cfg = ConfigurationFileH(CFG_PATH)
        cfg.exists()
        data = cfg.cfg_reader.get('serial')['COM']
        return SerialH.get_com_ports().index(str(data))
    
    @staticmethod
    def get_default_baud_rate() -> int:
        cfg = ConfigurationFileH(CFG_PATH)
        cfg.exists()
        data = cfg.cfg_reader.get('serial')['BAUD']
        return SerialH.get_baud_rates().index(str(data))
    
    @staticmethod
    def get_default_weigher_com_port() -> int:
        cfg = ConfigurationFileH(CFG_PATH)
        cfg.exists()
        data = cfg.cfg_reader.get('weigher')['COM']
        return SerialH.get_com_ports().index(str(data))
    
    @staticmethod
    def get_default_weigher_baud_rate() -> int:
        cfg = ConfigurationFileH(CFG_PATH)
        cfg.exists()
        data = cfg.cfg_reader.get('weigher')['BAUD']
        return SerialH.get_baud_rates().index(str(data))
