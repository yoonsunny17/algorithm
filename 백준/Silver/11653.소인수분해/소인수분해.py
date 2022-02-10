def fact(x):
    d = 2

    while d <= x:
        if x % d == 0:
            x = x / d
            print(d)
        else:
            d = d + 1

N = int(input())
fact(N)