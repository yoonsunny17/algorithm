N = int(input())
alpha = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpha_arr = []
ans = 0
lst = [] # 인풋값 받을 리스트

for _ in range(N):
    word = input()
    lst.append(word)

for word in lst:
    for i in range(len(word)):
        numb = 10 ** (len(word)-i-1)
        alpha[word[i]] += numb

for v in alpha.values():
    if v > 0:
        alpha_arr.append(v)

sorted_arr = sorted(alpha_arr, reverse=True)
for i in range(len(sorted_arr)):
    ans += sorted_arr[i] * (9-i)

print(ans)