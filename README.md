
# Library Management System

## Overview

The **Library Management System** is a Python-based application designed to manage a library's operations. It allows users to manage books, track borrowed and returned books, and maintain user accounts through a menu-driven interface.

## Features

1. **Book Management**:
   - Add new books to the library.
   - Display all available books.
   - Borrow and return books.

2. **User Management**:
   - Register new users.
   - Display registered users and their borrowed books.

3. **Menu-Driven Interface**:
   - Interactive prompts for users to navigate through the system.

## Classes and Methods

### `Book`
Represents a book with attributes:
- `title`: The title of the book.
- `author`: The author of the book.
- `copies`: The number of available copies.

### `Library`
Handles library operations:
- `add_book(title, author, copies)`: Adds a new book.
- `display_books()`: Displays all available books.
- `borrow_book(user, title)`: Allows a user to borrow a book.
- `return_book(user, title)`: Allows a user to return a book.
- `add_user(name)`: Adds a new user.
- `display_users()`: Displays all registered users and their borrowed books.

### `User`
Represents a user with attributes:
- `name`: The name of the user.
- `borrowed_books`: A list of borrowed book titles.

## How to Use

1. **Run the Application**:
   - Execute the `library.py` file to start the system.

2. **Menu Options**:
   - `1`: Add a new book to the library.
   - `2`: Display all available books.
   - `3`: Borrow a book by an existing user.
   - `4`: Return a borrowed book.
   - `5`: Add a new user.
   - `6`: Display all registered users.
   - `7`: Exit the system.

3. **Interactive Prompts**:
   - Follow the on-screen instructions to navigate the system.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. Clone the repository or download the `library.py` file.
2. Navigate to the directory containing `library.py`.

## Running the Program

```bash
python library.py
```

## Example Usage

- **Add a Book**: Enter the title, author, and number of copies.
- **Borrow a Book**: Enter the user's name and the title of the book.
- **Return a Book**: Enter the user's name and the title of the book to return.

