from typing_extensions import Self

class MySqlConnection(object):
    
    __connection = None

    def __new__(cls: type[Self]) -> Self:
        if cls.__connection is None:
            cls.__connection = super(MySqlConnection, cls).__new__(cls)
        return cls.__connection
