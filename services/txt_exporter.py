from sanitize_filename import sanitize


class TextExporter:
    @staticmethod
    def export(retrieved_annotations, directory) -> None:
        for author in retrieved_annotations:
            books = retrieved_annotations[author]
            for book in books:
                file_name = sanitize(author + '-' + book)
                f = open(directory + file_name + '.txt', "a")
                f.write('-' * 80)
                chapters = books[book]
                for chapter in chapters:
                    f.write('-' * 1 + chapter)
                    annotations = chapters[chapter]
                    for annotation in annotations:
                        comment = ''
                        if annotation.comment is not None and annotation.comment:
                            comment = '(' + annotation.comment + ') '
                        last_update = '[' + annotation.last_update + '] '
                        f.write('--' + last_update + comment + annotation.text)
                f.close()
