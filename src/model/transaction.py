from datetime import datetime

class Transaction:
    def __init__(self, account_transaction, transaction_type, value):
        self.account_transaction = account_transaction
        self.transaction_type = transaction_type
        self.value = value
        self.transaction_date = datetime.now()


    def to_dict(self): 
        return {
            "account_transaction": self.account_transaction,
            "transaction_type": self.transaction_type,
            "value": self.value,
            "transaction_date": self.transaction_date.isoformat()
        }
    
