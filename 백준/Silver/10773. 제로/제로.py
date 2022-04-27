K = int(input())

# 숫자 받을 스택 만들기
stack = []

for _ in range(K):
    n = int(input())

    if n != 0:
        stack.append(n)

    else:
        stack.pop()

print(sum(stack))