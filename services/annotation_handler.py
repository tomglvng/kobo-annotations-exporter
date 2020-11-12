from services.annotation_retriever import AnnotationRetriever
from services.console_exporter import ConsoleExporter
from services.word_exporter import WordExporter
from services.txt_exporter import TextExporter


class AnnotationHandler:
    def __init__(self, sqlite_file_name: str, word_format: str, text_format: str, export_directory: str) -> None:
        self.retriever = AnnotationRetriever(sqlite_file_name)

        self.export_format = "console"

        if word_format is not None:
            self.export_format = word_format

        if text_format is not None:
            self.export_format = text_format

        self.export_directory = "exports/" if export_directory is None else export_directory

    def handle(self) -> None:
        annotations = self.retriever.retrieve()

        if self.export_format == 'word':
            WordExporter.export(annotations, self.export_directory)
        elif self.export_format == 'text':
            TextExporter.export(annotations, self.export_directory)
        else:
            ConsoleExporter.export(annotations)
