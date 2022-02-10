from dataclasses import dataclass

from domain.entity.transaction.transaction_status import TransactionStatus

@dataclass
class TransactionDtoOutput:
    
    identifier: str
    status: TransactionStatus