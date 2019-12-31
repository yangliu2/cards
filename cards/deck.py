import random
from cards.card import Card
from typing import List, Dict

class Deck:

    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self) -> None:
        """Generate cards to initialize the deck
        return: stack of Card object in card.py
        """
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def show(self) -> None:
        """Display the cards in the deck."""

        for card in self.cards:
            card.show()

    def shuffle(self):
        """
        Shuffle according to the Fisher Yates methods.
        https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3
        """
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self) -> None:
        """Draw one card from the deck"""
        return self.cards.pop()

    def set_rank(self, name_to_rank: Dict) -> None:

        """Assing the ranking of cards according to the game rules
        :param name_to_rank: the dictionary mapping of ranking"""
        for card in self.cards:
            card.rank = name_to_rank[card.name]