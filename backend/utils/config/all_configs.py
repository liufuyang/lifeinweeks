from utils.config.config_env_parser import ConfigEvnParser

config = ConfigEvnParser()


class Config:
    DEBUG = config.get_bool('DEBUG')
    SECRET_KEY = config.get('SECRET_KEY')
    LOGGING_FILENAME = config.get('LOGGING_FILENAME')
    LOGGING_DEBUG_LEVEL = config.get('LOGGING_DEBUG_LEVEL')
