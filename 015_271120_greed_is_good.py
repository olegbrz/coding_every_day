points = {
    # number: [<3, >= 3]
    0: [0, 0], 1: [100, 1000], 2: [0, 200], 3: [0, 300],
    4: [0, 400], 5: [50, 500], 6: [0, 600]
}


def score(dices):
    counter = {dice: dices.count(dice) for dice in dices}
    total_score = 0

    for n in counter.keys():
        if counter[n] >= 3:
            total_score += points[n][1]
            counter[n] -= 3
        total_score += counter[n]*points[n][0]
    return total_score
