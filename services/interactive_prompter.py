from exceptions.user_asks_for_end_of_interactive_mode_exception import UserAsksforEndOfInteractiveModeException
from exceptions.sqlite_file_not_found_exception import SqliteFileNotFoundException
from exceptions.export_format_not_recognized_exception import ExportFormatNotRecognized
from exceptions.export_directory_not_found_exception import ExportDirectoryNotFound
import os.path


class InteractivePrompter:
    HOW_TO_QUIT = "You can exit this interactive mode by tiping 'quit'"
    QUIT = "quit"
    AVAILABLE_EXPORT_FORMATS = ["console", "word", "text"]

    def __init__(self) -> None:
        self.books_selection = []
        self.end_of_prompt = False
        self.sqlite = ""
        self.format = "console"
        self.directory = "exports"

    def ask_books(self, annotations: dict) -> dict:
        titles = {}
        i = 1
        for author in annotations:
            books = annotations[author]
            for book in books:
                titles[i] = {
                    'author': author,
                    'title': book}
                print("{0} : {1} - {2}".format(i, book, author))
                i = i + 1

        self.__prompt_books_selection()

        filtered_annotation = {}

        for indice in titles:
            if indice in self.books_selection:
                selected_book = titles[indice].get('title')
                selected_author = titles[indice].get('author')
                if selected_author not in filtered_annotation:
                    filtered_annotation[selected_author] = {}
                if selected_book not in filtered_annotation[selected_author]:
                    filtered_annotation[selected_author][selected_book] = {}
                filtered_annotation[selected_author][selected_book] = annotations[selected_author].get(selected_book)

        return filtered_annotation

    def ask_information(self):
        print("###############################################################################")
        print("#                                                                             #")
        print("#                        Kobo Annotations Exporter                            #")
        print("#                                                                             #")
        print("###############################################################################")
        print("Welcome to the Kobo Annotations Exporter !")
        print("This software will help you to export annotations you made during your reading on your beloved Kobo "
              "device.")

        while not self.end_of_prompt:
            try:
                # self.__prompt_sqlite_location()
                # TODO: DEBUG
                self.sqlite = "databases/database.sqlite"
                self.__prompt_export_format()
                self.__prompt_export_directory_location()
                self.__set_end_of_prompt()
            except (SqliteFileNotFoundException, ExportFormatNotRecognized, ExportDirectoryNotFound) as e:
                print(e.message)

    def __prompt_books_selection(self) -> None:
        raw_books_selection = self.__prompt_text_or_quit(
            "Which books do you want to export ? Select books by typing their number separated by space. Press 'Enter' for exporting all")
        self.books_selection = [int(x) for x in raw_books_selection.split(" ")]

    def __prompt_sqlite_location(self) -> None:
        raw_sqlite = self.__prompt_text_or_quit("First of all, where is your Kobo sqlite file ?")
        if not os.path.isfile(raw_sqlite):
            raise SqliteFileNotFoundException("file '{}' not found".format(raw_sqlite))
        self.sqlite = raw_sqlite

    def __prompt_export_format(self) -> None:
        raw_export_format = self.__prompt_text_or_quit(
            "In which format do you want to export (word or text) ? Press 'Enter' for console export")
        if not raw_export_format == '' and raw_export_format not in self.AVAILABLE_EXPORT_FORMATS:
            raise ExportFormatNotRecognized(
                "export format '{0}' not found in {1}".format(raw_export_format, self.AVAILABLE_EXPORT_FORMATS))
        self.format = raw_export_format

    def __prompt_export_directory_location(self) -> None:
        raw_export_directory = self.__prompt_text_or_quit(
            "In which directory do you want to export your annotations ? Press 'Enter' for the default directory "
            "'exports'")
        if raw_export_directory == '':
            raw_export_directory = "exports"
            if not os.path.isdir(raw_export_directory):
                os.mkdir(raw_export_directory)
        elif not os.path.isdir(raw_export_directory):
            raise ExportDirectoryNotFound("directory '{0}' not found".format(raw_export_directory))
        self.directory = raw_export_directory if raw_export_directory[-1] != '/' else raw_export_directory[:-1]

    def __prompt_text_or_quit(self, question: str) -> str:
        answer = input("{0} ({1}): ".format(question, self.HOW_TO_QUIT))
        if self.QUIT == answer:
            raise UserAsksforEndOfInteractiveModeException
        return answer

    def __set_end_of_prompt(self) -> None:
        self.end_of_prompt = True
