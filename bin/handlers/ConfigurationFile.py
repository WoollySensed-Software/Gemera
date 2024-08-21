import toml

from pathlib import Path
from WSS_ToolKit.WConfigUtils import ConfigUtils as cu

from settings import DEFAULT_CFG


class ConfigurationFileH:

    def __init__(self, cfg_path: Path, /):
        self.cfg_path = cfg_path
        self.cfg_reader = cu.BaseConfig(self.cfg_path, use_exists_check=False).activate
    
    def exists(self):
        is_dir = self.cfg_path.parent.is_dir()
        is_file = self.cfg_path.is_file()

        if is_dir:
            if not is_file: self.set_default()
        else:
            self.cfg_path.parent.mkdir(parents=True)
            self.set_default()

    def set_default(self):
        with open(self.cfg_path, 'w', encoding='utf-8') as file:
            toml.dump(DEFAULT_CFG, file)


# class ConfigurationFileH:

#     def __init__(self, cfg_path: Path, /):
#         self.cfg_path = cfg_path

#     @property
#     def exists(self):
#         is_dir = self.cfg_path.parent.is_dir()
#         is_file = self.cfg_path.is_file()

#         if is_dir:
#             if not is_file: self.set_default()
#         else:
#             self.cfg_path.parent.mkdir(parents=True)
#             self.set_default()
    
#     def set_default(self) -> Nothing:
#         with open(self.cfg_path, 'w', encoding='utf-8') as file:
#             toml.dump(DEFAULT_CFG, file)
    
#     def get(self, section: SectionOptions | None = None) -> ConfigResponse:

#         if not isinstance(section, (str, list, tuple)) and section is not None:
#             raise TypeError(f'section must be str, list or tuple, not {type(section)}')

#         with open(self.cfg_path, 'r', encoding='utf-8') as file:
#             config = toml.load(file)

#             if section is None:
#                 return config
#             elif isinstance(section, str):
#                 return config[section]
#             else: return [config[k] for k in section]
    
#     def set(self, section: str, key_value: dict[str, Any]) -> Nothing:
#         if not isinstance(section, str):
#             raise TypeError(f'section must be str, not {type(section)}')

#         if not isinstance(key_value, dict):
#             raise TypeError(f'key_value must be dict, not {type(key_value)}')
        
#         with open(self.cfg_path, 'r', encoding='utf-8') as file:
#             config = toml.load(file)

#             if config in config.keys():
#                 config[section].update(key_value)
#             else: config[section] = key_value
        
#         with open(self.cfg_path, 'w', encoding='utf-8') as file:
#             toml.dump(config, file)
