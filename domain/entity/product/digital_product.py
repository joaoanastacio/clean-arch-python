from datetime import datetime

from product_information import ProductInformation
from product_tax import ProductTax

class DigitalProduct:

    def __init__(self, product_information: ProductInformation, product_tax: ProductTax) -> None:
        self.product_information = product_information
        self.product_tax = product_tax
        self.available = False
        self.customer_limit = 1000
        self.created_on = datetime.now()

    def make_available(self) -> None:
        self.available = True
    
    def change_customer_limit(self, new_customer_limit: int) -> None:
        if new_customer_limit < 0:
            raise ValueError("New customer limit is not valid. It must be greater or equal to zero")
        self.customer_limit = new_customer_limit
