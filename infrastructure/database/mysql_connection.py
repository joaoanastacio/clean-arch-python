import mysql.connector
from mysql.connector import errorcode

class MySqlConnection:

    __connection = None

    def connect(self):
        if not self.__connection:
            try:
                config = {
                    "user":"clean-arch-user",
                    "password": "clean-arch-pwd",
                    "host": "127.0.0.1",
                    "database": "clean-arch",
                    "raise_on_warnings": False
                }
                self.__connection =  mysql.connector.connect(**config)

            except mysql.connector.Error as error:
                if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif error.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(error)
        else:
            return self.__connection
