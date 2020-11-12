import os.path
import configparser

CONFIGURATION_FILE_NAME = 'configuration.ini'


def get_config_value(group: str, key: str) -> str:
    configuration = configparser.ConfigParser()
    configuration.read(CONFIGURATION_FILE_NAME)

    return configuration[group][key]


def check_file_exists(file_name) -> str:
    if os.path.isfile(file_name):
        return file_name
    else:
        raise FileNotFoundError(file_name)
