import math

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N

for i in range(N):
    if students[i] - B > 0:
        cnt += math.ceil((students[i] - B) / C)

print(cnt)