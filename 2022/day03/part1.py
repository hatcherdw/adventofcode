import string


def find_common_item(rucksack_contents: str) -> str:
    num_contents = len(rucksack_contents)
    compartment_size = int(num_contents / 2)
    compartment_1 = rucksack_contents[0:compartment_size]
    compartment_2 = rucksack_contents[compartment_size:num_contents]
    for item in compartment_1:
        if item in compartment_2:
            return item


def item_to_priority(item: str) -> int:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    priorities = lowercase + uppercase
    index = priorities.index(item)
    return index + 1


def main():
    with open('input.txt', 'r') as f:
        rucksacks = f.readlines()
    total = 0
    for rucksack in rucksacks:
        common_item = find_common_item(rucksack)
        priority = item_to_priority(common_item)
        total += priority
    print(total)


if __name__ == '__main__':
    main()