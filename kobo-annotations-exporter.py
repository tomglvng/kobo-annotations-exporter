import argparse
from services.annotation_handler import AnnotationHandler
from services.argument_checker import check_date
from services.argument_checker import check_file_existence
from services.argument_checker import check_folder_existence
from services.interactive_prompter import InteractivePrompter
from exceptions.user_asks_for_end_of_interactive_mode_exception import UserAsksforEndOfInteractiveModeException
from services.annotation_retriever import AnnotationRetriever


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export annotations from Kobo sqlite database",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--interactive',
                        '-i',
                        action='store_true',
                        help='Interactive mode')
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

    try:
        if args.interactive:
            print(args.interactive)
            interactive_prompter = InteractivePrompter()
            interactive_prompter.ask_information()

            retriever = AnnotationRetriever(interactive_prompter.sqlite)
            annotations = retriever.retrieve(args.since)

            books_title = interactive_prompter.ask_books(annotations)
            print(books_title)

            # TODO: change data structure maybe ?
            # TODO: integration choice list of books
            # TODO: uuid.uuid4() for idbook

            """
                Format of the returned data structure :
                {
                    uuid_author: id {
                        name: str,
                        books: [
                            uuid_book: id {
                                title: str,
                                chapters:[
                                    chapter: str, {annotation: Annotation},
                                ]
                            }
                        ]
                    }
                },
                """





        else:
            annotation_handler = AnnotationHandler(args.sqlite, args.format, args.directory, args.since)
            annotation_handler.handle()
    except UserAsksforEndOfInteractiveModeException:
        print("Bye.")
        exit()


if __name__ == "__main__":
    main()
