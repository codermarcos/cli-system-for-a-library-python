import time

from database import get_connection


class Book:
    @staticmethod
    def save(book):
        connection = get_connection()

        cursor = connection.cursor()

        books = [(str(hash(time.time() + i)), book["title"], book["published"], book["author"]) for i in range(0, int(book["copies"]))]

        query = "INSERT INTO book (code, title, published, author) VALUES (?, ?, ?, ?)"

        cursor.executemany(query, books)

        connection.commit()

    @staticmethod
    def search(filter):
        connection = get_connection()

        cursor = connection.cursor()

        query = "SELECT code, title, author, published, COUNT(*) as total, COUNT(loaned_to_id) as unavailable FROM book"

        if filter != None and len(filter) != 0:
            fields = ["code", "title", "published", "author"]
            conditions = [f"{field} LIKE '%{filter}%'"for field in fields]
            query += f" WHERE {" OR ".join(conditions)}"

        query += " GROUP BY title"

        cursor.execute(query)

        return cursor.fetchall()
    
    @staticmethod
    def search_only_availables(filter):
        connection = get_connection()

        cursor = connection.cursor()

        query = "SELECT code, title, author, published, COUNT(*) as availables FROM book WHERE loaned_to_id IS NULL"

        if filter != None and len(filter) != 0:
            fields = ["title", "published", "author"]
            conditions = [f"{field} LIKE '%{filter}%'"for field in fields]
            query += f" AND ({" OR ".join(conditions)})"

        query += " GROUP BY title"

        cursor.execute(query)

        return cursor.fetchall()
    
    @staticmethod
    def search_books_borrowed(user_id, filter):
        connection = get_connection()

        cursor = connection.cursor()

        query = f"SELECT code, title, author, published FROM book WHERE loaned_to_id = '{user_id}'"

        if filter != None and len(filter) != 0:
            fields = ["title", "published", "author"]
            conditions = [f"{field} LIKE '%{filter}%'"for field in fields]
            query += f" AND ({" OR ".join(conditions)})"

        cursor.execute(query)

        return cursor.fetchall()
    

    @staticmethod
    def update(book):
        connection = get_connection()

        cursor = connection.cursor()

        query = "UPDATE book SET loaned_to_id = ? WHERE code = ?"

        cursor.execute(query, (book["loaned_to_id"], book["code"]))

        connection.commit()

