word = input()
arr = [0] * 26

for i in word:
    arr[ord(i) - 97] += 1

print(*arr)