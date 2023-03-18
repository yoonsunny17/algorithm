# 최대공약수
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

# 최소공배수
def lcm(x, y):
    result = (x*y) // gcd(x,y)
    return result

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))