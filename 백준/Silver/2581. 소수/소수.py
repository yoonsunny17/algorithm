M = int(input())
N = int(input())

lst = []
for numb in range(M, N+1):
    cnt = 0
    if numb > 1:
        for i in range(2, numb):
            if numb % i == 0:
                cnt += 1
                break
        if cnt == 0:
            lst.append(numb)

if len(lst) > 0:
    print(f'{sum(lst)}\n{min(lst)}')
else:
    print(-1)