# Aggregation: 두 객체가 서로 연결되어 있지만 서로 독립적으로 존재할 수 있는 관계
#              e.g. 학생과 노트북: 학생은 노트북을 가지고 있지만, 둘은 서로 독립적임

class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # Aggregation

    def add_book(self, book): # Aggregation
        self.books.append(book) # Aggregation

    def list_books(self): # Aggregation
        return [f'{book.title} by {book.author}' for book in self.books] # Aggregation

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library('New York Public Library')

book1 = Book('Harry Potter...', 'J.K.Rowling')        # 독립적으로 존재
book2 = Book('The Hobbit', 'J.R.R.Tolkein')           # 독립적으로 존재
book3 = Book('The Colour of Magic', 'Terry Pratchet') # 독립적으로 존재

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)               # New York Public Library

for book in library.list_books(): # Harry Potter... by J.K.Rowling
        print(book)               # The Hobbit by J.R.R.Tolkein
                                  # The Colour of Magic by Terry Pratchet
