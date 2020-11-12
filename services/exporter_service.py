import sqlite3
from model.annotations import Annotation
from model.book import Book


class ExporterService:
    query_books = "SELECT " \
                  "ContentId," \
                  "title," \
                  "Attribution " \
                  "FROM content " \
                  "WHERE title IS NOT NULL " \
                  "AND title <> '' " \
                  "AND Attribution IS NOT NULL " \
                  "AND Attribution <> '' " \
                  "AND ReadStatus <> 0 " \
                  "ORDER BY ContentId ASC LIMIT 70"

    book_id = 0
    title = 1
    author = 2

    annotation_query = "SELECT  " \
                       "Bookmark.BookmarkID, " \
                       "Bookmark.Text AS text," \
                       "Bookmark.Annotation AS comment," \
                       "content.Title AS chapter," \
                       "COALESCE(Bookmark.DateModified,Bookmark.DateCreated) AS last_update " \
                       "FROM Bookmark INNER JOIN content ON Bookmark.VolumeID = content.ContentID " \
                       "WHERE (Text IS NOT NULL OR Annotation IS NOT NULL) " \
                       " AND Bookmark.VolumeID='{}'" \
                       "ORDER BY content.title ASC"
    bookmark_id = 0
    text = 1
    comment = 2
    chapter = 3
    last_update = 4

    def __init__(self, sqlite_file_name: str) -> None:
        self.connection = sqlite3.connect(sqlite_file_name)

    def get_books(self) -> dict:
        books = {}
        cursor = self.connection.cursor()
        for row in cursor.execute(self.query_books):
            books[row[self.book_id]] = Book(row[self.title], row[self.author])
        cursor.close()

        return books

    def get_annotations(self, book_id: str) -> dict:
        annotations = {}
        cursor = self.connection.cursor()
        for row in cursor.execute(self.annotation_query.format(book_id)):
            if not row[self.chapter] in annotations:
                annotations[row[self.chapter]] = []
            annotation = Annotation(row[self.text], row[self.comment], row[self.chapter],
                                    row[self.last_update])
            annotations[row[self.chapter]].append(annotation)
        cursor.close()

        return annotations

    def print_annotations(self, per_authors) -> None:
        for author in per_authors:
            print('\n----------')
            print('-' + author)
            for books in per_authors[author]:
                for book in books:
                    print('--' + book)
                    for annotation in books[book]:
                        print('---' + '(' + str(annotation.comment).strip() + ') ' + str(annotation.text).strip())

    def export_annotations(self) -> None:
        per_authors = {}
        books = self.get_books()
        for key in books:
            author = books[key].author
            title = books[key].title
            annotations = self.get_annotations(key)

            if len(annotations) > 0:
                if author not in per_authors:
                    per_authors[author] = []

                per_authors[author].append(annotations)

        self.print_annotations(per_authors)
