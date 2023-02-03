a, b, c = map(int, input().split())
time = [0] * 101
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        time[i] += 1
rlt = time.count(1) * a + time.count(2) * b * 2 + time.count(3) * c * 3

print(rlt)