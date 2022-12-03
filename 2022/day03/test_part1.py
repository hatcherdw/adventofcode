import unittest

import part1


class TestPart1(unittest.TestCase):

    def test_find_common_item_1(self):
        rucksack_contents = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 'p')

    def test_find_common_item_2(self):
        rucksack_contents = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 'L')

    def test_find_common_item_3(self):
        rucksack_contents = 'PmmdzqPrVvPwwTWBwg'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 'P')

    def test_find_common_item_4(self):
        rucksack_contents = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 'v')

    def test_find_common_item_5(self):
        rucksack_contents = 'ttgJtRGJQctTZtZT'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 't')
    
    def test_find_common_item_6(self):
        rucksack_contents = 'CrZsJsPPZsGzwwsLwLmpwMDw'
        common_item = part1.find_common_item(rucksack_contents)
        self.assertEqual(common_item, 's')

    def test_item_to_priority_1(self):
        item = 'p'
        priority = part1.item_to_priority(item)
        self.assertEqual(priority, 16)

    def test_item_to_priority_2(self):
        item = 'L'
        priority = part1.item_to_priority(item)
        self.assertEqual(priority, 38)

if __name__ == '__main__':
    unittest.main()