from datetime import datetime
from services.annotation_retriever import AnnotationRetriever
from services.console_exporter import ConsoleExporter
from services.exporter_interface import ExporterInterface
from services.text_exporter import TextExporter
from services.word_exporter import WordExporter


def instanciate_exporter(export_type: str) -> ExporterInterface:
    if "word" == export_type:
        return WordExporter()
    if "text" == export_type:
        return TextExporter()

    return ConsoleExporter()


class AnnotationHandler:
    def __init__(self,
                 sqlite_file_name: str,
                 export_format: str,
                 export_directory: str,
                 export_since: datetime,
                 books: str) -> None:
        self.sqlite_file_name = sqlite_file_name
        self.export_format = export_format
        self.export_directory = export_directory
        self.export_since = export_since
        self.books = books

    def handle(self) -> None:
        retriever = AnnotationRetriever(self.sqlite_file_name)
        annotations = retriever.retrieve(self.export_since)
        if self.books:
            for author in annotations:
                print('---------')
                print(author)
                books = annotations[author]
                for book in books:
                    print(book)
                print('---------')
        else:
            exporter = instanciate_exporter(self.export_format)
            exporter.export(annotations, self.export_directory)
