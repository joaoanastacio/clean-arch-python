from typing import Protocol

from domain.entity.transaction.transaction import Transaction

class PaymentGateway(Protocol):

    def pay(self, transaction: Transaction) -> None:
        ...
        