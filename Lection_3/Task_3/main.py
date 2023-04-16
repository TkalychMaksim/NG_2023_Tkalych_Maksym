global library
library = {}  # Creating dictionary to store books


def main():
    while True:
        print("Welcome to Library <3")
        print("Choose the operation from list:\n [1] Add new book\n [2] Delete book\n [3] Edit existing book"
              "\n [4] Find a book ")
        operation = input("Chosen operation: ")
        match operation:
            case "Add new book" | "1":
                new_book()
            case "Delete book" | "2":
                delete_book()
            case "Edit existing book" | "3":
                edit_book()
            case "Find a book" | "4":
                find_book()


def new_book():
    print("Fill in information about the book:")
    book_name = input("Book title: ")
    book_author = input("Author: ")
    book_pages = int(input("Number of pages: "))
    book_genre = input("Genre: ")
    book_binding = input("Book binding: ")
    print('<L> <I> <B> <R> <A> <R> <Y>')
    print()
    book = {
        "Title": book_name,
        "Author": book_author,
        "Pages": book_pages,
        "Genre": book_genre,
        "Binding": book_binding

    }
    book_key = book_name
    library[book_key] = book


def delete_book():
    print(f"Book list: {list(library.keys())} ")
    book_title = input("Enter the title of book you want to delete: ")
    if book_title in library.keys():
        del library[book_title]
        print(f"Success. Book with title {book_title} was deleted.")
    else:
        print("Error. Book with this title not found.")
    print('<L> <I> <B> <R> <A> <R> <Y>')
    print()


def edit_book():
    editing_book = input(f"Choose the book from list {list(library.keys())}: ")
    param = input(f"Choose the param:\n {list(library[editing_book].keys())} ")
    new_value = input(f"Enter the new value of {param}: ")
    library[editing_book][param] = new_value
    print(f"Success!. The new value of {param} is '{new_value}'")
    print('<L> <I> <B> <R> <A> <R> <Y>')
    print()


def find_book():
    print(f'Book list: {list(library.keys())}')
    search_title = input("Enter the title of book you are interested in: ")
    if search_title in library.keys():
        print("The book was successfully found!")
        print(library[search_title])
    else:
        print("Error. Book with this title not found")
    print('<L> <I> <B> <R> <A> <R> <Y>')
    print()


main()
