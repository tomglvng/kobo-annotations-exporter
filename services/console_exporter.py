from services.exporter_interface import ExporterInterface


class ConsoleExporter(ExporterInterface):
    def export(self, retrieved_annotations: dict, directory: str) -> None:
        for author in retrieved_annotations:
            print('\n' + '-' * 10)
            print('-' * 1 + author)
            books = retrieved_annotations[author]
            for book in books:
                print('-' * 2 + book)
                chapters = books[book]
                for chapter in chapters:
                    print('-' * 3 + chapter)
                    annotations = chapters[chapter]
                    for annotation in annotations:
                        comment = ''
                        if annotation.comment is not None and annotation.comment:
                            comment = '(' + annotation.comment + ') '
                        last_update = '[' + annotation.last_update + '] '
                        print('-' * 4 + last_update + comment + annotation.text)
