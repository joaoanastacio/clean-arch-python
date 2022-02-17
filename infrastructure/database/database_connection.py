from typing import Protocol

class DatabaseConnection(Protocol):

    def connect(self): 
        ...