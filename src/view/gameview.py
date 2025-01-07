from view.app_view import AppView

class GameView(AppView):

    def game_start_menu(self, user):
        while True:
            self.clear_screen()
            print('============ BlackJack ============\n')       
            print(f'User: {user.username}')    
            print(f'Current Balance: ${user.chips}\n')         
     
            print("[1] - Start Game")
            print("[2] - Deposit")
            print("[3] - Withdraw")
            print("[4] - Transactions")
            print("[5] - Exit")
            decision_menu = input("\nSelect an option: ")
            return decision_menu
    
    def show_hand(self, hand, playerName, score):
        print(f"\n{playerName}'s hand:")
        for card in hand:
            print(f"{card}")
        print(f"\nSum:{score}")

    def get_round_chips(self):
        return input("\nWhat's your deal? ")

    def get_input(self, prompt, upper=False):
        return input(prompt).strip() if not upper else input(prompt).strip().upper()
        