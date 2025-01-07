from view.app_view import AppView

class GameView(AppView):

    def game_start_menu(self, user):
        while True:
            self.clear_screen()
            print('============ BlackJack ============')       
            print(f'Username: {user.username}')    
            print(f'Chips: {user.chips}')         
     
            print("[1] - Start Game")
            print("[2] - Deposit")
            print("[3] - Withdraw")
            print("[4] - Transactions")
            print("[5] - Exit")
            decision_menu = input("Select an option: ")
            return decision_menu
    

    def get_hit_or_stand(self):
        return input("[H]it or [S]tand? ").upper()

    def show_hand(self, hand, playerName, score):
        print(f"\n{playerName}'s hand:")
        for card in hand:
            print(f"{card}")
        print(f"\nSum:{score}")

  
    def get_round_chips(self):
        return input("What's your deal? ")
    
 
    def get_player_continue_decision(self):
        return input("[C]ontinue or [S]top? ").upper()
    
 
    def show_balance(self, balance):
        print(f"\nYour Balance: ${balance}")
