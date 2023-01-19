n, k = map(int, input().split())
students = list(map(int, input().split()))

arr = []
for i in range(1, n):
    arr.append(students[i] - students[i-1])

arr.sort(reverse=True)
print(sum(arr[k-1:]))