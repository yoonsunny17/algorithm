import sys

def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    
    if len(t) == 0:
        return 0
    
    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        dfs(t[1:][::-1])

S = list(input())
T = list(input())

dfs(T)  
print(0)