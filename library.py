# Book Class
# This class represents a book with attributes such as title, author, and the number of copies available.

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


# Library Class
# This class manages the collection of books and users, and it includes methods for adding books,
#  displaying books, borrowing books, returning books, and managing users.



class Library:
    def __init__(self):
        self.books = []
        self.users = []

#add_book method: Creates a new book object and adds it to the library's book list.

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)
        print(f'Added "{title}" by {author} ({copies} copies).')

#display_books method: Displays all available books in the library. If no books are available, it prints a message.

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nAvailable books:")
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Copies: {book.copies}')

#borrow_book method: Allows a user to borrow a book if it is available. If the book is available,
#  it decreases the number of copies by one and adds the book to the user's borrowed list.

    def borrow_book(self, user, title):
        for book in self.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                user.borrowed_books.append(book.title)
                print(f'{user.name} borrowed "{book.title}".')
                return
        print(f'Sorry, "{title}" is not available.')

#return_book method: Allows a user to return a borrowed book. If the user has the book,
#  it increases the number of copies by one and removes the book from the user's borrowed list.

    def return_book(self, user, title):
        if title in user.borrowed_books:
            for book in self.books:
                if book.title == title:
                    book.copies += 1
                    user.borrowed_books.remove(title)
                    print(f'{user.name} returned "{book.title}".')
                    return
        print(f'{user.name} does not have "{title}" borrowed.')

#add_user method: Adds a new user to the library.

    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f'Added user "{name}".')

#display_users method: Displays all registered users and the books they have borrowed.
#  If no users are registered, it prints a message.

    def display_users(self):
        if not self.users:
            print("No users registered in the library.")
            return
        print("\nRegistered users:")
        for user in self.users:
            print(f'Name: {user.name}, Borrowed Books: {", ".join(user.borrowed_books) or "None"}')

#User Class
# This class represents a user with a name and a list of borrowed books.

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

#Main Function
# The main function provides a menu-driven interface for interacting with the library management system.
# Menu Interface:
# Option 1: Adds a new book to the library.
# Option 2: Displays all available books in the library.
# Option 3: Allows a user to borrow a book. It first checks if the user exists, then proceeds with borrowing.
# Option 4: Allows a user to return a book. It first checks if the user exists, then proceeds with returning.
# Option 5: Adds a new user to the library.
# Option 6: Displays all registered users and their borrowed books.
# Option 7: Exits the system.
# Invalid Choice: Prompts the user to enter a valid choice.

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Add User")
        print("6. Display Users")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            user_name = input("Enter your name: ")
            title = input("Enter book title to borrow: ")
            user = next((u for u in library.users if u.name == user_name), None)
            if user:
                library.borrow_book(user, title)
            else:
                print(f'User "{user_name}" not found.')
        elif choice == '4':
            user_name = input("Enter your name: ")
            title = input("Enter book title to return: ")
            user = next((u for u in library.users if u.name == user_name), None)
            if user:
                library.return_book(user, title)
            else:
                print(f'User "{user_name}" not found.')
        elif choice == '5':
            name = input("Enter user name: ")
            library.add_user(name)
        elif choice == '6':
            library.display_users()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
