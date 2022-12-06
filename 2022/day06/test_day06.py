import unittest

from day06 import find_start_marker


class TestDay06(unittest.TestCase):

    def test_find_start_marker_1(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        start = find_start_marker(buffer)
        self.assertEqual(start, 7)

    def test_find_start_marker_2(self):
        buffer = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        start = find_start_marker(buffer)
        self.assertEqual(start, 5)

if __name__ == '__main__':
    unittest.main()
