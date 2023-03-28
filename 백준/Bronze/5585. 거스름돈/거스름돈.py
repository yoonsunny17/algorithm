money = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in arr:
    cnt += money // i
    money %= i

print(cnt)
