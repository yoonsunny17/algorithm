n, k = map(int, input().split())
lst = list(map(int, input().split()))

sum_arr = list()
sum_arr.append(sum(lst[:k]))

for i in range(n-k):
    sum_arr.append(sum_arr[i] - lst[i] + lst[k+i])

print(max(sum_arr))