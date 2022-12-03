from part1 import item_to_priority


def find_badge(group: list[str]):
    unique_items_1 = set(group[0])
    unique_items_2 = set(group[1])
    unique_items_3 = set(group[2])
    badge = unique_items_1.intersection(
        unique_items_2, unique_items_3
    )
    return list(badge)[0]


def main():
    with open('input.txt', 'r') as f:
        rucksacks = f.readlines()
    total = 0
    for start in range(0, len(rucksacks), 3):
        stop = start + 3
        group = rucksacks[start:stop]
        clean_group = [rucksack.replace('\n', '') for rucksack in group]
        badge = find_badge(clean_group)
        priority = item_to_priority(badge)
        total += priority
    print(total)


if __name__ == '__main__':
    main()