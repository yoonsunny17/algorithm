M, N = map(int, input().split())

for numb in range(M, N+1):
    # 1은 소수가 아님
    if numb == 1:
        continue
    # 소수 판별 (에라토스테네스의 채 범위는 외우자..)
    for i in range(2, int(numb**0.5)+1):
        if numb % i == 0:
            break
    else:
        print(numb)