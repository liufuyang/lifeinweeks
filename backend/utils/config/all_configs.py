from utils.config.config_env_parser import ConfigEvnParser

config = ConfigEvnParser()


class Config:
    DEBUG = config.get_bool('DEBUG')
    SECRET_KEY = config.get('SECRET_KEY')
    LOGGING_FILENAME = config.get('LOGGING_FILENAME')
    LOGGING_DEBUG_LEVEL = config.get('LOGGING_DEBUG_LEVEL')

    DB_HOST=config.get('DB_HOST')
    DB_PORT=config.get_int('DB_PORT')
    DB_USER=config.get('DB_USER')
    DB_PASS=config.get('DB_PASS')
    DB_NAME=config.get('DB_NAME')
