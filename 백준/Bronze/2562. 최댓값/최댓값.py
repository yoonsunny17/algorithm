numbers = [int(input()) for _ in range(9)]

for i in range(9):
    if numbers[i] == max(numbers):
        print(f'{numbers[i]}\n{i+1}')