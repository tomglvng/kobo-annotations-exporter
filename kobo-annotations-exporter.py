import argparse
from services.annotation_handler import AnnotationHandler
from services.argument_checker import check_date
from services.argument_checker import check_file_existence
from services.argument_checker import check_folder_existence


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export annotations from Kobo sqlite database",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

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
    parser.add_argument('--since',
                        '-s',
                        type=check_date,
                        help="Export updated annotations since a given date (format: YYYY-MM-DD HH:MM:SS", )

    args = parser.parse_args()

    annotation_handler = AnnotationHandler(args.sqlite, args.format, args.directory, args.since)
    annotation_handler.handle()


if __name__ == "__main__":
    main()
