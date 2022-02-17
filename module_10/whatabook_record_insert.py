import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "whatabook_user",
    "password": "MySQLIsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

# insert store
cursor.execute("INSERT INTO store(locale) VALUES ('500 Starfish Dr, Blacksburg, VA, 24060')");

# insert books
cursor.execute("INSERT INTO book(book_name, author, details) VALUES ('Water for Elephants','Sara Gruen','Best book ever')");
cursor.execute("INSERT INTO book (book_name, author) VALUES ('The Maze Runner','James Dashner')");
cursor.execute("INSERT INTO book (book_name, author) VALUES ('The Maze Runner: Scorch Trials','James Dashner')");
cursor.execute("INSERT INTO book (book_name, author) VALUES ('The Maze Runner: The Death Cure','James Dashner')");
cursor.execute("INSERT INTO book (book_name, author) VALUES (' Twilight','Stephanie Meyer')");
cursor.execute("INSERT INTO book (book_name, author) VALUES (' Twilight : New Moon','Stephanie Meyer')");
cursor.execute("INSERT INTO book (book_name, author) VALUES (' Twilight : Eclipse','Stephanie Meyer')");
cursor.execute("INSERT INTO book (book_name, author) VALUES ('Of Mice and Men','John Steinbeck')");
cursor.execute("INSERT INTO book (book_name, author) VALUES ('The Prince','Niccolo Machiavelli')");

# insert users
cursor.execute("INSERT INTO user (first_name, last_name) VALUES ('Beth','Williams')");
cursor.execute("INSERT INTO user (first_name, last_name) VALUES ('Henry','Smith')");
cursor.execute("INSERT INTO user (first_name, last_name) VALUES ('Lauren','Baker')");

# wishlist items
cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Beth'), (SELECT book_id FROM book WHERE book_name = 'Water for Elephants'))");
cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Henry'), (SELECT book_id FROM book WHERE book_name = 'The Maze Runner'))");
cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES((SELECT user_id FROM user WHERE first_name = 'Lauren'), (SELECT book_id FROM book WHERE book_name = 'Of Mice and Men'))");

try:
    # db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press Any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

