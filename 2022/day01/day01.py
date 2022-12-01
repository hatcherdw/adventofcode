from webbrowser import get


def get_totals(inventory: str) -> list[int]:
    split_inventory = inventory.split('\n\n')
    totals = []
    for individual in split_inventory:
        items = individual.split('\n')
        items = [int(item) for item in items]
        totals.append(sum(items))
    return totals


def most_calories(inventory: str) -> int:
    '''Which elf is carrying the most calories'''
    totals = get_totals(inventory)
    return max(totals)


def main():
    with open('input.txt', 'r') as f:
        input = f.read()
    totals = get_totals(input)
    sorted_totals = sorted(totals)
    print(sorted_totals[-1])
    print(sum(sorted_totals[-3:]))


if __name__ == '__main__':
    main()
