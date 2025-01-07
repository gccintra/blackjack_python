from controller.data_record import DataRecord
from datetime import datetime


class MyPerformance():
    def __init__(self):
        self.db = DataRecord("transactions.json")

    def show(self, user):
        transactions = self.db.get_models()
        user_transactions = [t for t in transactions if t['account_transaction'] == user.username]

        total_deposit = sum(t['value'] for t in user_transactions if t['transaction_type'] == 'Deposit')
        total_withdraw = sum(t['value'] for t in user_transactions if t['transaction_type'] == 'Withdraw')
        total_profit = (total_withdraw + user.chips) - total_deposit

        print("\n=== Resume ===")
        print(f"User: {user.username}")
        print(f"Current Balance: ${user.chips}\n")

        if not user_transactions:
            print("Nenhuma transação encontrada.")
        else:
            for transaction in user_transactions:
                date = transaction['transaction_date']
                formatted_date = datetime.fromisoformat(date).strftime("%d/%m/%Y %H:%M:%S")
                transaction_type = transaction['transaction_type']
                value = transaction['value']
                print(f"{formatted_date}: {transaction_type} - ${value}")

        print(f"\nTotal Profit: {total_profit}")
        print("===============================")
        input("Press ENTER to continue...")
