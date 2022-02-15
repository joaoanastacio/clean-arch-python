from typing import Protocol

from domain.entity.transaction.transaction import Transaction

class PaymentProcessor(Protocol):

    def pay(self, transaction: Transaction) -> bool:
        ...