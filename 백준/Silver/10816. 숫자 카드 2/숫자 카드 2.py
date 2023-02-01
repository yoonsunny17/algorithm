import sys

def binarySearch(target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if target == cards[mid]:
            return cards[mid]
        elif target < cards[mid]:
            return binarySearch(target, left, mid-1)
        else:
            return binarySearch(target, mid+1, right)
    return None

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, n-1

dictionary = dict()
for i in cards:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for target in arr:
    print(dictionary[target], end=' ') if binarySearch(target, left, right) is not None else print(0, end=' ')