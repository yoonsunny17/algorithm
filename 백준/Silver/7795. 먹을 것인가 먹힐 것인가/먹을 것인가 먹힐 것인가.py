T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    start, cnt = 0, 0

    for i in range(N):
        while True:
            if start == M or a[i] <= b[start]:
                cnt += start
                break
            else:
                start += 1

    print(cnt)