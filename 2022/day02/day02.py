#A rock 1 -> B
#B paper 2 -> C
#C scissors 3 -> A

#X lose 0
#Y draw 3
#Z win 6
A = 1
B = 2
C = 3
scores = {
    'X': {
        'result_score': 0,
        'A': C,
        'B': A,
        'C': B
    },
    'Y': {
        'result_score': 3,
        'A': A,
        'B': B,
        'C': C
    },
    'Z': {
        'result_score': 6,
        'A': B,
        'B': C,
        'C': A
    }
}


def score_round(round_code: str):
    round_code_split = round_code.split(' ')
    left = round_code_split[0]
    right = round_code_split[1].rstrip()
    result = scores[right]
    score = result['result_score'] + result[left]
    return score


def main():
    with open('input.txt', 'r') as f:
        input = f.readlines()
    total_score = 0
    for round in input:
        total_score += score_round(round)
    print(total_score)


if __name__ == '__main__':
    main()