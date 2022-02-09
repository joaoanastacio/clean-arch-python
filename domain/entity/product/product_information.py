class ProductInformation:

    def __init__(self, product_name: str, product_description: str, product_image: str, product_price: float) -> None:
        self.product_name = product_name
        self.product_description = product_description
        self.product_image = product_image
        self.__product_price = self.__validate_price(product_price)

    def get_product_name(self) -> str:
        return self.product_name

    def get_product_description(self) -> str:
        return self.product_description

    def get_product_image(self) -> str:
        return self.product_image

    def get_product_price(self) -> float:
        return self.__product_price

    def increase_product_price(self, increase_amount: float) -> None:
        self.__product_price += increase_amount
    
    def decrease_product_price(self, decrease_amount: float) -> None:
        self.__product_price -= decrease_amount

    def __validate_price(self, product_price: float) -> float:
        if product_price <= 0:
            raise ValueError("Invalid product price. It must be greater than 0")
        return product_price
