import sys

def back(depth, lst):
    global max_v

    if len(lst) == N:
        total = 0
        for i in range(N-1):
            total += abs(lst[i] - lst[i+1])
        
        max_v = max(total, max_v)
        return
    
    for i in range(N):
        if not visited[i]:
            lst.append(numbs[i])
            visited[i] = True
            back(depth+1, lst)
            lst.pop()
            visited[i] = False

N = int(sys.stdin.readline())
numbs = list(map(int, sys.stdin.readline().split()))

max_v = 0
visited = [False] * N

back(0, [])

print(max_v)