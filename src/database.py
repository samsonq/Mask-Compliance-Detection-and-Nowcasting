import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Database:
    """
    Manages database storage to insert and select mask compliance events predicted by the
    computer vision model.
    """
    def __init__(self):
        """
        Establish connection to a MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='Rebellion',
                                                      user='root',
                                                      password='')
            self.cursor = self.connection.cursor()
        except Error as error:
            print("Failed to insert record into table {}".format(error))

    def insert(self, query):
        """
        Inserts event into database.
        :param query: insert query
        """
        self.cursor.execute(query)
        self.connection.commit()

    def select(self, query):
        """
        Retrieves event from database.
        :param query: select query
        :return: event records
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        """
        Close connection to database.
        """
        self.cursor.close()
