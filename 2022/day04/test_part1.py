import unittest

import part1


class TestPart1(unittest.TestCase):

    def test_parse_assignments(self):
        assignments = '2-4,6-8'
        result = part1.Assignments(assignments)
        self.assertEqual(result.left_min, 2)
        self.assertEqual(result.left_max, 4)
        self.assertEqual(result.right_min, 6)
        self.assertEqual(result.right_max, 8)
    
    def test_complete_overlap(self):
        assignments = part1.Assignments('2-8,3-7')
        result = assignments.complete_overlap()
        self.assertTrue(result)
    
    def test_complete_overlap_2(self):
        assignments = part1.Assignments('6-6,4-6')
        result = assignments.complete_overlap()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
