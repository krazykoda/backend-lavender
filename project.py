# Project Assignment: Book Title Library
# Objective:
# Create a simple Book Title Library program that allows users to manage a list of book titles.

# Requirements:
# Store book titles using a list.
# Provide a menu where users can choose different actions.
# Allow users to:
# Add a new book to the list.
# Remove a book from the list.
# View all books in the library.
# Exit the program.
# Validate user input to ensure the program does not crash if incorrect input is given.
# Use only:
# Variables
# Lists
# Loops (while and for)
# Conditionals (if-else)
# input() and print()

#OUTPUT
# Welcome to the Book Title Library!

# Choose an option:
# 1. Add a Book
# 2. Remove a Book
# 3. View All Books
# 4. Exit

# Enter your choice: 1
# Enter the book title: Harry Potter
# "Harry Potter" has been added to the library.

# Enter your choice: 3
# Books in the Library:
# - Harry Potter

# Enter your choice: 2
# Enter the book title to remove: Harry Potter
# "Harry Potter" has been removed from the library.

# Enter your choice: 4
# Goodbye!
books = ['Harry Potter']

print("Welcome to the Book Title Library!")

print("Choose an option:\n 1. Add a Book\n 2. Remove a Book\n 3. View All Books\n 4. Exit")

while True: 
    user_input = input("Enter your choice (1-4) :  ")
    
    if user_input == '1':
        # Add a book or books
        add_books = input("Enter the book title separated by a comma: ")

        add_books = add_books.split(', ')
        books.extend(add_books)

        s = ""

        for book in books:
            s = s + book + ", "

        print(s)
        # print(f'{", ".join(add_books)} has been added to the library')

       
# Delete a book
# title = input("Enter the book title separated by a comma: ")

# if title in books: 
#     books.remove(title)
#     print(f'{title} has been removed from the library')

# else: 
#     print(f'{title} is not in the library')


# View all books 
# print("Books in the Library:")

# for book in books:
#     print(f'- {book}')