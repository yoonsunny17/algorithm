N = int(input())
arr = []
for _ in range(N):
    R, G, B = map(int, input().split())
    arr.append([R, G, B])

for i in range(1, len(arr)):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[N-1]))