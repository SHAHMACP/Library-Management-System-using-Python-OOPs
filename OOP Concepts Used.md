# 🧠 OOP Concepts Used

This project is mainly designed to demonstrate **Object-Oriented Programming in Python**.

### 1. Classes and Objects

Different real-world entities are represented using classes such as:

```python
Library
Book
Customer
Activity
```

Objects are created from these classes to manage library data.

---

### 2. Encapsulation

Customer-specific information and issued books are managed using encapsulation.

Example:

```python
self.__issued_books
```

The double underscore is used to create a private attribute.

---

### 3. Inheritance

Classes are related using inheritance where appropriate.

Example:

```python
class Customer(Library):
    ...
```

This demonstrates how one class can inherit properties and methods from another class.

---

### 4. Abstraction

The project uses Python's `ABC` and `abstractmethod` concepts to demonstrate abstraction.

Example:

```python
from abc import ABC, abstractmethod
```

An abstract class defines common functionality that can be implemented by child classes.

---

### 5. Class Variables

Common library information is maintained using class variables.

Example:

```python
class Library:
    library_name = "Central Library"
    library_location = "Calicut"
    starting_year = 1995
```

---

### 6. Methods

Different operations are implemented using methods such as:

```python
add_book()
issue_book()
return_book()
display_books()
library_details()
```

This keeps the application organized and makes the code reusable.

---

# 🏗️ Project Structure

```text
Library-Management-System/
│
├── library.py
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── screenshot.png
```

### `library.py`

Contains the main OOP implementation.

It includes classes such as:

```text
Library
Book
Customer
Activity
```

and their related attributes and methods.

### `app.py`

Contains the **Streamlit user interface**.

It connects the OOP classes with the web interface and handles user interactions.

### `requirements.txt`

Contains the Python packages required to run the project.

Example:

```text
streamlit
```

---

# ⚙️ Technologies Used

| Technology      | Purpose                  |
| --------------- | ------------------------ |
| 🐍 Python       | Programming language     |
| 🧱 OOP          | Application architecture |
| 🎈 Streamlit    | Web interface            |
| 📦 ABC Module   | Abstraction              |
| 💻 VS Code      | Development environment  |
| 🔧 Git & GitHub | Version control          |

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System.git
```

Move into the project directory:

```bash
cd Library-Management-System
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

# 📖 How the Application Works

### Step 1 — Home

The dashboard displays the current library statistics.

```text
Total Books
Available Books
Issued Books
Customers
```

### Step 2 — Library Details

View information about the library such as:

* Library name
* Location
* Starting year
* Librarian

### Step 3 — Books

View the books currently available in the library.

### Step 4 — Add Book

Add a new book by entering details such as:

```text
Book ID
Title
Author
Category
```

### Step 5 — Add Customer

Add a customer by providing details such as:

```text
Customer ID
Name
Phone
Age
```

### Step 6 — Issue Book

Select a customer and an available book to issue it.

The system automatically updates the book status.

### Step 7 — Return Book

Return an issued book and provide the required return information.

The system updates the book availability and calculates the applicable fine when required.

---

# 🎯 Learning Objectives

This project helps demonstrate:

* How to design a real-world application using Python
* How classes and objects work
* How inheritance can be used
* How abstraction can be implemented
* How encapsulation protects data
* How different classes can interact with each other
* How Python OOP can be connected with a web interface
* How Streamlit can be used to create interactive applications

---

# 🔮 Future Improvements

The project can be extended with additional features such as:

* 🔐 Login and authentication
* 🗄️ Database integration using SQLite/MySQL
* 📊 Advanced reports and analytics
* 🔍 Advanced book search and filtering
* 📅 Due-date management
* 💰 Automatic late-return fine calculation
* 📧 Email notifications
* 👥 Admin and student roles
* 📱 Responsive UI improvements
* ☁️ Deployment using Streamlit Community Cloud

---

# 👩‍💻 Author

**Shahma**

Data Science Trainer | Python | Data Science | AI | OOP

---

# ⭐ Acknowledgement

This project was developed as a practical demonstration of **Python Object-Oriented Programming and Streamlit application development**.

````
