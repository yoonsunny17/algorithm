N = int(input())
cnt = 0
for n in range(N):
    codes = list(input())
    stack = []
    stack.append(codes[0])
    for i in range(1, len(codes)):
        if not len(stack):
            stack.append(codes[i])
        else:
            if codes[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(codes[i])

    if len(stack) != 0:
        cnt += 1

rlt = N - cnt
print(rlt)