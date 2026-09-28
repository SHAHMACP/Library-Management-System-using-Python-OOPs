# ============================================================
#                 LIBRARY MANAGEMENT SYSTEM
#                       library.py
# ============================================================

from abc import ABC


# ============================================================
#                    1. LIBRARY CLASS
# ============================================================

class Library(ABC):

    # CLASS VARIABLES
    library_name = "Central Library"
    library_location = "Calicut"
    starting_year = 1995
    librarian = "Mr. Ahmed"
    contact_number = "9876543210"

    # INSTANCE METHOD - Display Library Details
    def library_details(self):

        return {
            "Library Name": self.library_name,
            "Location": self.library_location,
            "Starting Year": self.starting_year,
            "Librarian": self.librarian,
            "Contact Number": self.contact_number
        }


# ============================================================
#                    2. BOOKS CLASS
# ============================================================

class Books(Library):

    # CLASS VARIABLE
    # Stores all Book objects
    books_list = []

    def __init__(self, book_id, title, author, category):

        # INSTANCE VARIABLES
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category

        # Book is initially available
        self.available = True

        # Customer ID of the person who issued the book
        self.issued_to = None

        # Automatically add the complete Book object
        # to the list
        Books.books_list.append(self)


    # ========================================================
    # CLASS METHOD - Display Available Books
    # ========================================================

    @classmethod
    def display_available_books(cls):

        available_books = []

        for book in cls.books_list:
            if book.available:
                available_books.append(book)
        return available_books


    # ========================================================
    # CLASS METHOD - Search Available Books by Title
    # ========================================================

    @classmethod
    def search_book(cls, title):

        found_books = []

        for book in cls.books_list:
            # Check only available books
            if book.available:
                # Search title
                if title.lower() in book.title.lower():
                    found_books.append(book)
        return found_books


    # ========================================================
    # INSTANCE METHOD - Display Book Details
    # ========================================================

    def display_books(self):
        if self.available:
            status = "Available"
            issued_to = "None"
        else:
            status = "Issued"
            issued_to = self.issued_to
        return {
            "Book ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Category": self.category,
            "Status": status,
            "Issued To": issued_to
        }


# ============================================================
#                    3. CUSTOMER CLASS
# ============================================================

class Customer(Library):

    def __init__(self, customer_id, name, phone, age):
        # INSTANCE VARIABLES
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.age = age

        # PRIVATE INSTANCE VARIABLE
        # Stores books currently issued by this customer
        self.__issued_books = []

        # PRIVATE INSTANCE VARIABLE
        # Stores total fine
        self.__fine = 0


    # ========================================================
    # INSTANCE METHOD - Customer Details
    # ========================================================

    def customer_details(self):
        return {
            "Customer ID": self.customer_id,
            "Customer Name": self.name,
            "Phone Number": self.phone,
            "Age": self.age,
            "Books Issued": len(self.__issued_books),
            "Total Fine": self.__fine
        }


    # ========================================================
    # INSTANCE METHOD - Check Issue Eligibility
    # ========================================================

    def can_issue_book(self):
        # Maximum 4 books per customer
        if len(self.__issued_books) < 4:
            return True
        return False


    # ========================================================
    # INSTANCE METHOD - Add Issued Book
    # ========================================================

    def add_issued_book(self, book):
        self.__issued_books.append({
            "id": book.book_id,
            "title": book.title
        })


    # ========================================================
    # INSTANCE METHOD - Remove Issued Book
    # ========================================================

    def remove_issued_book(self, book_id):
        for book in self.__issued_books:
            if book["id"] == book_id:
                self.__issued_books.remove(book)
                return True
        return False


    # ========================================================
    # INSTANCE METHOD - Get Issued Books
    # ========================================================

    def get_issued_books(self):
        return self.__issued_books


    # ========================================================
    # INSTANCE METHOD - Add Fine
    # ========================================================

    def add_fine(self, amount):
        self.__fine += amount


    # ========================================================
    # INSTANCE METHOD - Get Fine
    # ========================================================

    def get_fine(self):
        return self.__fine


# ============================================================
#                4. LIBRARY ACTIVITIES CLASS
# ============================================================

class LibraryActivities:
    # ========================================================
    # INSTANCE METHOD - ISSUE BOOK
    # ========================================================

    def issue_book(self, customer, book):
        # Check customer eligibility
        if not customer.can_issue_book():
            return (
                False,
                "Book issue limit reached. "
                "A customer can issue maximum 4 books."
            )


        # Check book availability
        if not book.available:
            return (
                False,
                "Sorry! This book is already issued."
            )


        # Change book status
        book.available = False


        # Store customer ID in book
        book.issued_to = customer.customer_id


        # Add book to customer's issued list
        customer.add_issued_book(book)


        return (
            True,
            f"'{book.title}' issued successfully "
            f"to {customer.name}."
        )


    # ========================================================
    # INSTANCE METHOD - RETURN BOOK
    # ========================================================

    def return_book(
        self,
        customer,
        book,
        damage_level
    ):

        # Check whether this customer issued the book
        if book.issued_to != customer.customer_id:

            return (
                False,
                0,
                "This book was not issued to this customer."
            )


        # Calculate fine
        fine = 0


        if damage_level == "No Damage":
            fine = 0
        elif damage_level == "Minor Damage":
            fine = 50
        elif damage_level == "Major Damage":
            fine = 100


        # Make book available again
        book.available = True


        # Remove customer ID
        book.issued_to = None


        # Remove book from customer's issued list
        customer.remove_issued_book(
            book.book_id
        )


        # Add fine to customer account
        customer.add_fine(fine)


        return (
            True,
            fine,
            f"'{book.title}' returned successfully."
        )