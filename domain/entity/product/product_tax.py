class ProductTax:

    def __init__(self, pst: int, gst: int) -> None:
        self.__provincial_tax = pst
        self.__federal_tax = gst

    def get_provincial_tax(self) -> float:
        return self.__provincial_tax
    
    def get_federal_tax(self) -> float:
        return self.__federal_tax
    
    def get_full_tax(self) -> float:
        return self.__federal_tax + self.__provincial_tax