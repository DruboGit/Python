from enum import Enum

class card:
    def __init__(self, suit, type):
        self.suit = suit
        self.type = type

class suit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4
    
class type (Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

def new_deck():
    deck = []
    for suits in suit:
        for types in type:
            new_card = card(suits, types)
            deck.append(new_card)
    return deck