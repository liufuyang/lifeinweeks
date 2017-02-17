from configparser import ConfigParser, ExtendedInterpolation
import os

class ConfigEvnParser:
    """
    ConfigEvnParser is a class used to read configs from config files and environment variables.
    The default config path is at './config/config.properties'
    and to change the default path one can change the environment variable via:
        export CONFIG_FILE_PATH=your/new/config/file/path/config.properties
    Note that as we use the python package called configparser, it can only handle INI format of config.
    Thus, you need to add a session name '[DEFAULT]' at the beginning of each config file.
    """

    DEFAULT_SECTION_NAME = 'DEFAULT'
    CONFIG_FILE_PATH_NAME = 'CONFIG_FILE_PATH'

    def __init__(self, config_file_path='./config/config.properties'):

        self.config = {}

        # universal parser, which include all env vars, used for interpolation config files
        interpolateParser = ConfigParser(os.environ, allow_no_value=True, interpolation=ExtendedInterpolation())
        interpolateParser.read(config_file_path)
        newConfigFilePath = os.environ.get(self.CONFIG_FILE_PATH_NAME, config_file_path)
        interpolateParser.read(newConfigFilePath)

        # use rawParser to get only the keys specified in the config files, so that we only generate the configs specified in config files
        rawParser = ConfigParser(allow_no_value=True)
        rawParser.read(config_file_path)
        rawParser.read(newConfigFilePath)

        # Override with env var:
        for key in rawParser[self.DEFAULT_SECTION_NAME]:
            envValue = os.environ.get(key.upper(), None)
            if envValue is not None:
                interpolateParser.set(self.DEFAULT_SECTION_NAME, key, envValue)
            self.set(key, interpolateParser.get(self.DEFAULT_SECTION_NAME, key))

    def set(self, key, value):
        self.config[key.upper()] = str(value)

    def get(self, key):
        return self.config[key.upper()]

    def get_bool(self, key):
        return self._str2bool((self.config[key.upper()]))

    def get_int(self, key):
        return int(self.config[key.upper()])

    def _str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")