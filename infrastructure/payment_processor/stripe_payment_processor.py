from domain.entity.transaction.transaction import Transaction

class StripePaymentProcessor:
    
    def pay(self, transaction: Transaction) -> bool:
        transaction_id = transaction.get_transaction_id()
        transaction_credit_card = transaction.get_credit_card()
        print(f"Processing transaction {transaction_id} using credit credit card number {transaction_credit_card.get_card_number()}")
        return True