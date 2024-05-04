import sqlite3
from sqlite3 import Error


def get_connection():
    return sqlite3.connect("library.db")


def migrate():
    try:
        connection = get_connection()

        if connection is not None:
            cursor = connection.cursor()

            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute(
                """
CREATE TABLE IF NOT EXISTS book(
  code TEXT PRIMARY KEY,
  loaned_to_id TEXT DEFAULT(NULL),
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  published DATE NOT NULL,
    
  FOREIGN KEY (loaned_to_id)
    REFERENCES user (id) 
);"""
            )

            cursor.execute(
                """
CREATE TABLE IF NOT EXISTS user(
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  contact TEXT NOT NULL
);
"""
            )
    except Error as e:
        print(e)
