from model.user import User

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def clear_hand(self):
        self.hand =[]

    @property
    def score(self):
        return sum([card.score for card in self.hand if card.visible])
    
    @property
    def aces(self):
        return len([card for card in self.hand if card.value == 'A'])
    
    @property
    def score_aces(self):
        temp_score = self.score
        aces_count = self.aces

        while aces_count > 0 and temp_score + 10 <= 21:
            temp_score += 10
            aces_count -= 1

        return temp_score
    
    def isBusted(self):
        return self.score_aces > 21
      

