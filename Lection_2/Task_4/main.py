print("Hello! You are welcome in our library <3")
library = {}
while True:
    print("Choose the operation from list:\n *Add new book\n *Delete book\n *Edit existing book\n *Find a book ")
    books = input("Chosen operation: ")
    match books:
        case "Add new book":
            book_name = input("Enter the name of the book you want to add: ")
            book_author = input("Enter the name of the author of this book: ")
            book_pages = int(input("Enter the number of pages: "))
            book_genre = input("Enter the book genre: ")
            book_binding = input("Enter the book binding: ")
            print('<L> <I> <B> <R> <A> <R> <Y>')

            book = {
                "Title": book_name,
                "Author": book_author,
                "Pages": book_pages,
                "Genre":  book_genre,
                "Binding": book_binding

            }
            key = book_name
            library[key] = book

        case "Delete book":
            print(f"Books list: {list(library.keys())}")
            book_name = input("Enter the name of book you want to delete: ")
            del library[book_name]
            print('<L> <I> <B> <R> <A> <R> <Y>')

        case "Edit existing book":
            editing_book = input(f"Choose the book: \n Books list: {list(library.keys())} ")
            param = input(f"Choose the param:\n {list(library[editing_book].keys())} ")
            new_value = input(f"Enter the new value of {param}: ")
            library[editing_book][param] = new_value
            print(f"Success!. The new value of {param} is '{new_value}'")
            print('<L> <I> <B> <R> <A> <R> <Y>')

        case "Find a book":
            print(f'Book list: {list(library.keys())}')
            search_title = input("Enter the title of book you are interested in: ")
            if search_title in library.keys():
                print("The book was successfully found!")
                print(library[search_title])
            else:
                print("Error. Book with this title not found")
            print('<L> <I> <B> <R> <A> <R> <Y>')

