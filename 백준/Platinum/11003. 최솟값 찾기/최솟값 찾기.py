import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))

window = deque()
ans = []
for i in range(N):
    # min값 갱신하는 경우
    # window의 맨 뒤 값이, 이제 들어오는 값보다 큰 경우라면
    # 그 친구는 필요없어! pop해버려
    while window and window[-1][1] > numbs[i]:
        window.pop()
    
    # window가 다 찬 경우
    # 맨 앞의 인덱스보다 이제 들어오는 값의 인덱스가 크거나 같으면
    # 맨 앞의 친구는 빠져줘! popleft해버려
    while window and window[0][0] <= i-L:
        window.popleft()
    
    # window에 값 채워주기
    # while 중간에 있든, 여기에 있든 어짜피 while 둘 중 하나만 걸릴테니까
    # 여기있는게 효율적인가?
    window.append([i, numbs[i]])

    print(window[0][1], end=' ')