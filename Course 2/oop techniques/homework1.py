class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

clrs = Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009)
jk = Book('Diary of a Wimpy Kid', ['Jeff Kinney'], 2007)

vov = Book("3 Idiots", ['Vaishnav', "Shubham", "Ranak"], 2024)


print(clrs)
print(jk)
print(vov)
print()

books = [clrs, jk, vov]

books.sort(key= lambda book: len(book.authors), reverse=True)

for book in books:
    print(book)