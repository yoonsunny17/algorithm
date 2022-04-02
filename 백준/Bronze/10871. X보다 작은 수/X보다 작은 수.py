N, X = map(int, input().split())
arr = list(map(int, input().split()))

for numb in arr:
    if numb < X:
        print(numb, end=' ')