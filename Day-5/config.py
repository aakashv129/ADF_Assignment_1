import mysql.connector


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port="3307",
    database="python_connection"
)