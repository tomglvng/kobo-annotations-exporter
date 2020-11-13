import argparse
import os.path
from services.annotation_handler import AnnotationHandler


def check_file_existence(file_name: str) -> str:
    if not os.path.isfile(file_name):
        raise FileNotFoundError(file_name)
    return file_name


def check_folder_existence(directory_name: str) -> str:
    if not os.path.isdir(directory_name):
        raise NotADirectoryError(directory_name)
    return directory_name if directory_name[-1] != '/' else directory_name[:-1]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export annotations from Kobo sqlite database",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    try:
        parser.add_argument('sqlite',
                            type=check_file_existence,
                            help="Define the sqlite file location")
        parser.add_argument('--format',
                            '-f',
                            type=str,
                            choices={"console", "word", "text"},
                            default="console",
                            help="Specify the export format")
        parser.add_argument('--directory',
                            '-d',
                            type=check_folder_existence,
                            default="exports",
                            help="Specify the export directory", )

        args = parser.parse_args()
        annotation_handler = AnnotationHandler(args.sqlite, args.format, args.directory)
        annotation_handler.handle()

    except FileNotFoundError as not_found:
        print("File '{}' not found".format(not_found))

    except NotADirectoryError as not_found:
        print("Directory '{}' does not exist".format(not_found))


if __name__ == "__main__":
    main()
