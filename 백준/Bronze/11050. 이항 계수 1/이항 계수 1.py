from math import factorial

n, k = map(int, input().split())

answer = factorial(n) // (factorial(n-k) * factorial(k))

print(answer)