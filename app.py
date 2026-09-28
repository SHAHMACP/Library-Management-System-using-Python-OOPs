# ============================================================
#                 LIBRARY MANAGEMENT SYSTEM
#                         app.py
# ============================================================

import streamlit as st

from library import (
    Library,
    Books,
    Customer,
    LibraryActivities
)


# ============================================================
#                    PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)


# ============================================================
#                    INITIAL DATA
# ============================================================

# Create initial books only once

if "books_initialized" not in st.session_state:

    # Clear class list
    Books.books_list = []

    Books(
        101,
        "Python Basics",
        "John Smith",
        "Programming"
    )

    Books(
        102,
        "Data Science with Python",
        "Rahul",
        "Data Science"
    )

    Books(
        103,
        "Machine Learning",
        "David",
        "AI"
    )

    st.session_state.books_initialized = True


# Create customers only once

if "customers" not in st.session_state:

    st.session_state.customers = [

        Customer(
            "C1026",
            "Emin",
            67809765,
            6
        )
    ]


# Create LibraryActivities object

if "activities" not in st.session_state:

    st.session_state.activities = LibraryActivities()


# ============================================================
#                       SIDEBAR
# ============================================================

st.sidebar.title("📚 Library Management")

menu = st.sidebar.radio(
    "Select Activity",
    [
        "🏠 Home",
        "🏛️ Library Details",
        "📚 Books",
        "👤 Customers",
        "➕ Add Book",
        "👤 Add Customer",
        "🔄 Issue Book",
        "↩️ Return Book"
    ]
)


# ============================================================
#                         HOME
# ============================================================

if menu == "🏠 Home":

    st.title("📚 Library Management System")

    st.write(
        "Welcome to the Central Library Management System."
    )

    st.divider()


    # Calculate statistics

    total_books = len(Books.books_list)

    available_books = len(
        Books.display_available_books()
    )

    issued_books = (
        total_books - available_books
    )

    total_customers = len(
        st.session_state.customers
    )


    # Dashboard

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Books",
        total_books
    )

    col2.metric(
        "Available Books",
        available_books
    )

    col3.metric(
        "Issued Books",
        issued_books
    )

    col4.metric(
        "Customers",
        total_customers
    )


    st.divider()

    st.subheader("📖 Available Books")


    available = Books.display_available_books()


    if available:

        for book in available:

            st.write(
                f"📗 **{book.title}** "
                f"— {book.author}"
            )

    else:

        st.warning(
            "No books are currently available."
        )


# ============================================================
#                  LIBRARY DETAILS
# ============================================================

elif menu == "🏛️ Library Details":

    st.title("🏛️ Library Details")

    library = Library()

    details = library.library_details()


    for key, value in details.items():

        st.write(
            f"**{key}:** {value}"
        )


# ============================================================
#                         BOOKS
# ============================================================

elif menu == "📚 Books":

    st.title("📚 Books")


    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------

    st.subheader("🔍 Search Available Books")

    search_title = st.text_input(
        "Enter book title"
    )


    if search_title:

        results = Books.search_book(
            search_title
        )


        if results:

            for book in results:

                st.info(
                    f"""
                    **Book ID:** {book.book_id}

                    **Title:** {book.title}

                    **Author:** {book.author}

                    **Category:** {book.category}
                    """
                )

        else:

            st.warning(
                "No available book found with this title."
            )


    st.divider()


    # --------------------------------------------------------
    # Display all books
    # --------------------------------------------------------

    st.subheader("📚 All Books")


    for book in Books.books_list:

        if book.available:

            st.success(
                f"📗 {book.title} — Available"
            )

        else:

            st.error(
                f"📕 {book.title} — "
                f"Issued to {book.issued_to}"
            )


# ============================================================
#                       CUSTOMERS
# ============================================================

elif menu == "👤 Customers":

    st.title("👤 Customers")


    for customer in st.session_state.customers:

        with st.expander(
            f"{customer.name} "
            f"({customer.customer_id})"
        ):

            st.write(
                f"**Phone:** {customer.phone}"
            )

            st.write(
                f"**Age:** {customer.age}"
            )

            issued_books = (
                customer.get_issued_books()
            )

            st.write(
                f"**Books Issued:** "
                f"{len(issued_books)} / 4"
            )

            st.write(
                f"**Total Fine:** "
                f"₹{customer.get_fine()}"
            )


            if issued_books:

                st.write("### Issued Books")

                for book in issued_books:

                    st.write(
                        f"📕 {book['id']} - "
                        f"{book['title']}"
                    )

            else:

                st.write(
                    "No books issued."
                )


# ============================================================
#                       ADD BOOK
# ============================================================

elif menu == "➕ Add Book":

    st.title("➕ Add New Book")


    book_id = st.number_input(
        "Book ID",
        min_value=1,
        step=1
    )

    title = st.text_input(
        "Book Title"
    )

    author = st.text_input(
        "Author"
    )

    category = st.text_input(
        "Category"
    )


    if st.button(
        "Add Book",
        type="primary"
    ):

        if not title or not author or not category:

            st.warning(
                "Please fill all fields."
            )

        else:

            # Check duplicate Book ID

            duplicate = any(
                book.book_id == book_id
                for book in Books.books_list
            )


            if duplicate:

                st.error(
                    "A book with this ID already exists."
                )

            else:

                Books(
                    book_id,
                    title,
                    author,
                    category
                )

                st.success(
                    f"Book '{title}' added successfully!"
                )


# ============================================================
#                    ADD CUSTOMER
# ============================================================

elif menu == "👤 Add Customer":

    st.title("👤 Add New Customer")


    customer_id = st.text_input(
        "Customer ID"
    )

    name = st.text_input(
        "Customer Name"
    )

    phone = st.text_input(
        "Phone Number"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )


    if st.button(
        "Add Customer",
        type="primary"
    ):

        if not customer_id or not name or not phone:

            st.warning(
                "Please fill all fields."
            )

        else:

            # Check duplicate Customer ID

            duplicate = any(
                customer.customer_id == customer_id
                for customer in
                st.session_state.customers
            )


            if duplicate:

                st.error(
                    "A customer with this ID already exists."
                )

            else:

                new_customer = Customer(
                    customer_id,
                    name,
                    phone,
                    age
                )

                st.session_state.customers.append(
                    new_customer
                )

                st.success(
                    f"Customer '{name}' added successfully!"
                )


# ============================================================
#                       ISSUE BOOK
# ============================================================

elif menu == "🔄 Issue Book":

    st.title("🔄 Issue Book")


    available_books = (
        Books.display_available_books()
    )


    if not available_books:

        st.warning(
            "No books are currently available."
        )

    elif not st.session_state.customers:

        st.warning(
            "No customers are registered."
        )

    else:

        # ----------------------------------------------------
        # Select Customer
        # ----------------------------------------------------

        customer_options = {

            f"{customer.customer_id} - "
            f"{customer.name}":
            customer

            for customer in
            st.session_state.customers
        }


        selected_customer = st.selectbox(
            "Select Customer",
            list(customer_options.keys())
        )


        customer = customer_options[
            selected_customer
        ]


        # ----------------------------------------------------
        # Select Book
        # ----------------------------------------------------

        book_options = {

            f"{book.book_id} - "
            f"{book.title}":
            book

            for book in available_books
        }


        selected_book = st.selectbox(
            "Select Book",
            list(book_options.keys())
        )


        book = book_options[
            selected_book
        ]


        # Show customer's current issue count

        issued_count = len(
            customer.get_issued_books()
        )


        st.info(
            f"Books currently issued: "
            f"{issued_count} / 4"
        )


        # ----------------------------------------------------
        # Issue Button
        # ----------------------------------------------------

        if st.button(
            "Issue Book",
            type="primary"
        ):

            success, message = (
                st.session_state.activities.issue_book(
                    customer,
                    book
                )
            )


            if success:

                st.success(message)

            else:

                st.error(message)


# ============================================================
#                       RETURN BOOK
# ============================================================

elif menu == "↩️ Return Book":

    st.title("↩️ Return Book")


    if not st.session_state.customers:

        st.warning(
            "No customers are registered."
        )

    else:

        # ----------------------------------------------------
        # Select Customer
        # ----------------------------------------------------

        customer_options = {

            f"{customer.customer_id} - "
            f"{customer.name}":
            customer

            for customer in
            st.session_state.customers
        }


        selected_customer = st.selectbox(
            "Select Customer",
            list(customer_options.keys())
        )


        customer = customer_options[
            selected_customer
        ]


        # Get customer's issued books

        issued_books = (
            customer.get_issued_books()
        )


        if not issued_books:

            st.info(
                "This customer has no issued books."
            )

        else:

            # ------------------------------------------------
            # Find actual Book objects
            # ------------------------------------------------

            customer_books = []


            for issued in issued_books:

                for book in Books.books_list:

                    if book.book_id == issued["id"]:

                        customer_books.append(book)


            # ------------------------------------------------
            # Select Book
            # ------------------------------------------------

            book_options = {

                f"{book.book_id} - "
                f"{book.title}":
                book

                for book in customer_books
            }


            selected_book = st.selectbox(
                "Select Book to Return",
                list(book_options.keys())
            )


            book = book_options[
                selected_book
            ]


            # ------------------------------------------------
            # Book Condition
            # ------------------------------------------------

            st.subheader(
                "📕 Book Condition"
            )


            damage_level = st.radio(
                "Select the condition of the returned book:",
                [
                    "No Damage",
                    "Minor Damage",
                    "Major Damage"
                ]
            )


            # Show fine

            if damage_level == "No Damage":

                st.info(
                    "Fine: ₹0"
                )

            elif damage_level == "Minor Damage":

                st.warning(
                    "Fine: ₹50"
                )

            else:

                st.error(
                    "Fine: ₹100"
                )


            # ------------------------------------------------
            # Return Button
            # ------------------------------------------------

            if st.button(
                "Return Book",
                type="primary"
            ):

                success, fine, message = (
                    st.session_state.activities.return_book(
                        customer,
                        book,
                        damage_level
                    )
                )


                if success:

                    st.success(message)

                    if fine > 0:

                        st.warning(
                            f"Damage Fine: ₹{fine}"
                        )

                    else:

                        st.info(
                            "No fine applied."
                        )

                else:

                    st.error(message)