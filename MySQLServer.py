import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server (without specifying a database)
        mydb = mysql.connector.connect(
            host="localhost",          # Update if needed
            user="root",      # Replace with your MySQL username
            password="your_password"   # Replace with your MySQL password
        )
        mycursor = mydb.cursor()

        # Try to create the database
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("✅ Database 'alx_book_store' created successfully!")

        except mysql.connector.Error as err:
            print(f"❌ Failed to create database: {err}")

        # Close cursor and connection
        mycursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        print(f"❌ Error connecting to MySQL: {err}")

if __name__ == "__main__":
    create_database()
