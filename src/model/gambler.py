from model.player import Player

class Gambler(Player):
    def __init__(self, name, chips=0):
        super().__init__(name)
        self.chips = chips

    def receive_card(self, card):
        self.hand.append(card)
    
    def validate_bet(self, player_bet):
        if player_bet > self.chips:
            return False, "You don't have enough chips for this bet! Please enter a smaller amount."
        elif player_bet <= 0:
            return False, "Please enter a valid amount greater than 0."
        else:
            return True, player_bet
        
