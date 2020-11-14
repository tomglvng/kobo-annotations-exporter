from sanitize_filename import sanitize
from pathlib import Path


class TextExporter:
    @staticmethod
    def export(retrieved_annotations: dict, directory: str) -> None:
        for author in retrieved_annotations:
            author_directory = "{}/{}/".format(directory, sanitize(author))
            Path(author_directory).mkdir(parents=True, exist_ok=True)
            books = retrieved_annotations[author]
            for book in books:
                book_file_name = "{}/{}.txt".format(author_directory, sanitize(book))
                book_file = Path(book_file_name).open(mode="a", encoding="utf-16")
                chapters = books[book]
                for chapter in chapters:
                    book_file.write("\n\n{}\n".format(chapter))
                    annotations = chapters[chapter]
                    for annotation in annotations:
                        comment = ''
                        if annotation.comment is not None and annotation.comment:
                            comment = "({})".format(annotation.comment)
                        last_update = "[{}]".format(annotation.last_update)
                        book_file.write("{} - {}: {}\n\n".format(last_update, comment, annotation.text))
                    book_file.write("\n")
