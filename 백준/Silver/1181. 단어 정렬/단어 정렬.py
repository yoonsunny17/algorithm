n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

set_arr = list(set(arr))

dict = []

for i in set_arr:
    dict.append((len(i), i))

answer = sorted(dict)

for len_word, word in answer:
    print(word)