cnt_lst = [0] * 42
for _ in range(10):
    numb = int(input())
    if cnt_lst[numb % 42] == 0:
        cnt_lst[numb % 42] = 1
    else:
        continue
rlt = cnt_lst.count(1)
print(rlt)