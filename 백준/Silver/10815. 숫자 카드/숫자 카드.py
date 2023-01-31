def binarySearch(numb, left, right):
    while left <= right:
        mid = (left + right) // 2
        if numb == cards[mid]:
            return mid
        elif numb < cards[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
numbs = list(map(int, input().split()))

left, right = 0, N-1

for numb in numbs:
    print(1, end=' ') if binarySearch(numb, left, right) is not None else print(0, end=' ')