import unittest

import part2


class TestPart2(unittest.TestCase):
    
    def test_find_badge_1(self):
        group = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]
        badge = part2.find_badge(group)
        self.assertEqual(badge, 'r')

    def test_find_badge_2(self):
        group = [
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]
        badge = part2.find_badge(group)
        self.assertEqual(badge, 'Z')


if __name__ == '__main__':
    unittest.main()