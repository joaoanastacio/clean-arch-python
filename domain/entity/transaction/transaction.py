from domain.entity.payment_method.credit_card import CreditCard
from domain.entity.product.product import Product
from domain.entity.transaction.transaction_status import TransactionStatus

class Transaction:

    def __init__(self, identifier: str, account_id: str) -> None:
        self.__identifier = identifier
        self.__account_id = account_id
        self.__products = []
        self.__credit_card = None
        self.__status = None

    def get_transaction_id(self) -> str:
        return self.__identifier

    def get_account_id(self) -> str:
        return self.__account_id

    def get_transaction_amount(self) -> float:
        amount = 0.0

        for product in self.__products:
            amount += product.product_information.get_product_price()

        return amount

    def get_transaction_status(self) -> str:
        return self.__status

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def add_credit_card(self, credit_card: CreditCard) -> None:
        self.__credit_card = credit_card

    def add_transaction_status(self, transaction_status: TransactionStatus) -> None:
        self.__status = transaction_status
