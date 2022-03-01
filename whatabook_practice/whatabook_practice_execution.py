import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabookpractice_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook_practice",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()






def show_menu():  # method that displays main menu
    print("\n\nMain Menu : ")
    print("          1. View Books\n          2. View Store Locations\n          3. My Account ")

    try:
        user_input = int(input("      Enter 1 to view books, enter 2 to view store locations, enter 3 to go to your account, and enter 4 to exit >>> "))

        return user_input
    except ValueError:
        print("\n The number you entered was not an option - PROGRAM TERMINATED \n")
        sys.exit(0)






def show_books(_cursor):   # method that displays all books at What-A-Book

    _cursor.execute("SELECT book_id, book_name, author, details FROM book")

    books = _cursor.fetchall()

    print("\n\n<<<<  SHOWING BOOKS  >>>>\n")
    i =  0
    while i < 1:
        for book in books:
            print("  Book ID: {}     Book Name: {}     Author: {}     Details: {}\n".format(book[0], book[1], book[2], book[3]))
        i += 1





def show_locations(_cursor):   # method that shows different store locations
    _cursor.execute("SELECT store_id, locale FROM store")
    locations = _cursor.fetchall()
    print("\n\n<<<<  SHOWING STORE LOCATIONS  >>>>\n")
    i = 0
    while i < 1:
        for location in locations:
            print("  Locale: {}\n".format(location[1]))
        i += 1






def validate_user(_cursor):    # method that validates user
    try:
        user_id = int(input('\n      Enter your user id (1, 2, or 3) >>> '))

        if user_id < 0 or user_id > 3:
            print("\n  user id invalid - PROGRAM TERMINATED\n")
            sys.exit(0)
        if user_id == 1:
            _cursor.execute("SELECT first_name FROM user WHERE user_id = 1")
            name = _cursor.fetchall()
            for x in name:
                print("\n\nWelcome, {}".format(x[0]))
        if user_id == 2:
            _cursor.execute("SELECT first_name FROM user WHERE user_id = 2")
            name = _cursor.fetchall()
            for x in name:
                print("\n\nWelcome, {}".format(x[0]))
        if user_id == 3:
            _cursor.execute("SELECT first_name FROM user WHERE user_id = 3")
            name = _cursor.fetchall()
            for x in name:
                print("\n\nWelcome, {}".format(x[0]))

        return user_id
    except ValueError:
        print("\n  user id invalid - PROGRAM TERMINATED\n")
        sys.exit(0)





def show_account_menu():   # method that lets the user view wishlist/add books to wishlist
    try:
        print("\n>>>>  Account Menu  >>>>")
        print("          1. Wishlist\n          2. Add Book\n          3. Main Menu")
        user_input = int(input("Enter 1 for Wishlist, enter 2 to Add Book, enter 3 for Main Menu >>> "))

        return user_input

    except ValueError:
        print(' entry invalid - PROGRAM TERMINATED')
        sys.exit(0)





def show_wishlist (_cursor, _user_id):    # method that shows the user their wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    print("\n\n<<<<  SHOWING WISHLIST ITEMS  >>>>\n")

    for book in wishlist:
        print("          Book Name : {}\n          Author : {}\n".format(book[4], book[5]))





def show_books_to_add(_cursor, _user_id):    # method that shows the user what books are available to add to the wishlist

    books_not_in_wishlist = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    
    print(books_not_in_wishlist)

    _cursor.execute(books_not_in_wishlist)

    available_books_to_add = _cursor.fetchall()

    print("\n <<<< SHOWING BOOKS AVAILABLE TO ADD TO WISHLIST >>>> ")
    
    for book in available_books_to_add:
        print("  Book_id : {}\n  Title : {}\n".format(book[0], book[1]))





def add_book_to_wishlist(_cursor, _user_id, _book_id):   # method that allows the user to add more books to their wishlist
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES ({}, {})".format(_user_id, _book_id))





try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("\n <<<<    What-A-Book Store    >>>>")

    selection = show_menu()

    while selection != 4:  # selection 4 ends the program

        if selection == 1:    # selection 1 will show user books
            show_books(cursor)
            #break


        if selection == 2:   # selection 2 will show store locations
            show_locations(cursor)
            #break


        if selection == 3:  # selection 3 will show the user their account menu
            user_id_option = validate_user(cursor)
            account = show_account_menu()

            while account != 3:  # account option 3 will take user back to main menu
                    
                if account == 1:  # account option 1 will show the user their wishlist
                        show_wishlist(cursor, user_id_option)
                    
                if account == 2:   # account option 2 will let the user add books to their wishlist
                    show_books_to_add(cursor, user_id_option)
                    book_id = int(input("\n        Enter the book ID of the book you would like to add to your wishlist: "))
                    add_book_to_wishlist(cursor, user_id_option, book_id)
                    db.commit()   # commit the changes to the whatabook database
                    print("\n Book ID : {} was added to your wishlist".format(book_id))


                    

                if account < 0 or account > 3:  # for user account option
                    print("\n Invalid account option, retry >>> ")
                account = show_account_menu()


        if selection < 0 or selection > 4:  # for main menu options
                print("entry invalid, retry >>> ")


        selection = show_menu()
    

    print(" >>>> END OF PROGRAM <<<< ")



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close