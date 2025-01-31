
class Book:
    def __init__(self, title, author, isbn, genre, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True
        self.price = price
        self.issued_timestamp =  None
    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Price: {self.price}, Availability: {availability},TimeStamp:{self.issued_timestamp}"
