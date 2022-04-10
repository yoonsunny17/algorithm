N = int(input())
A_lst = list(map(int, input().split()))
B, C = map(int, input().split())

rlt = 0
for A in A_lst:
    A -= B
    rlt += 1
    if A > 0:
        rlt += A // C

        if A % C > 0:
            rlt += 1

print(rlt)