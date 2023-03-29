N = int(input())
numbs = list(map(int, input().split()))
numbs.sort()

print(numbs[0]*numbs[-1])