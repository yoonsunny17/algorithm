N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

arr = []
for i in range(1, len(sensors)):
    arr.append(sensors[i] - sensors[i-1])

arr.sort(reverse=True)
print(sum(arr[K-1:])) if K < N else print(0)