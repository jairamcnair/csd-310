import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "shopping_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "Shopping",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

cursor.execute("CREATE TABLE Customer (customer_id	INT	 NOT NULL   AUTO_INCREMENT, first_name	   VARCHAR(75)   NOT NULL, last_name  VARCHAR(75)  NOT NULL  PRIMARY KEY(customer_id));")
cursor.execute("CREATE TABLE Products (product_id  INT  NOT NULL   AUTO_INCREMENT, product_name   VARCHAR(200)  NOT NULL, description VARCHAR(500) PRIMARY KEY(product_id));")
cursor.execute("CREATE TABLE Orders (order_id   INT   NOT NULL   AUTO_INCREMENT, customer_id  INT  NOT NULL, product_id   INT  NOT NULL, PRIMARY KEY(order_id), CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES Products(product_id), CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customer(customer_id));")


cursor.execute("SHOW TABLES;")

# code is wrong so far...