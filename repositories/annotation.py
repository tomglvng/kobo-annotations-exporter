from datetime import datetime
from sqlite3 import Connection
from models.annotation import AnnotationModel


class AnnotationRepository:
    def __init__(self, connection: Connection):
        self.connection = connection
        self._col_id = 0
        self._col_text = 1
        self._col_comment = 2
        self._col_chapter = 3
        self._col_last_update = 4

    @staticmethod
    def __get_base_query() -> str:
        return "SELECT Bookmark.BookmarkID, Bookmark.Text AS text, Bookmark.Annotation AS comment, " \
               "content.Title AS chapter, COALESCE(Bookmark.DateModified,Bookmark.DateCreated) AS last_update " \
               "FROM Bookmark INNER JOIN content ON Bookmark.ContentID = content.ContentID " \
               "WHERE (Text IS NOT NULL OR Annotation IS NOT NULL) "

    def __get_query_by_book_id(self, book_id: str) -> str:
        return "{} AND Bookmark.VolumeID='{}' ORDER BY content.title ASC".format(self.__get_base_query(), book_id)

    def __get_query_by_book_id_and_last_update_date(self, book_id: str, last_update_date: datetime) -> str:
        return "{} AND Bookmark.VolumeID='{}' AND strftime('%Y-%m-%d %H:%M:%S',last_update) > '{}' " \
               "ORDER BY content.title ASC".format(self.__get_base_query(), book_id, last_update_date)

    def get_annotations(self, book_id: str, last_update_date: datetime) -> dict:
        query = self.__get_query_by_book_id(book_id) \
            if last_update_date is None \
            else self.__get_query_by_book_id_and_last_update_date(book_id, last_update_date)
        annotations = {}

        for row in self.connection.cursor().execute(query):
            text = row[self._col_text]
            comment = row[self._col_comment]
            chapter = row[self._col_chapter]
            last_update = row[self._col_last_update]
            annotation = AnnotationModel(text, comment, last_update)
            if chapter not in annotations:
                annotations[chapter] = []
            annotations[chapter].append(annotation)

        return annotations
