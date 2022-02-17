# Before doing this program, create the database (this one is named Shopping) in the MySQL command line client by typing CREATE DATABASE Shopping; into the command client 
# after creating the database, create the database user (named shopping_user) by typing the following into the command client >>>
#   DROP USER IF EXISTS ‘shopping_user’@’localhost’;
#   CREATE USER ‘shopping_user’@’localhost’ IDENTIFIED WITH mysql_native_password BY ‘MySQL8IsGreat!’;
#   GRANT ALL PRIVILEGES ON Shopping.*TO ‘shopping_user’@’localhost’;
#   After following the above steps, type the following program to connect 

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "shopping_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "Shopping",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
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