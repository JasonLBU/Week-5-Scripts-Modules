# Task 5
import random

def CreateDeck():
    Deck = []
    Card_Type = ['Hearts','Spades','Clubs','Diamonds']
    Card_Value = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    for i in Card_Type:
        for j in Card_Value:
            Deck.append(j + ' of ' + i)
    print(Deck)
    return Deck

def ShuffleDeck(Deck):
    random.shuffle(Deck)


def DealHands(Deck):
    P1_Hand = []
    P2_Hand = []
    P3_Hand = []
    P4_Hand = []
    for i in range(0,14):
        card = random.randint(0, len(Deck)-1)
        P1_Hand.append()

def Main():
    print()

print(ShuffleDeck(CreateDeck()))