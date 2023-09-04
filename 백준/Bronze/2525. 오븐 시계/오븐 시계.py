a, b = map(int, input().split())
c = int(input())

if (b + c) % 60 == 0:
    a = a + (b + c) // 60
    b = 0
    if a > 23:
        a = a % 24
 
else:
    a = a + (b + c) // 60
    b = (b + c) % 60

    if a > 23:
        a = a % 24

print(a, b)