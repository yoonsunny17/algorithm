import sys

def backtracking(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
            return
    
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    backtracking(cnt+1)
                    graph[i][j] = 'X'


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for t in teacher:
        for i in range(4):
            rr, cc = t

            while 0 <= rr < N and 0 <= cc < N:
                if graph[rr][cc] == 'O':
                    break
                if graph[rr][cc] == 'S':
                    return False
                rr += dr[i]
                cc += dc[i]
    
    return True


N = int(sys.stdin.readline())
graph = [list(map(str, input().split())) for _ in range(N)]
flag = False

teacher = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teacher.append([i, j])

backtracking(0)
print("YES") if flag else print("NO")