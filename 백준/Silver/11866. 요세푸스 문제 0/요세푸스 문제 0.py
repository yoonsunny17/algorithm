import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([x for x in range(1, n+1)])
removed = []

while q:
    q.rotate(-(k-1))
    removed.append(q.popleft())

print(f'<{", ".join(map(str, removed))}>')