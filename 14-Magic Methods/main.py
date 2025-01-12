# Magic Methods: Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Python's built-in operations.
#                They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # instead of returning a memory adress, we can customize it
        return f'{self.title} by {self.author}'
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f'Key {key} was not found'

book1 = Book('The Hobbit', 'J.R.R. Tolkien', 310)
book2 = Book("Harry Potter and The Philosopher's Stone", 'J.K. Rowling', 223)
book3 = Book('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 172)

# __str__로 구현
# 원래의 print(book1)은 메모리주소를 반환하지만, __str__를 설정해서 print(book1)이 The Hobbit by J.R.R Tolkien을 반환함
print(book1) # The Hobbit by J.R.R Tolkien

# __eq__ (구현 안 해도 출력되긴 함)
print(book1 == book2) # False

#  __lt__로 구현
print(book2 > book3) # True

# __add__로 구현
print(book2 + book3) # 395

# __contains__로 구현
print("Lion" in book3) # True

# __getitem__로 구현
print(book1['title']) # The Hobbit
print(book3['audio']) # Key audio was not found