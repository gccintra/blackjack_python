from model.deck import Deck
from model.player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__(name='Dealer')
        self.deck = Deck()  

    def distribute_card(self):
        if len(self.deck) < 104:
            self.new_deck()
        card = self.deck.cards.pop() if self.deck.cards else None
        return card
    
    def new_deck(self):
        print('Picking up a new deck...')
        self.deck.clear_deck()
        self.deck.fill(4)
        self.deck.shuffle_cards()

    def receive_card(self, card):
        if len(self.hand) == 1:
            card.hide() 
        self.hand.append(card)
