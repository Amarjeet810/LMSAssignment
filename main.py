from book import Book
from library import Library
library = Library()

#adding books to the library
def add_books():
    while True:
        title = input("Enter book title (or 'quit' to stop): ")
        if title.lower() == 'quit':
            break
        author = input("Enter book author: ")
        isbn = int(input("Enter ISBN number: "))
        genre = input("Enter genre: ")
        price = float(input("Enter book price: "))

        new_book = Book(title, author, isbn, genre, price)
        library.addBook(new_book)
        print(f"Book '{title}' added successfully.\n")

# add users in library
def add_users():
    while True:
        user_name = input("Enter user name (or 'quit' to stop): ")
        if user_name.lower() == 'quit':
            break
        library.addUser(user_name)
        print(f"User {user_name} added to the library.\n")

#search books from the library
def search_books():
    while True:
        search_type = input("Search by Title, Author, or Genre (or 'quit' to stop): ").lower()
        if search_type == 'quit':
            break
        if search_type == 'title':
            title = input("Enter book title: ")
            library.searchByTitle(title)
        elif search_type == 'author':
            author = input("Enter author name: ")
            library.searchByAuthor(author)
        elif search_type == 'genre':
            genre = input("Enter genre: ")
            library.searchByGenre(genre)
        else:
            print("Invalid search type.")

#Borrow books
def borrow_book():
    while True:
        isbn = int(input("Enter ISBN of the book to borrow (or 'quit' to stop): "))
        if isbn == 'quit':
            break
        try:
            library.borrowBook(isbn)
        except Exception as e:
            print(e)

# Function to issue books to users
def issue_book_to_user():
    user_name = input("Enter user name: ")
    isbn = int(input("Enter ISBN of the book to issue: "))
    try:
        library.issueToUser(user_name, isbn)
    except Exception as e:
        print(e)

# Function to display user library card
def display_library_card():
    user_name = input("Enter user name to display library card: ")
    library.displayLibrarycard(user_name)

# Function to calculate fines for a user
def calculate_fine():
    user_name = input("Enter user name to calculate fine: ")
    library.fine(user_name)

# Function to return a borrowed book
def return_borrowed_book():
    isbn = int(input("Enter ISBN of the book to return: "))
    library.returnBook(isbn)

# Function to display all users
def display_all_users():
    library.displayAllUsers()

# Function to display all books
def display_all_books():
    library.displayAllBooks()

# Main function to drive the menu
def main():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Books")
        print("2. Add Users")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Issue Book to User")
        print("6. Display User Library Card")
        print("7. Calculate Fine")
        print("8. Return Book")
        print("9. Display All Users")
        print("10. Display All Books")
        print("11. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_books()
        elif choice == '2':
            add_users()
        elif choice == '3':
            search_books()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            issue_book_to_user()
        elif choice == '6':
            display_library_card()
        elif choice == '7':
            calculate_fine()
        elif choice == '8':
            return_borrowed_book()
        elif choice == '9':
            display_all_users()
        elif choice == '10':
            display_all_books()
        elif choice == '11':
            print("Exiting library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
