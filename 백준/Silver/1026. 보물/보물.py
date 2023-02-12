N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rlt = 0

for _ in range(N):
    rlt += min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(rlt)