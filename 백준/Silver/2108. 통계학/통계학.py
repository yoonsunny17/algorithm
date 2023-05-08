import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
print(round(sum(arr) / N))
print(arr[N//2])

dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

numb = []
for k, v in dic.items():
    if v == max(dic.values()):
        numb.append(k)

if len(numb) > 1:
    print(numb[1])
else:
    print(numb[0])

print(max(arr) - min(arr))