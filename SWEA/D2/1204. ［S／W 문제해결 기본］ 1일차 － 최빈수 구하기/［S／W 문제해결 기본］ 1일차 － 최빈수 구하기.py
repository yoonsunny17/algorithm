from collections import Counter

T = int(input())
for _ in range(T):
    tc = int(input())
    score = list(map(int, input().split()))
    counter = Counter(score)

    print(f'#{tc} {counter.most_common(1)[0][0]}')