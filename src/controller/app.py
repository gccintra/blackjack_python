from controller.auth import Auth
from controller.blackjack import Blackjack
from controller.transactions import Transactions
from controller.my_performance import MyPerformance

class App():
    def __init__(self):
        self.auth_controller = Auth()
        self.blackjack_controller = Blackjack()
        self.transactions_controller = Transactions()
        self.my_performance_controller = MyPerformance()
        self.__current_user = None

    def auth_menu(self):
        while True:
            decision_menu = self.auth_controller.auth_view.auth_menu()
            options = {
                '1': self.auth_controller.login,
                '2': self.auth_controller.register
            }
            action = options.get(decision_menu)
            if action:
                if decision_menu == '1':
                    self.__current_user = self.auth_controller.login()
                    self.game_menu()
                else:
                    action()
            else:
                self.auth_controller.auth_view.display_message("Invalid option. Please try again.", sleep_time=1)


    def game_menu(self):
        while True:
            decision_menu = self.blackjack_controller.blackjack_view.game_start_menu(self.__current_user)
            options = {
                '1': self.blackjack_controller.start_game,
                '2': self.transactions_controller.deposit,
                '3': self.transactions_controller.withdraw,
                '4': self.my_performance_controller.show,
                '5': self.logout
            }
            action = options.get(decision_menu)
            if action:
                if action is options['5']: 
                    action()
                    break
                action(self.__current_user)


            else:
                self.blackjack_controller.blackjack_view.display_message("Invalid option. Please try again.", sleep_time=1)



    def logout(self):
        self.blackjack_controller.blackjack_view.display_message("Logging out...", sleep_time=2)
