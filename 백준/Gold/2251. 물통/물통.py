'''
1. 3개의 물통에서 물을 한 번 옮기는 경우의 수는 6가지
2. a에 담긴 물을 x, b에 담긴 물을 y, c에 담긴 물을 z라고 할 때, c = x + y + z
3. 즉, c에 담긴 물의 양 z = c - x - y
'''

from collections import deque

a, b, c = map(int, input().split())

# 물을 담는 경우의 수 담을 큐 생성
# [x, y] 담아주기
q = deque()
q.append([0, 0])

# 해당 경우의 수 생각했는지 체크해줄 리스트
visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True  # x = 0, y = 0, z = total

ans = []

def move(x, y):
    # 이 경우의 수를 아직 생각한 적이 없다면,
    if not visited[x][y]:
        # 해당 경우를 생각해줘!
        visited[x][y] = True
        q.append([x, y])

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        # a물통이 비어있을 때, c물통에 남은 물의 양 저장
        if x == 0:
            ans.append(z)
        
        # a에서 b로 물 이동
        # water = a물통에서 b물통으로 들어갈 수 있는 물의 양이 얼마야?
        # b에 water를 담고, a에서 water를 빼줘
        water = min(x, b - y)
        move(x - water, y + water)
        # a에서 c로 물 이동
        water = min(x, c - z)
        move(x - water, y)

        # b에서 c로 물 이동
        water = min(y, c - z)
        move(x, y - water)
        # b에서 a로 물 이동
        water = min(y, a - x)
        move(x + water, y - water)

        # c에서 a로 물 이동
        water = min(z, a - x)
        move(x + water, y)
        # c에서 b로 물 이동
        water = min(z, b - y)
        move(x, y + water)

bfs()
ans.sort()

print(*ans)