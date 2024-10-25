'''
각 학생의 예상 등수: 1 1 2 3 5
실제 받아야 할 등수: 1 2 3 4 5

각 등수를 정렬하고, 순서대로 각각 비교해서 차이 계산한다.
'''
import sys

N = int(sys.stdin.readline())
expected = []

for _ in range(N):
    rank = int(sys.stdin.readline())
    expected.append(rank)

expected.sort() # 예상 등수를 정렬해준다.

ans = 0
for i in range(1, N+1):
    ans += abs(i - expected[i-1])

print(ans)