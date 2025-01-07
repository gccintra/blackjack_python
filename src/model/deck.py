from model.card import Card
import random

class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    naipes = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = []
        self.fill(4)
        self.shuffle_cards()         

    def shuffle_cards(self):
       random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)
    
    def clear_deck(self):
        self.cards =[]

    def fill(self, decks):
        for i in range(decks):
            for value in self.values:
                for naipe in self.naipes:
                    self.cards.append(Card(value, naipe))
