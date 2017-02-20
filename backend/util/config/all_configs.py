from utils.config.config_env_parser import ConfigEvnParser

config = ConfigEvnParser()

class Config:
    LOGGING_FILENAME = config.get('LOGGING_FILENAME')