N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

pair_numbs = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0,
}

sides = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4],
}

answer = 0

for i in range(6):
    top_idx = pair_numbs[i]
    top_numb = dice[0][top_idx]
    side_idx = sides[i]

    temp = max(dice[0][idx] for idx in side_idx)

    for j in range(1, len(dice)):
        bottom_idx = dice[j].index(top_numb)
        top_idx = pair_numbs[bottom_idx]
        top_numb = dice[j][top_idx]
        side_idx = sides[bottom_idx]

        temp += max(dice[j][idx] for idx in side_idx)

    if answer < temp:
        answer = temp

print(answer)