N, M = map(int, input().split())
a = set()
b = set()

for _ in range(N):
    name = input()
    a.add(name)

for _ in range(M):
    check = input()
    b.add(check)

rlt = sorted(list(a & b))
print(len(rlt))
for i in rlt:
    print(i)