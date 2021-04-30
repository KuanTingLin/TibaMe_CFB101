from pathlib import Path
import sqlite3
import os


class DBConnector:
    def __init__(self, database):
        self.connector = None
        self.database = database
        self.get_connection(database)

    def get_connection(self, database=None):
        if database or (self.connector is None):
            self.connector = sqlite3.connect(database)
            self.connector.row_factory = DBConnector.dict_factory
            self.connector.execute("PRAGMA foreign_keys = ON")
        return self.connector

    def close_connection(self):
        if self.connector is not None:
            self.connector.close()

    @staticmethod
    def remove_db(self):
        if os.path.isfile(self.database):
            os.remove(self.database)

    @staticmethod
    def dict_factory(cursor, row):
        return {column[0]: row[index] for index, column in enumerate(cursor.description)}


def main():
    database = "test.db"
    db_connector = DBConnector(database)
    connection = db_connector.get_connection()
    cursor = connection.cursor()
    # # CUD
    query_string = '''INSERT INTO test
                      VALUES ({}, {}, '{}');'''.format(1236, 200, 'juice')
    cursor.execute(query_string)
    connection.commit()

    # # R
    query_string = '''SELECT *
                      FROM test
                      WHERE price > 20;'''
    cursor.execute(query_string)
    # print(cursor.fetchall())
    # print(cursor.description)
    db_connector.close_connection()


if __name__ == "__main__":
    main()

