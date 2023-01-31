import sys

N = int(sys.stdin.readline())
numbs = list(map(int, sys.stdin.readline().split()))
numbs.sort()
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for target in check:
    left = 0
    right = N-1
    flag = False

    while left <= right:
        mid = (left + right) // 2
        
        if target == numbs[mid]:
            flag = True
            print(1)
            break

        elif target > numbs[mid]:
            left = mid + 1
        
        else:
            right = mid - 1

    if not flag:
        print(0)