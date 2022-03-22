T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    c = a + b
    print(f'Case #{tc}: {a} + {b} = {c}')