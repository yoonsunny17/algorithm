arr = list(map(int, input().split()))
N = len(arr)
for i in range(N):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(' '.join(map(str, arr)))