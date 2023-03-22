import math

# 최소공배수를 최대공약수로 구하는 함수 정의
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    answer = 0
    
    stack = []
    for i in arr:
        if not stack: # stack이 비어있으면 일단 숫자를 넣어줘
            stack.append(i)
        else: # stack에 숫자 들어있으면, 그거 꺼내서 지금 숫자랑 최소공배수 구해서 다시 스택에 넣어줘
            stack.append(lcm(i, stack.pop()))
    return stack[-1]