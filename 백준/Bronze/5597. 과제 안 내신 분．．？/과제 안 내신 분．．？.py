all = [i for i in range(1, 31)]
checked = list()
for _ in range(28):
    a = int(input())
    checked.append(a)

ans = []

for i in all:
    if i not in checked:
        ans.append(i)
ans.sort()
print(*ans, sep='\n')