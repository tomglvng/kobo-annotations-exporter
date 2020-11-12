from services.annotation_retriever import AnnotationRetriever
from services.console_exporter import ConsoleExporter
from services.word_exporter import word


class AnnotationHandler:
    def __init__(self, sqlite_file_name: str, export_format: str, export_directory: str) -> None:
        self.retriever = AnnotationRetriever(sqlite_file_name)
        self.export_format = "console" if export_format is None else export_format
        self.export_directory = "exports/" if export_directory is None else export_directory

    def handle(self) -> None:
        annotations = self.retriever.retrieve()

        if self.export_format == 'word':
            word(annotations, self.export_directory)
        else:
            ConsoleExporter.export(annotations)
