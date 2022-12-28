from collections import deque
import sys

N = int(sys.stdin.readline())

deq = deque()

for _ in range(N):
    d = sys.stdin.readline().split()

    if d[0] == 'push_front':
        deq.appendleft(d[1])
    elif d[0] == 'push_back':
        deq.append(d[1])
    elif d[0] == 'pop_front':
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif d[0] == 'pop_back':
        try:
            print(deq.pop())
        except:
            print(-1)
    elif d[0] == 'size':
        print(len(deq))
    elif d[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif d[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif d[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])