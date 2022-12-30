from collections import deque

n = int(input())

pizza = list(map(int, input().split()))

# 각 사람마다 피자 배부가 완료된 횟수
arr = [0 for _ in range(n)]

queue = deque()

for i in range(n):
    queue.append([i, 0])

cnt = 0

while queue:
    num, get = queue.popleft()  # 사람 번호, 받은 피자 수
    cnt += 1

    get += 1

    if pizza[num] == get:
        arr[num] = cnt  # 몇번째일 때 다 원하는 만큼 받았냐

    else:
        queue.append([num, get])

for i in arr:
    print(i, end=' ')
print('')