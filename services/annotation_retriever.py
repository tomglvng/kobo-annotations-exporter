import sqlite3
from constants import colmuns
from constants import queries
from model.annotation import Annotation
from model.book import Book


class AnnotationRetriever:

    def __init__(self, sqlite_file_name: str) -> None:
        self.connection = sqlite3.connect(sqlite_file_name)

    def __get_books(self) -> dict:
        cursor = self.connection.cursor()
        books = {}

        for row in cursor.execute(queries.BOOKS_RETRIEVER):
            book_id = row[colmuns.BOOK_ID]
            title = row[colmuns.BOOK_TITLE]
            author = row[colmuns.BOOK_AUTHOR]
            books[book_id] = Book(title, author)

        cursor.close()

        return books

    def __get_annotations(self, book_id: str) -> dict:
        cursor = self.connection.cursor()
        annotations = {}
        for row in cursor.execute(queries.ANNOTATIONS_RETRIEVER.format(book_id)):

            chapter = row[colmuns.ANNOTATION_CHAPTER]
            text = row[colmuns.ANNOTATION_TEXT]
            comment = row[colmuns.ANNOTATION_COMMENT]
            last_update = row[colmuns.ANNOTATION_LAST_UPDATE]
            annotation = Annotation(text, comment, chapter, last_update)
            if chapter not in annotations:
                annotations[chapter] = []
            annotations[chapter].append(annotation)

        cursor.close()

        return annotations

    def retrieve(self) -> dict:
        retrieved_annotations = {}
        books = self.__get_books()
        for book in books:
            author = books[book].author
            annotations = self.__get_annotations(book)

            if len(annotations) > 0:
                if author not in retrieved_annotations:
                    retrieved_annotations[author] = []

                retrieved_annotations[author].append(annotations)

        return retrieved_annotations
