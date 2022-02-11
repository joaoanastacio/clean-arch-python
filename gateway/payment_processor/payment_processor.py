from typing import Protocol

class PaymentProcessor(Protocol):

    def pay(self, transaction) -> bool:
        ...