
from datetime import datetime
from book import Book
#  when a book is unavailable for borrowing
class BookUnavailableException(Exception):
    def __init__(self, message="This book is currently unavailable."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"BookUnavailableException: {self.message}"

# when a book is not found in the library
class BookNotFoundException(Exception):
    def __init__(self, message="Book not found in the library."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"BookNotFoundException: {self.message}"


#creating Library Class
class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    #creating add Book function
    def addBook(self,book):
        self.books.append(book)

    # Search book by title
    def searchByTitle(self,title):
        getBook = [book for book in self.books if book.title.lower() == title.lower()]
        if getBook:
            for book in getBook:
                print(book)
        else:
            print("No books found with that title.")
    
    # Search book by author
    def searchByAuthor(self,author):
        getBook = [book for book in self.books if book.author.lower() == author.lower()]
        if getBook:
            for book in getBook:
                print(book)
        else:
            print("No books found with that author.")
    
    # Search book by genre
    def searchByGenre(self,genre):
        getBook = [book for book in self.books if book.genre.lower() == genre.lower()]
        if getBook:
            for book in getBook:
                print(book)
        else:
            print("No books found with that genre.")


    # creating borrow method
    def borrowBook(self,isbn):
        #book = [book for book in self.books if book.isbn == isbn]
        book = next((book for book in self.books if book.isbn == isbn), None) 
        if book:
            if book.available:
                book.available = False
                book.issued_timestamp = datetime.now()
                print(f"Book '{book.title}' has been borrowed.")
            else:
                raise BookUnavailableException(f"Book '{book.title}' is currently unavailable.")
        else:
            raise BookNotFoundException("Book not found in the library.")

     #create return book method          
    def returnBook(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book:
            if not book.available:
                book.available = True
                book.issued_timestamp = None
                print(f"Book '{book.title}' has been returned")
            else:
                print("This book was not borrowed")
        else:
            raise BookNotFoundException("Book not found in the library")
    
    #  Add users method
    def addUser(self, user):
        if user not in self.users:
            self.users[user] = {'issued_books': [], 'fine': 0}
            print(f"User {user} has been added to the library.")
        else:
            print(f"User {user} already exists.")

    #issuing book to particular user
    def issueToUser(self, user,isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book:
            if book.available:
                book.available = False
                book.issued_timestamp = datetime.now()
                #creating issued book list
                self.users[user]['issued_books'].append(book)
                print(f"Book '{book.title}' has been issued to user {user}")
            else:
                raise BookUnavailableException(f"Book '{book.title}' is currently unavailable.")
        else:
            raise BookNotFoundException("Book not found in the library.")
        

    # display library card method by user    
    def displayLibrarycard(self,userName):
         user = self.users[userName]
         if user:
            print(f"Library Card for User {userName}:")
            for book in user['issued_books']:
                print(book)
            print(f"Total Fine: Rs{user['fine']:.2f}")
         else:
            print(f"User {user} not found.")

    #create fine method for calculate fine for user
    def fine(self, userName):
        fineRate = 0.02  # 2% per day
        totalFine = 0
        for book in self.users[userName]['issued_books']:
            if book.issued_timestamp:
                days_issued = (datetime.now() - book.issued_timestamp).days
                if days_issued > 90:
                    totalFine += (book.price * fineRate * (days_issued - 90))
        self.users[userName]['fine'] = totalFine
        print(f"User {userName} has a total fine of: ${totalFine:.2f}")

    #Display all User method
    def displayAllUsers(self):
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users available in the library")
        

    #Display all books method
    def displayAllBooks(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")
    

  
    