BOOKS_RETRIEVER = "SELECT " \
                  "ContentId," \
                  "title," \
                  "Attribution " \
                  "FROM content " \
                  "WHERE title IS NOT NULL " \
                  "AND title <> '' " \
                  "AND Attribution IS NOT NULL " \
                  "AND Attribution <> '' " \
                  "AND ReadStatus <> 0 " \
                  "ORDER BY ContentId ASC"
ANNOTATIONS_RETRIEVER = "SELECT  " \
                        "Bookmark.BookmarkID, " \
                        "Bookmark.Text AS text," \
                        "Bookmark.Annotation AS comment," \
                        "content.Title AS chapter," \
                        "COALESCE(Bookmark.DateModified,Bookmark.DateCreated) AS last_update " \
                        "FROM Bookmark INNER JOIN content ON Bookmark.VolumeID = content.ContentID " \
                        "WHERE (Text IS NOT NULL OR Annotation IS NOT NULL) " \
                        " AND Bookmark.VolumeID='{}'" \
                        "ORDER BY content.title ASC"
