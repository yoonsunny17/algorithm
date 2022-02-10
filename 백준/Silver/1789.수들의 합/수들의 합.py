S = int(input())
cnt = 0
n = 1

while True:

    if S - n < 0:
        break

    if S - n >= 0:
        S = S - n
        n += 1
        cnt += 1

print(cnt)