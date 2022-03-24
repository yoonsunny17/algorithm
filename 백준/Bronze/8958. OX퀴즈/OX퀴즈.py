T = int(input())
for tc in range(T):
    codes = input()
    cnt = 0
    lst = [0]*len(codes)
    for i in range(len(codes)):
        if codes[i] == 'O':
            cnt += 1
            lst[i] = cnt
        else:
            cnt = 0
    print(sum(lst))