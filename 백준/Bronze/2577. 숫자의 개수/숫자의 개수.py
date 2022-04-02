A = int(input())
B = int(input())
C = int(input())

rlt = A * B * C
numb_lst = [0] * 10

rlt = str(rlt)

for i in rlt:
    numb_lst[int(i)] += 1

for numb in numb_lst:
    print(numb)