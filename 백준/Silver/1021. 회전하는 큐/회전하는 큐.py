from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))

q = deque()
for i in range(1, N+1):
    q.append(i)

cnt = 0
for numb in target:
    while True:
        if q[0] == numb:
            q.popleft()
            break

        else:
            if q.index(numb) <= len(q) // 2:
                while q[0] != numb:
                    q.append(q.popleft())
                    cnt += 1

            else:
                while q[0] != numb:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)
