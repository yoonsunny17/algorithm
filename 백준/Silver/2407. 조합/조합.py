import math

n, m = map(int, input().split())
rlt = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))
print(rlt)