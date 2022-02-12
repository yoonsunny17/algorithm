N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
print(numbers[0], numbers[-1])