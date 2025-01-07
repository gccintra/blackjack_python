from view.gameview import GameView
from model.gambler import Gambler
from model.dealer import Dealer
from controller.data_record import DataRecord

class Round:
    def __init__(self, round_result, value):
        self.round_result = round_result
        self.value = value

    def __repr__(self):
        return f"Round(result={self.round_result}, value={self.value})"

class Blackjack:
    def __init__(self):
        self.blackjack_view = GameView()
        self.rounds = []  
        self.players = []
        self.player_bet = 0
        self.users_db = DataRecord("users.json")


    def start_game(self, user):
        self.user = user
        self.player = Gambler(user.username, user.chips)
        self.dealer = Dealer()
        self.players = [self.dealer, self.player]
        self.start_round()

    def show_hand(self):
        for player in self.players:
            self.blackjack_view.show_hand(player.hand, player.name, player.score_aces)
        self.blackjack_view.display_message("\n=============")

    def start_round(self):
        self.blackjack_view.clear_screen()
        self.blackjack_view.display_message(f"============ BlackJack - Round {len(self.rounds) + 1}  ============\n")
        self.blackjack_view.display_message(f"Your Balance: ${self.player.chips}")

        self.player.clear_hand()
        self.dealer.clear_hand()
        self.player_bet = self.get_validated_round_chips()
        self.blackjack_view.display_message("\n=============")
        for i in range(2):
            for player in self.players:
                player.receive_card(self.dealer.distribute_card())
        self.show_hand()
        self.hit_or_stand()
        self.bet_result()
        if self.player.chips != 0:
            self.continue_or_stop()
        else:
            self.blackjack_view.display_message(f"\nLooks like you're out of chips! Better luck next time, champ!", 2)
            self.show_round_results()

    def bet_result(self):
        result = self.rounds[-1].round_result if self.rounds else None
        if result == "Win":
            self.player.chips += self.player_bet
        elif result == "Loss":
            self.player.chips -= self.player_bet

        self.user.chips = int(self.player.chips)
        self.users_db.update_user(self.user.username, {"total_chips": self.user.chips})

    def get_initial_chips(self):
        while True:
            try:
                player_initial_chips = int(self.blackjack_view.get_initial_chips())
                if player_initial_chips <= 0:
                    self.blackjack_view.display_message("Please enter a valid amount greater than 0.")
                else:
                    return player_initial_chips
            except ValueError:
                self.blackjack_view.display_message("Invalid Input! Please enter a valid number.")

    def get_validated_round_chips(self):
        while True:
            try:
                self.player_bet = int(self.blackjack_view.get_round_chips())
                valid, response = self.player.validate_bet(self.player_bet)

                if valid:
                    return self.player_bet
                else:
                    self.blackjack_view.display_message(response)
            except ValueError:
                self.blackjack_view.display_message("Invalid Input! Please enter a valid number.")

    def hit(self):
        self.player.receive_card(self.dealer.distribute_card())
        self.show_hand()
        if self.player.isBusted():
            self.blackjack_view.display_message(f"\nYou're busted :(")
            self.rounds.append(Round('Loss', self.player_bet))
        else:
            self.hit_or_stand()

    def stand(self):
        self.dealer.hand[1].reveal()
        while self.dealer.score_aces < 17:
            self.dealer.receive_card(self.dealer.distribute_card())
        round_result = self.verify_stand_result()
        self.rounds.append(Round(round_result, self.player_bet))

    def verify_stand_result(self):
        if self.dealer.isBusted():
            self.show_hand()
            self.blackjack_view.display_message(f'\nDealer is Busted, you won!')
            return 'Win'
        elif self.dealer.score_aces > self.player.score_aces:
            self.show_hand()
            self.blackjack_view.display_message(f'\nYou Lost :(')
            return 'Loss'
        elif self.dealer.score_aces == self.player.score_aces:
            self.show_hand()
            self.blackjack_view.display_message(f'\nDraw')
            return 'Draw'
        else:
            self.show_hand()
            self.blackjack_view.display_message(f'\nYou won!')
            return 'Win'

    def hit_or_stand(self):
        player_decision = self.blackjack_view.get_input("\n[H]it or [S]tand? ", upper=True)
        while (player_decision != 'H') and (player_decision != 'S'):
            self.blackjack_view.display_message("Invalid Decision!")
            player_decision = self.blackjack_view.get_input("\n[H]it or [S]tand? ", upper=True)
        self.hit() if player_decision == "H" else self.stand()

    def show_round_results(self):
        profit = 0
        self.blackjack_view.display_message("\n===== Your Results =====")
        
        if not self.rounds:
            self.blackjack_view.display_message("No rounds have been played.")
        else:
            for index, round in enumerate(self.rounds, start=1):
                result_message = f"Round {index}: {round.round_result}"
                if round.round_result == "Win":
                    result_message += f" (+{round.value} chips)"
                    profit += round.value
                elif round.round_result == "Loss":
                    result_message += f" (-{round.value} chips)"
                    profit -= round.value

                elif round.round_result == "Draw":
                    result_message += " (No change)"
                    
                self.blackjack_view.display_message(result_message)
        self.blackjack_view.display_message(f"\nYour Balance: ${self.player.chips}")
        self.blackjack_view.display_message(f'Profit: {profit}')
        self.blackjack_view.display_message("======================")
        input("\nPress ENTER to continue...")

    def continue_or_stop(self):
        self.blackjack_view.display_message(f"\nYour Balance: ${self.player.chips}")
        self.blackjack_view.display_message("\n=============")
        player_decision = self.blackjack_view.get_input("\n[C]ontinue or [S]top? ", upper=True)
        while (player_decision != 'C') and (player_decision != 'S'):
            self.blackjack_view.display_message("Invalid Decision!")
            player_decision = self.blackjack_view.get_input("\n[C]ontinue or [S]top? ", upper=True)
        self.start_round() if player_decision == 'C' else self.show_round_results()
