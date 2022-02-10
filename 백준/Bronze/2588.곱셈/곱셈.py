num_1 = int(input())
num_2 = list(map(int,input()))

ans = [0, 0, 0]
for i in range(len(num_2)):
    ans[i] += (num_1 * num_2[i])

ans = ans[::-1]
rlt = ans[0] + ans[1] * 10 + ans[2] * 100

for a in ans:
    print(a)
print(rlt)