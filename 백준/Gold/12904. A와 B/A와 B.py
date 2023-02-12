S = list(map(str, input()))
T = list(map(str, input()))

while True:
    if len(T) == len(S):
        break

    if T[-1] == 'A':
        T.pop()
    
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

print(1) if S == T else print(0)