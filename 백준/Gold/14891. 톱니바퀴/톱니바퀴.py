from collections import deque
import sys

def check_right(numb, dirs):
    if numb > 4 or arr[numb-1][2] == arr[numb][6]:
        return
    
    # 오른쪽 확인해보기
    if arr[numb-1][2] != arr[numb][6]:
        # 인접 톱니바퀴 회전 가능한지 확인해보기
        check_right(numb+1, -dirs)
        # 그 다음에 회전시키기
        arr[numb].rotate(dirs)

def check_left(numb, dirs):
    if numb < 1 or arr[numb+1][6] == arr[numb][2]:
        return
    
    # 왼쪽 확인해보기
    if arr[numb+1][6] != arr[numb][2]:
        # 인접 톱니바퀴 회전 가능한지 확인해보기
        check_left(numb-1, -dirs)
        # 그 다음에 회전시키기
        arr[numb].rotate(dirs)

arr = {}
# 톱니바퀴 1 - 4
for i in range(1, 5):
    arr[i] = deque(list(map(int, input().rstrip())))
k = int(input())

for _ in range(k):
    numb, dirs = map(int, input().split())

    check_right(numb+1, -dirs)
    check_left(numb-1, -dirs)

    # 해당 톱니바퀴는 무조건 회전시켜야 함
    arr[numb].rotate(dirs)

rlt = 0
for i in range(4):
    rlt += (2**i) * arr[i+1][0]

print(rlt)