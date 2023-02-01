n = int(input())
w = list(int(input()) for _ in range(n))
w.sort(reverse=True)

arr = []
for i in range(len(w)):
    arr.append(w[i]*(i+1))

print(max(arr))