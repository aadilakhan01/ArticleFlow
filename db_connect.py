import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aadila@sql3",
    database="blog_data"
)

# Create a cursor

c = conn.cursor()
# Function to close the database connection
def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS blogtable (
            author VARCHAR(255),
            title VARCHAR(255),
            article TEXT,
            postdate DATE
        )
    ''')
    conn.commit()

def add_data(author, title, article, postdate):
    c.execute('''
        INSERT INTO blogtable (author, title, article, postdate)
        VALUES (%s, %s, %s, %s)
    ''', (author, title, article, postdate))
    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title = %s', (title,))
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable WHERE author = %s', (author,))
    data = c.fetchall()
    return data

def delete_data(title):
    c.execute('DELETE FROM blogtable WHERE title = %s', (title,))
    conn.commit()

def close_connection():
    conn.close()

