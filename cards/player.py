class Player:

    def __init__(self, name: str, win_total: int = 0):
        self.name = name
        self.hand = []
        self.win_total = win_total

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        print(f"For player {self.name}")
        for card in self.hand:
            card.show()
        print("\n")
    
    def sort_hand(self):
        """sort the hand according to rank. this may help to 
        determine the policy of the player"""

        # stop sorting if the no rank set by the game
        if self.hand[0].rank == -1:
            print(f"rank was not assigned for this game")
            return

        self.hand = sorted(self.hand, key=lambda x: x.rank, 
            reverse=False)

    def play_hand(self, previous_hand):
        # play by sorted order, no rank, baseline
        played_card = self.hand.pop()
        print(f"{self.name} played {played_card}")
        return played_card
            