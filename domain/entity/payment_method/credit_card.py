from datetime import date

class CreditCard:

    def __init__(self, holder_name: str, card_number: str, expiration_month: int, expiration_year: int, verification_value: int) -> None:
       self.__holder_name = self.__validate_name(holder_name)
       self.__card_number = self.__validate_number(card_number)
       self.__expiration_month = self.__validate_month(expiration_month)
       self.__expiration_year = self.__validate_year(expiration_year)
       self.__verification_value =  self.__validate_verification_value(verification_value)

    def get_holder_name(self) -> str:
        return self.__holder_name

    def get_card_number(self) -> str:
        return self.__card_number
    
    def get_expiration_month(self) -> int:
        return self.__expiration_month
    
    def get_expiration_year(self) -> int:
        return self.__expiration_year

    def get_verification_value(self) -> int:
        return self.__verification_value

    def __validate_name(self, holder_name: str) -> str:
        if len(holder_name) < 3:
            raise ValueError("Invalid holder name")
        return holder_name
            
    def __validate_number(self, card_number: str) -> str:
        if not 0 < len(card_number) < 16:
            raise ValueError("Invalid credit card number")
        return card_number
        
    def __validate_month(self, expiration_month: int) -> int:
        if not 1 < expiration_month < 13:
            raise ValueError("Invalid expiration month")
        return expiration_month

    def __validate_year(self, expiration_year: int) -> int:
        if not expiration_year > date.today().year:
            raise ValueError("Invalid expiration year")
        return expiration_year

    def __validate_verification_value(self, verification_value: int) -> int:
        if len(str(verification_value)) < 3:
            raise ValueError("Invalid card verification number")
        return verification_value
