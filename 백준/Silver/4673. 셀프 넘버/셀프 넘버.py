arr1 = set(range(1, 10001))
arr2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    arr2.add(i)

numb = sorted(arr1 - arr2)
for i in numb:
    print(i)