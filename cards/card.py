class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.rank = -1
        self.name = self.convert_value_to_name(value)

    def __str__(self):
        """give back string name"""
        return f"{self.name} of {self.suit}"

    def __repr__(self):
        return f"{self.name} of {self.suit}"

    def __eq__(self, other):
        return f"{self.name} of {self.suit}" == f"{other.name} of {other.suit}"

    @staticmethod
    def convert_value_to_name(value) -> str:
        """Map the value to a string"""
        value_to_name = {
                1: "Ace",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Jack",
                12: "Queen",
                13: "King"
            }
        return value_to_name[value]

    def show(self):
        print(f"{self.name} of {self.suit}")