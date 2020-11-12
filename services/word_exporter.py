from docx import Document
from sanitize_filename import sanitize


class WordExporter:
    @staticmethod
    def export(retrieved_annotations, directory) -> None:
        for author in retrieved_annotations:
            books = retrieved_annotations[author]
            for book in books:
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
                        p = document.add_paragraph(last_update + comment + annotation.text, style='Intense Quote')
                file_name = sanitize(author + '-' + book)
                document.save(directory + file_name + '.docx')
