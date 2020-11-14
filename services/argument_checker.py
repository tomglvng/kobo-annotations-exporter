import os.path
from dateutil import parser
from datetime import datetime
import argparse


def check_file_existence(file_name) -> str:
    if not os.path.isfile(file_name):
        raise argparse.ArgumentTypeError("file '{}' not found".format(file_name))
    return file_name


def check_folder_existence(directory_name: str) -> str:
    if not os.path.isdir(directory_name):
        raise argparse.ArgumentTypeError("directory '{}' does not exist".format(directory_name))
    return directory_name if directory_name[-1] != '/' else directory_name[:-1]


def check_date(date: str) -> datetime:
    try:
        parsed_date = parser.parse(date)
    except ValueError as value_error:
        raise argparse.ArgumentTypeError(
            "date '{}' is invalid ({})".format(date, value_error))
    return parsed_date
