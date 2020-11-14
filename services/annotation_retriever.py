import sqlite3
from constants import colmuns
from constants import queries
from models.annotation import Annotation
from models.book import Book


class AnnotationRetriever:
    def __init__(self, sqlite_file_name: str) -> None:
        self.connection = sqlite3.connect(sqlite_file_name)

    """
        Return books.
        Format of the return data structure :
        {book1: Book, book2: Book},
    """

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

    """
       Return annotations by chapter and by book.
       Format of the return data structure :
       {
            book1: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
            book2: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
       },
       """

    def __get_annotations(self, book_id: str) -> dict:
        cursor = self.connection.cursor()
        annotations = {}
        for row in cursor.execute(queries.ANNOTATIONS_RETRIEVER.format(book_id)):
            text = row[colmuns.ANNOTATION_TEXT]
            comment = row[colmuns.ANNOTATION_COMMENT]
            chapter = row[colmuns.ANNOTATION_CHAPTER]
            last_update = row[colmuns.ANNOTATION_LAST_UPDATE]
            annotation = Annotation(text, comment, last_update)
            if chapter not in annotations:
                annotations[chapter] = []
            annotations[chapter].append(annotation)
        cursor.close()

        return annotations

    """
    Return annotations by book and by author.
    Format of the return data structure :
    {
        author1: str, {
            book1: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
            book2: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
       },
       author2: str, {
            book1: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
            book2: str, {
                chapter1: str, {annotation1: Annotation,annotation2: Annotation,},
                chapter2: str, {annotation1: Annotation,annotation2: Annotation,},
            },
       },
    """

    def retrieve(self) -> dict:
        retrieved_annotations = {}
        books = self.__get_books()
        for book in books:
            author = books[book].author
            title = books[book].title
            annotations = self.__get_annotations(book)
            if len(annotations) > 0:
                if author not in retrieved_annotations:
                    retrieved_annotations[author] = {}
                if title not in retrieved_annotations[author]:
                    retrieved_annotations[author][title] = {}
                retrieved_annotations[author][title] = annotations

        return retrieved_annotations
