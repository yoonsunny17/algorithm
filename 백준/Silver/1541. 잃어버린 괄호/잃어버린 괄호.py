info = input().split('-')

arr = []

for i in info:
    calc = 0
    temp = i.split('+')
    for j in temp:
        calc += int(j)
    arr.append(calc)

numb = arr[0]
for i in range(1, len(arr)):
    numb -= arr[i]

print(numb)