from collections import deque

N = int(input())
q = deque([x for x in range(1, N+1)])

while q:
    if len(q) == 1:
        break

    else:
        q.popleft()
        q.rotate(-1)

print(q[0])