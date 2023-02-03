n = int(input())

arr = [0, 1, 1]

for i in range(3, 91):
    rlt = arr[i-1] + arr[i-2]
    arr.append(rlt)

print(arr[n])