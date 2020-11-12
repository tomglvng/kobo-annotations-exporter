class ConsoleExporter:
    @staticmethod
    def export(retrieved_annotations) -> None:
        for author in retrieved_annotations:
            print('\n----------')
            print('-' + author)
            for books in retrieved_annotations[author]:
                for book in books:
                    print('--' + book)
                    for annotation in books[book]:
                        print('---' + '(' + str(annotation.comment).strip() + ') ' + str(annotation.text).strip())
