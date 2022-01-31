N = int(input())
numb = N
cnt = 0
while True:
    x = (numb % 10)
    y = (numb // 10)
    z = (x + y) % 10

    numb = (x * 10) + z
    cnt += 1
    if numb == N:
        break

print(cnt)