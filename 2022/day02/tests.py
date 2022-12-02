import unittest

import day02


class TestDay02(unittest.TestCase):

    def test_score_round_example_1(self):
        round_choices = 'A Y\n'
        score = day02.score_round(round_choices)
        self.assertEqual(score, 4)

    def test_score_round_example_2(self):
        round_choices = 'B X\n'
        score = day02.score_round(round_choices)
        self.assertEqual(score, 1)

    def test_score_round_example_3(self):
        round_choices = 'C Z\n'
        score = day02.score_round(round_choices)
        self.assertEqual(score, 7)


if __name__ == '__main__':
    unittest.main()
