from docx import Document
from sanitize_filename import sanitize
from pathlib import Path


class WordExporter:
    @staticmethod
    def export(retrieved_annotations: dict, directory: str) -> None:
        for author in retrieved_annotations:
            author_directory = "{}/{}/".format(directory, sanitize(author))
            Path(author_directory).mkdir(parents=True, exist_ok=True)
            books = retrieved_annotations[author]
            for book in books:
                book_file_name = "{}/{}.docx".format(author_directory, sanitize(book))
                document = Document()
                document.add_heading(book, 0)
                chapters = books[book]
                for chapter in chapters:
                    document.add_heading(chapter, level=1)
                    annotations = chapters[chapter]
                    for annotation in annotations:
                        comment = ''
                        if annotation.comment is not None and annotation.comment:
                            comment = '(' + annotation.comment + ') '
                        last_update = '[' + annotation.last_update + '] '
                        document.add_paragraph(last_update + comment + annotation.text, style='Intense Quote')
                document.save(book_file_name)
