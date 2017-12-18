"""Golf solitaire."""

from itertools import zip_longest
from textwrap import dedent

from cards import Card, Deck


class Solitaire:
    """
    Solitaire class representing a game of Golf Solitaire.

    This game has 7 columns and 5 cards in each column,
    but the methods should work with other valid values as well.
    """

    columns = 7
    cards_in_column = 5

    def __init__(self):
        """
        Constructor, do the setup here.

        After setup with Solitaire.columns = 7, Solitaire.cards_in_column = 5
        You should have:
        self.tableau -> 7 columns of cards with 5 cards in each column
        self.stock -> 16 cards
        self.waste -> 1 card
        """
        if Solitaire.columns * Solitaire.cards_in_column > 50:
            if Solitaire.columns * Solitaire.cards_in_column < 1:
                raise Exception("Incorrect amount of columns and cards in columns")
        self.deck = Deck(symbols=True, decorated=False)  # -> Deck instance
        self.tableau = []  # -> list of (columns[lists] (where each list -> cards_in_column * Card instances))
        self.deck.shuffle_deck()
        for i in range(Solitaire.columns):
            column = []
            for j in range(Solitaire.cards_in_column):
                column.append(self.deck.deal_card())
            self.tableau.append(column)
        self.waste = [self.deck.deal_card()]  # -> list of Card instances
        self.stock = []  # -> list of Card instances
        for i in range(len(self.deck.cards)):
            self.stock.append(self.deck.deal_card())


    def can_move(self, card) -> bool:
        """
        Validate if a card from the tableau can be moved to the waste pile.

        The card must be last in the column list and adjacent by rank
        to the topmost card of the waste pile (last in waste list).
        Example: 8 is adjacent to 7 and 9. Ace is only adjacent to 2.
        King is only adjacent to Queen.
        """
        rank = card.rank()
        pass

    def move_card(self, col: int):
        """
        Move a card from the tableau to the waste pile.

        Does not validate the move.
        :param col: index of column
        """
        pass  # your code

    def deal_from_stock(self):
        """
        Deal last card from stock pile to the waste pile.

        If the stock is empty, do nothing.
        """
        pass  # your code

    def has_won(self) -> bool:
        """Check for the winning position - no cards left in tableau."""
        pass  # your code

    def has_lost(self) -> bool:
        """
        Check for the losing position.

        Losing position: no cards left in stock and no possible moves.
        """
        pass  # your code

    def print_game(self):
        """
        Print the game.

        Assumes:
        Card(decorated=True) by default it is already set to True
        self.tableau -> a list of lists (each list represents a column of cards)
        self.stock -> a list of Card objects that are in the stock
        self.waste_pile -> a list of Card objects that are in the waste pile

        You may modify/write your own print_game.
        """
        print(f" {'    '.join(list('0123456'))}")
        print('-' * 34)
        print("\n".join([(" ".join((map(str, x)))) for x in (zip_longest(*self.tableau, fillvalue="    "))]))
        print()
        print(f"Stock pile: {len(self.stock)} card{'s' if len(self.stock) != 1 else ''}")
        print(f"Waste pile: {self.waste[-1] if self.waste else 'Empty'}")

    @staticmethod
    def rules():
        """Print the rules of the game."""
        print("Rules".center(40, "-"))
        print(dedent("""
                Objective: Move all the cards from each column to the waste pile.

                A card can be moved from a column to the waste pile if the
                rank of that card is one higher or lower than the topmost card
                of the waste pile. Only the first card of each column can be moved.

                You can deal cards from the stock to the waste pile.
                The game is over if the stock is finished and
                there are no more moves left.

                The game is won once the tableau is empty.

                Commands:
                  (0-6) - integer of the column, where the topmost card will be moved
                  (d) - deal a card from the stock
                  (r) - show rules
                  (q) - quit
                  """))

    def play(self):
        """
        Play a game of Golf Solitaire.

        Create the game loop here.
        Use input() for player input.
        Available commands are described in rules().
        """
        pass  # your code


if __name__ == '__main__':
    s = Solitaire()
    print(s.deck)
    print(s.tableau)
    print(f"Table has {len(s.tableau * s.cards_in_column)} cards")
    print(s.stock)
    print(f"Stock has {len(s.stock)} cards")
    print(s.waste)
    print(type(s.waste[0]))
