# import psycopg2


# #  connect to the database
# connection = psycopg2.connect(dbname="stsdb", user="postgres", password="postgres", host="localhost", port="5432")
# cursor = connection.cursor()

# # write function to drop table
# def drop_table(table_name):
#     pass


# # create a table
# cursor.execute("""CREATE TABLE IF NOT EXISTS students (
#     id SERIAL PRIMARY KEY, 
#     name VARCHAR(50) NOT NULL, 
#     student_id CHAR(8) UNIQUE NOT NULL, 
#     program TEXT NOT NULL);"""
# )


# # Insert data
# # cursor.execute("""INSERT INTO students (name, student_id, program) 
# #     VALUES ('Kofi', '12345678', 'Backend')
# # """)

# cursor.execute("""INSERT INTO students (name, student_id, program) 
#     VALUES (%s, %s, %s)
# """, ('Ama','87654321', 'Frontend'))

# # def st_db(student):  
# #     cursor.execute("""INSERT INTO students (name, student_id, program) 
# #         VALUES (%s, %s, %s)
# #     """, (student["name"], student["student_id"], student["program"]))

# connection.commit()

# cursor.close()
# connection.close()




# ======================================================================================================

#communication between db and python can be done through packages(ibrary)
#psycopg allows you to connect Postgres, 
import psycopg2

connection = psycopg2.connect(dbname= "stsdb", user = "postgres", password = "postgres", host = "localhost", port="5432")
cursor = connection.cursor()

def create_table(table_name):
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), published_date DATE)", )

# create_table('books')

def insert_data(title, author, published_date):
    try:

        # Correct SQL syntax for inserting data
        insert_query = "INSERT INTO books (title, author, published_date) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (title, author, published_date))

        # Commit the transaction
        connection.commit()
        print(f"✅ Book '{title}' by {author} added successfully!")

    except Exception as e:
        print(f"❌ Error inserting data: {e}")

    finally:
        cursor.close()
        connection.close()

# Example Usage:
# insert_data("Things Fall Apart", "Peggy Oppong", "2020-10-10")


def add_book(title,author,published_date):
    cursor.execute("SELECT title, author FROM books")
    all_books = cursor.fetchall()
    for book in all_books:
        if title in book and author in book:
            print("Book already exists")
            return
    #make data persistent by committing
    connection.commit()
    cursor.close()
    #used to close connection
    connection.close()


def remove_book(title, author):
    cursor.execute("SELECT * FROM books WHERE title = %s and author = %s", (title,author))
    book = cursor.fetchone()


    if book:
        #Delete book if found
        cursor.execute("DELETE FROM books where title = %s and author = %s", (title,author))
        connection.commit()
        print(f"the book '{title}' removed successfully")

    else:
        print(f"the book '{title}' not found")

# remove_book("The Great Gatsby", "F. Scott Fitzgerald")

def view_books(size):
    cursor.execute("SELECT id FROM books LIMIT %s", [size])
    all_books = cursor.fetchall()

    print(all_books)

view_books(5)

def view_book(id):
    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()
    print(book)

# view_book(2)

def update_book(id, title, author, published_date):
    cursor.execute("UPDATE books SET title = %s, author = %s, published_date = %s WHERE id = %s", (title, author, published_date, id))

    connection.commit()
    view_book(id)

update_book(2, 'Second Chance', 'Salvador', '2000-10-10')


