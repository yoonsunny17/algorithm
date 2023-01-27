def sumcase(num):
    if num == 1:
        return 1
    
    if num == 2:
        return 2

    if num == 3:
        return 4

    else:
        return sumcase(num-1) + sumcase(num-2) + sumcase(num-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(sumcase(n))