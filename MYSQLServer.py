import mysql.connector

        # Connect to MySQL server
mydb = mysql.connector.connect(
      
     host="localhost",
     user="root",
     password="Betsyme234!",
     port=3307
 )
cursor = mydb.cursor()

def create_database():
        try:
              query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
              cursor.execute(query)
              mydb.commit()
              print("Database 'alx_book_store' created successfully!")

        
        except mysql.connector.Error as err:
         
         print(f"Error: {err}")
        
        finally:
        # Close the connection
          if 'mydb' in locals() and mydb.is_connected():
            cursor.close()
            mydb.close()

if __name__ == "__main__":
    create_database()


