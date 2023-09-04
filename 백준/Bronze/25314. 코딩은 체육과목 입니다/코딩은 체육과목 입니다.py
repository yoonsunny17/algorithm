N = int(input())

arr = []

while True:
    if N // 4 == 0:
        if N % 4 == 0:
            break
        else:
            arr.append('long')
            N -= N % 4

    else:
        arr.append('long')
        N -= 4

ans = ' '.join(arr) + ' int'

print(ans)