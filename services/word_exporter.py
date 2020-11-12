from docx import Document


def word(per_authors, directory):
    document = Document()
    document.add_heading('Document', 0)

    for author in per_authors:
        document.add_heading(author, level=1)
        for books in per_authors[author]:
            for book in books:
                document.add_heading(book, level=2)
                for annotation in books[book]:
                    p = document.add_paragraph(str(annotation.text).strip(), style='Intense Quote')
                    if annotation.comment:
                        p.add_run(str(annotation.comment).strip())
    document.add_page_break()
    document.save(directory + 'demoaaaa.docx')
