def dfs(t):
    global flag

    if len(t) == len(S):
        if t == S:
            flag = True
        return

    if t[0] == 'B':
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()
    
    if t[-1] == 'A':
        t.pop()
        dfs(t)
        t.append('A')

S = list(input())
T = list(input())

flag = False
dfs(T)

if flag == False:
    print(0)
else:
    print(1)
