from typing import Protocol

class Product(Protocol):

    def make_available(self) -> None:
        ...

    def change_customer_limit(self, new_customer_limit: int) -> None:
        ...
        