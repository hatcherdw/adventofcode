import re
from queue import LifoQueue


class Supplies:

    def __init__(self):
        self.num_stacks = 0
        self.stacks = dict()

    def add_stack(self, containers: list[str]):
        self.num_stacks += 1
        stack = LifoQueue()
        for container in containers:
            stack.put(container)
        self.stacks[str(self.num_stacks)] = stack

    def move_containers(self, n: int, source: str, target: str):
        source_stack = self.stacks[source]
        target_stack = self.stacks[target]
        buffer = LifoQueue()
        for _ in range(n):
            container = source_stack.get()
            buffer.put(container)
        for _ in range(n):
            container = buffer.get()
            target_stack.put(container)


def parse_procedure(procedure: str):
    numbers = re.findall(r'\d+', procedure)
    return int(numbers[0]), numbers[1], numbers[2]


def main():
    supplies = Supplies()
    supplies.add_stack(['D','L','J','R','V','G','F'])
    supplies.add_stack(['T','P','M','B','V','H','J','S'])
    supplies.add_stack(['V','H','M','F','D','G','P','C'])
    supplies.add_stack(['M','D','P','N','G','Q'])
    supplies.add_stack(['J','L','H','N','F'])
    supplies.add_stack(['N','F','V','Q','D','G','T','Z'])
    supplies.add_stack(['F','D','B','L'])
    supplies.add_stack(['M','J','B','S','V','D','N'])
    supplies.add_stack(['G','L','D'])
    with open('input.txt', 'r') as f:
        input = f.readlines()
    for line in input[10:]:
        n, source, target = parse_procedure(line)
        supplies.move_containers(n, source, target)
    for stack in supplies.stacks.keys():
        print(supplies.stacks[stack].queue)


if __name__ =='__main__':
    main()
