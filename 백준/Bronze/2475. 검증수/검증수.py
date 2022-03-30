numbs = list(map(int, input().split()))
codes = 0
for numb in numbs:
    codes += pow(numb, 2)
code = codes % 10
print(code)