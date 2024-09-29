# Library Management System using Tuples

# Book information stored in tuples (title, author, published year)
library_books = [
    ("2", "F. Scott Fitzgerald", 1925),
    ("1984", "George Orwell", 1949),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("The Catcher in the Rye", "J.D. Salinger", 1951),
    ("Pride and Prejudice", "Jane Austen", 1813)
]

# Function to Add a New Book
def add_book(title, author, year):
    new_book = (title, author, year)
    library_books.append(new_book)
    print(f"'{{title}}' by {{author}} (Published: {{year}}) added to the library.")

# Function to Search a Book by Title
def search_book(title):
    for book in library_books:
        if book[0].lower() == title.lower():
            print(f"Found: '{{book[0]}}' by {{book[1]}} (Published: {{book[2]}})")
            return
    print(f"Book '{{title}}' not found.")

# Function to Count Total Books
def count_books():
    print(f"Total books in the library: {{len(library_books)}}")

# Function to List All Books
def list_books():
    print("Books in the library:")
    for book in library_books:
        print(f"'{{book[0]}}' by {{book[1]}} (Published: {{book[2]}})")

# Library Menu to Interact with User
def library_menu():
    while True:
        print("\\nLibrary Management System")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Count total books")
        print("4. List all books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter published year: "))
            add_book(title, author, year)

        elif choice == '2':
            title = input("Enter book title to search: ")
            search_book(title)

        elif choice == '3':
            count_books()

        elif choice == '4':
            list_books()

        elif choice == '5':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Start the Library Management System
library_menu()