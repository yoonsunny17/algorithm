N = int(input())
max_numb = 0

for N2 in range(N//2, N+1):
    lst = [N]
    lst.append(N2)
    
    i = 1
    while True:
        if lst[i-1] < lst[i]:
            break
        else:
            lst.append(lst[i-1]-lst[i])
            i += 1
    
    if max_numb <= len(lst):
        max_numb = len(lst)
        max_lst = lst

print(max_numb)
for j in range(len(max_lst)):
    print(max_lst[j], end=' ')