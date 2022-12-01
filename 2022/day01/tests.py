import unittest

import day01


class TestDay01(unittest.TestCase):

    def test_most_calories_example(self):
        input = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'
        result = day01.most_calories(input)
        self.assertEqual(result, 24000)


if __name__ == '__main__':
    unittest.main()
