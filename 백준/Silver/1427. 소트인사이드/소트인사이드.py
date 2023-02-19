n = list(map(int, str(input())))
n.sort(reverse=True)
for i in n:
    print(i, end='')