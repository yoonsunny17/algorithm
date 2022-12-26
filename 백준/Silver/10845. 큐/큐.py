from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    q = sys.stdin.readline().split()  # 음절? 로 나누어서 생각

    if q[0] == 'push':
        queue.append(int(q[1]))
    elif q[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif q[0] == 'size':
        print(len(queue))
    elif q[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif q[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif q[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])