T = int(input())
for t in range(T):
    R, S = input().split()
    for i in S:
        print(i*int(R), end='')
    print()