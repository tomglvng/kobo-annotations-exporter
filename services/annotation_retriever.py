import sqlite3
from datetime import datetime
from repositories.book import BookRepository
from repositories.annotation import AnnotationRepository


class AnnotationRetriever:
    def __init__(self, sqlite_file_name: str) -> None:
        connection = sqlite3.connect(sqlite_file_name)
        self.book_repository = BookRepository(connection)
        self.annotation_repository = AnnotationRepository(connection)

    """
        Return books.
        Format of the return data structure :
        {book1: Book, book2: Book},
    """

    def __get_books(self) -> dict:
        return self.book_repository.get_already_opened_books()

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

    def __get_annotations(self, book_id: str, since: datetime) -> dict:
        return self.annotation_repository.get_annotations(book_id, since)

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

    def retrieve(self, since: datetime) -> dict:
        retrieved_annotations = {}
        books = self.__get_books()
        for book in books:
            author = books[book].author
            title = books[book].title
            annotations = self.__get_annotations(book, since)
            if len(annotations) > 0:
                if author not in retrieved_annotations:
                    retrieved_annotations[author] = {}
                if title not in retrieved_annotations[author]:
                    retrieved_annotations[author][title] = {}
                retrieved_annotations[author][title] = annotations

        return retrieved_annotations
