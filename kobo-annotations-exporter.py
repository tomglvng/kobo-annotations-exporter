import argparse
from utils import check_file_exists
from messages import *
from services.exporter_service import ExporterService


def main() -> None:
    try:
        parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)
        parser.add_argument('sqlite', help=ARGUMENT_SQLITE_HELP, type=check_file_exists)
        args = parser.parse_args()

        exporter = ExporterService(args.sqlite)
        exporter.export_annotations()

    except FileNotFoundError as not_found:
        print("File '{}' not found".format(not_found))
        exit()


if __name__ == "__main__":
    main()
