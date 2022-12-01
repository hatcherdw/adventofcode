def most_calories(inventory: str) -> int:
    '''Which elf is carrying the most calories'''
    split_inventory = inventory.split('\n\n')
    most = 0
    for individual in split_inventory:
        items = individual.split('\n')
        items = [int(item) for item in items]
        total_calories = sum(items)
        if total_calories > most:
            most = total_calories
    return most


def main():
    with open('input.txt', 'r') as f:
        input = f.read()
    print(most_calories(input))


if __name__ == '__main__':
    main()
