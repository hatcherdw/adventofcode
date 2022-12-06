

class Assignments:

    def __init__(self, ranges: str):
        self.parse_ranges(ranges)

    def parse_ranges(self, ranges: str):
        split_ranges = ranges.split(',')
        split_left = split_ranges[0].split('-')
        split_right = split_ranges[1].split('-')
        self.left_min = int(split_left[0])
        self.left_max = int(split_left[1])
        self.right_min = int(split_right[0])
        self.right_max = int(split_right[1])

    def complete_overlap(self) -> bool:
        if (self.left_min <= self.right_min) & (self.left_max >= self.right_max):
            return True
        elif (self.right_min <= self.left_min) & (self.right_max >= self.left_max):
            return True
        else:
            return False

    def overlap(self) -> bool:
        if (self.left_max >= self.right_min) & (self.left_max < self.right_max):
            return True
        if (self.left_min <= self.right_max) & (self.left_max > self.right_max):
            return True
        return False


def main():
    with open('input.txt', 'r') as f:
        assignments_input = f.readlines()
    total_overlap = 0
    for line in assignments_input:
        assignments = Assignments(line.rstrip())
        if assignments.complete_overlap():
            total_overlap += 1
        elif assignments.overlap():
            total_overlap += 1
    print(total_overlap)


if __name__ =='__main__':
    main()