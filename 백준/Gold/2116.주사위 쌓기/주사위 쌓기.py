N = int(input()) # 주사위 개수
dice_lst = [] # 이중 리스트 만들기위해 빈 리스트 생성
for _ in range(N):
    dice_lst.append(list(map(int, input().split()))) # 각 주사위 수 리스트로 받아서 리스트에 추가

# 윗면 아랫면 짝지어주기
bottom_and_top = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
} 

# 가능한 옆면을 value로 받는 딕셔너리 설정
sides = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4]
}

max_result = 0
# 첫번째 주사위 먼저 시작 => 윗면만 고려
for i in range(6):
    top_idx = bottom_and_top[i]
    top_numb = dice_lst[0][top_idx]
    side_idx = sides[i]

    result = max(dice_lst[0][idx] for idx in side_idx)

    # 두번째 ~ 마지막 주사위 반복 => 아랫면, 윗면 둘 다 고려
    for j in range(1, len(dice_lst)):
        bottom_idx = dice_lst[j].index(top_numb)
        top_idx = bottom_and_top[bottom_idx]
        top_numb = dice_lst[j][top_idx]
        side_idx = sides[bottom_idx]

        result += max(dice_lst[j][idx] for idx in side_idx)

    if max_result < result:
        max_result = result

print(max_result)