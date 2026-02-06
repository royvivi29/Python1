class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

book1 = Book("Build wealth like a boss", 420)
book2 = Book("48 LAws of Power", 562)

#print(len(book1))   #typeError: object of type 'Book' has no lens()
#print(str(book1)) #<__main__.Book object at 0x0000022FEF4D05C0>
#print(book1 == book2) # false

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages
    
book1 = Book("Build wealth like a boss", 420)
book2 = Book("Be your own start", 420)

print(len(book1))
print(len(book2))
print(str(book1))
print(str(book2))
print(book1 == book2)