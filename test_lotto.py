import unittest
from lotto_game import Card, Player

class TestCard(unittest.TestCase):

    def test_generate_card(self):
        card = Card()
        self.assertEqual(len(card.rows), 3)
        for row in card.rows:
            self.assertEqual(len(row.split()), 5)

    def test_mark_number(self):
        card = Card()
        card.rows = ["25 26 0 - 67 - 8 - 9 22"]
        self.assertEqual(card.mark_number("25"), True)

    def test_has_won(self):
        card = Card()
        self.assertFalse(card.has_won())

    def test_repr(self):
        card = Card()
        expected_repr = f'Card(rows={card.rows})'
        self.assertEqual(repr(card), expected_repr)

    def test_str(self):
        card = Card()
        expected_str = '-' * 26 + '\n'
        expected_str += '\n'.join(row for row in card.rows)
        expected_str += '\n' + '-' * 26
        self.assertEqual(str(card), expected_str)

class TestPlayer(unittest.TestCase):

    def test_has_won(self):
        player = Player("player")
        self.assertFalse(player.has_won())
