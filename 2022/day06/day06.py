from collections import deque


def find_start_marker(buffer: str):
    d = deque(maxlen=14)
    for index, character in enumerate(buffer):
        d.append(character)
        if len(set(d)) == 14:
            return index + 1


def main():
    with open('input.txt', 'r') as f:
        input = f.read()
    start = find_start_marker(input)
    print(start)


if __name__ == '__main__':
    main()