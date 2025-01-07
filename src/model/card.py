class Card:
    def __init__(self, value, naipe, visible=True):
        self.value = value
        self.naipe = naipe
        self.visible = visible
    
    def reveal(self):
        self.visible = True

    def hide(self):
        self.visible = False

    @property
    def score(self):
        if self.value in ['J', 'K', 'Q']:
            return 10
        elif self.value == 'A':
            return 1
        else:
            return int(self.value) 

    def __str__(self):
        return f"{self.value} of {self.naipe}" if self.visible else "Hidden Card"