N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
coins.sort(reverse=True)

rlt = 0  # 동전 몇개 썼는지 세어줄 변수

for coin in coins:
    rlt += K // coin  # 동전으로 나눈 몫 = 동전으로 나눈 개수
    K = K % coin  # 동전으로 나눈 나머지 = 잔돈

print(rlt)