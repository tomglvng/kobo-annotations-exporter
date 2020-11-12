from constants.messages import *
from services.annotation_handler import AnnotationHandler
from services.checkers import check_folder_exists
from services.checkers import check_file_exists
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)
    try:
        parser.add_argument('sqlite', help=ARGUMENT_SQLITE_HELP, type=check_file_exists)
        parser.add_argument('-d', '--directory', help=DIRECTORY_HELP, type=check_folder_exists)
        parser.add_argument('-w', '--word', help=WORD_HELP, action="store_const", const="word")
        args = parser.parse_args()

        annotation_handler = AnnotationHandler(args.sqlite, args.word, args.directory)
        annotation_handler.handle()

    except FileNotFoundError as not_found:
        print("File '{}' not found".format(not_found))

    except NotADirectoryError as not_found:
        print("Directory '{}' does not exist".format(not_found))


if __name__ == "__main__":
    main()
