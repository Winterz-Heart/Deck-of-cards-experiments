import random

class DECK:
    # Generate the whole deck
    def __init__(self):
        suits = ["C", "D", "H", "S"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.card = [(suit+rank) for suit in suits for rank in ranks]

    # 1 Random card
    def random(self):
        return random.choice(self.card)
    
    # 1 seven card hand
    def hand(self):
        return random.sample(self.card, 7)






# Print the whole deck
deck = DECK()
print(deck.hand())
