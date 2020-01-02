from cards.card import Card
from cards.player import Player
from cards.deck import Deck
from typing import List

class Game:
    def __init__(self, player_count: int = 3):

        self.players = self.create_players(player_count)
        self.player_order = [player.name for player in self.players]
        self.deck = Deck()
        self.set_rank()
        self.draw_cards()


    @staticmethod
    def create_players(player_count: int) -> List[Player]:
        """Create a list of players according to count
        return: list of Players
        """

        player_list = []
        
        for n in range(player_count):
            player_list.append(Player(f"Player{n}"))
        return player_list

    def draw_cards(self):
        # keep drawing if there are cards
        while self.deck.cards:

            for player in self.players:
                # stop if no cards to draw
                if not self.deck.cards:
                    break
                player.draw(self.deck)

    def set_rank(self):
        """Set up the ranking for this game and change ranking 
        of the cards."""
        name_to_rank = {
            "Two": 1,
            "Ace": 2,
            "King": 3,
            "Queen": 4,
            "Jack": 5,
            "Ten": 6,
            "Nine": 7,
            "Eight": 8,
            "Seven": 9,
            "Six": 10,
            "Five": 11,
            "Four": 12,
            "Three": 13
        }
        self.deck.set_rank(name_to_rank)

    def determine_first(self) -> str:
        """Determine who goes first. Need to draw cards first"""
        for player in self.players:
            start_card = Card("Hearts", 3)

            if start_card in player.hand:
                print(f"{player.name} goes first.")
                return player.name

        return "Nobody"

    def play(self):

        # sort hand according to the game ranking
        [player.sort_hand() for player in self.players]

        # show player hands
        # [player.show_hand() for player in self.players]

        # determine who start and change player order
        starting_player = self.determine_first()
        starter_index = self.player_order.index(starting_player)
        self.player_order = self.players[starter_index:] + self.players[:starter_index]


        # print(self.player_order)
        # go through each turns
        previous_hands = []
        player_card_count = len(self.player_order[0].hand)

        while player_card_count > 0:
            for current_player in self.player_order:
                previous_hand = current_player.play_hand(previous_hands)
                player_card_count = len(current_player.hand) 
                # print(f"current player hand len {player_card_count}")
                
                previous_hands.append(previous_hand)
                # print(f"{current_player.name}: {current_player.hand}")

                # need to exit for loop when last card from any player is played. 
                # TODO: might be a better algorithm with the whle loop?
                if player_card_count == 0:
                    current_player.win_total =+ 1
                    break

        win_total = [{player.name: player.win_total} for player in self.player_order]
        print(f"win total {win_total}")


def main():
    from cards.game import Game
    game = Game()
    game.play()


if __name__ == "__main__":
    main()