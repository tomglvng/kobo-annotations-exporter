from datetime import datetime
from services.annotation_retriever import AnnotationRetriever
from services.console_exporter import ConsoleExporter
from services.text_exporter import TextExporter
from services.word_exporter import WordExporter


class AnnotationHandler:
    def __init__(self,
                 sqlite_file_name: str,
                 export_format: str,
                 export_directory: str,
                 export_since: datetime) -> None:
        self.retriever = AnnotationRetriever(sqlite_file_name)
        self.export_format = export_format
        self.export_directory = export_directory
        self.export_since = export_since

    def handle(self) -> None:
        exporter = {
            "word": lambda a, d: WordExporter.export(a, d),
            "text": lambda a, d: TextExporter.export(a, d),
            "console": lambda a, d: ConsoleExporter.export(a),
        }
        exporter[self.export_format](self.retriever.retrieve(self.export_since),
                                     self.export_directory)
