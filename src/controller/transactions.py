from controller.data_record import DataRecord
from model.transaction import Transaction
from utils import get_valid_input
from view.app_view import AppView

class Transactions:
    def __init__(self):
        self.db = DataRecord("transactions.json")
        self.users_db = DataRecord("users.json")
        self.app_view = AppView()

    def deposit(self, user):
        value = get_valid_input(
            'How many chips do you want to deposit? ',
            [
                (lambda x: x.isdigit() and int(x) > 0, "Insert a valid number."),
            ]
        )
        deposit = Transaction(account_transaction = user.username, transaction_type="Deposit", value=int(value))
        deposit_dict = deposit.to_dict()
        if self.db.write(deposit_dict):
            user.chips += int(value)
            self.users_db.update_user(user.username, {"total_chips": user.chips})
            self.app_view.display_message(f"Deposit successfully!", sleep_time=2)
        else:
            self.app_view.display_message("An error occurred while depositing. Please try again.", sleep_time=2)
            del deposit

    def withdraw(self, user):
        if int(user.chips) == 0:
            self.app_view.display_message(f"You don't have enough chips.", sleep_time=2)
            return

        value = get_valid_input(
            'How many chips do you want to withdraw? ',
            [
                (lambda x: x.isdigit() and int(x) > 0, "Insert a valid number."),
                (lambda x: int(x) <= user.chips, "You don't have enough chips."),
            ]
        )
        withdraw = Transaction(account_transaction = user.username, transaction_type="Withdraw", value=int(value))
        withdraw_dict = withdraw.to_dict()
        if self.db.write(withdraw_dict):
            user.chips -= int(value)
            self.users_db.update_user(user.username, {"total_chips": user.chips})
            self.app_view.display_message(f"Successfully withdrew {value} chips!", sleep_time=2)
        else:
            self.app_view.display_message("An error occurred while withdewing. Please try again.", sleep_time=2)
            del withdraw

    
