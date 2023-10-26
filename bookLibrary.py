class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addBook(self, a):
        self.book_name = a
        self.books.append(self.book_name)
        self.no_of_books += 1
    
    def show_all_books(self):
        print(self.books)
        print("No. of Books in total : " + str(self.no_of_books))
        
library1 = Library()
library1.addBook("Alice in Wonderland")
library1.addBook("Around the world in 80 Days")
library1.show_all_books()
