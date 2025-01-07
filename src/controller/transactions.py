from controller.data_record import DataRecord
from model.transaction import Transaction
from utils import get_valid_input
from view.app_view import AppView
from datetime import datetime


class Transactions:
    def __init__(self):
        self.db = DataRecord("transactions.json")
        self.users_db = DataRecord("users.json")
        self.app_view = AppView()

    def deposit(self, user):
        self.app_view.display_message("\n=============")
        value = get_valid_input(
            '\nHow many chips do you want to deposit? ',
            [
                (lambda x: x.isdigit(), "Insert a valid number."),
                (lambda x: int(x) > 0 if x.isdigit() else True, "Insert a valid number.")
            ]
        )
        deposit = Transaction(account_transaction = user.username, transaction_type="Deposit", value=int(value))
        deposit_dict = deposit.to_dict()
        if self.db.write(deposit_dict):
            user.chips += int(value)
            self.users_db.update_user(user.username, {"total_chips": user.chips})
            self.app_view.display_message(f"\nDeposit successfully!", sleep_time=2)
        else:
            self.app_view.display_message("\nAn error occurred while depositing. Please try again.", sleep_time=2)
            del deposit

    def withdraw(self, user):
        self.app_view.display_message("\n=============")
        if int(user.chips) == 0:
            self.app_view.display_message(f"You don't have enough chips.", sleep_time=2)
            return

        value = get_valid_input(
            '\nHow many chips do you want to withdraw? ',
            [
                (lambda x: x.isdigit(), "Insert a valid number."),
                (lambda x: int(x) > 0 if x.isdigit() else True, "Insert a valid number."),
                (lambda x: int(x) <= user.chips if x.isdigit() else True, "You don't have enough chips."),
            ]
        )
        withdraw = Transaction(account_transaction = user.username, transaction_type="Withdraw", value=int(value))
        withdraw_dict = withdraw.to_dict()
        if self.db.write(withdraw_dict):
            user.chips -= int(value)
            self.users_db.update_user(user.username, {"total_chips": user.chips})
            self.app_view.display_message(f"\nSuccessfully withdrew {value} chips!", sleep_time=2)
        else:
            self.app_view.display_message("\nAn error occurred while withdewing. Please try again.", sleep_time=2)
            del withdraw

    
    def show(self, user):
        transactions = self.db.get_models()
        user_transactions = [t for t in transactions if t['account_transaction'] == user.username]

        total_deposit = sum(t['value'] for t in user_transactions if t['transaction_type'] == 'Deposit')
        total_withdraw = sum(t['value'] for t in user_transactions if t['transaction_type'] == 'Withdraw')
        total_profit = (total_withdraw + user.chips) - total_deposit
        self.app_view.clear_screen()
        self.app_view.display_message("========== Transactions ==========\n")
        self.app_view.display_message(f"User: {user.username}")
        self.app_view.display_message(f"Current Balance: ${user.chips}\n")

        if not user_transactions:
            self.app_view.display_message("No transactions found.")
        else:
            for transaction in user_transactions:
                date = transaction['transaction_date']
                formatted_date = datetime.fromisoformat(date).strftime("%d/%m/%Y %H:%M:%S")
                transaction_type = transaction['transaction_type']
                value = transaction['value']
                print(f"{formatted_date}: {transaction_type} - ${value}")
            self.app_view.display_message(f"\nTotal Profit: {total_profit}")
        self.app_view.display_message("\n===============================")
        input("\nPress ENTER to continue...")
  
