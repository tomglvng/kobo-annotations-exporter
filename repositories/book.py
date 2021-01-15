from pypika import Query, Table, Field, Order
from sqlite3 import Connection
from models.book import BookModel

class BookRepository:
    def __init__(self, connection: Connection):
        self.connection = connection
        self._col_id = 0
        self._col_title = 1
        self._col_author = 2

    @staticmethod
    def __get_base_query() -> str:
        
        return str(Query.from_('content').select('ContentId', 'title', 'Attribution').where(Field('title').notnull()).where(Field('title') != '').where(Field('Attribution').notnull()).where(Field('Attribution') != '').where(Field('ReadStatus') != 0).orderby(
    Field('ContentId'), order=Order.asc))
    
    def get_already_opened_books(self) -> dict:
        books = {}
        for row in self.connection.cursor().execute(self.__get_base_query()):
            book_id = row[self._col_id]
            title = row[self._col_title]
            author = row[self._col_author]
            books[book_id] = BookModel(title, author)

        return books
