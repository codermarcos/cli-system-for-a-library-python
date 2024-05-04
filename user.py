import time

from database import get_connection


class User:
    @staticmethod
    def save(user):
        connection = get_connection()

        cursor = connection.cursor()

        query = f"""INSERT INTO user (id, name, contact) VALUES (?, ?, ?)"""

        cursor.execute(query, (str(hash(time.time())), user["name"], user["contact"]))

        connection.commit()

    @staticmethod
    def search(filter):
        connection = get_connection()

        cursor = connection.cursor()

        query = "SELECT id, name, contact FROM user"

        if filter != None and len(filter) != 0:
            fields = ["id", "name", "contact"]
            conditions = [f"{field} LIKE '%{filter}%'"for field in fields]
            query += f" WHERE {" OR ".join(conditions)}"
            
        cursor.execute(query)

        return cursor.fetchall()
