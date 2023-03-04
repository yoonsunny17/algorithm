N = int(input())

arr = []
check = [False]*1001

for _ in range(N):
    d, w = map(int, input().split())
    arr.append([d, w])

arr.sort(reverse=True, key=lambda x: x[1])
answer = 0

for day, worth in arr:
    i = day
    # 과제를 할 날짜를 탐색하기
    while i > 0 and check[i]:
        i -= 1
    
    # 과제를 할 날짜가 없다면 패스하기
    if i == 0:
        continue
    else:
        check[i] = True
        answer += worth

print(answer)