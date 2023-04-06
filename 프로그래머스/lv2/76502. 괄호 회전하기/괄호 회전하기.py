from collections import deque

def check(s):
    stack = deque() # 괄호 하나하나 넣어 줄 리스트
    for i in range(len(s)):
        if len(stack) == 0: # 스택이 비어 있는 경우라면,
            stack.append(s[i]) # 괄호를 스택에 넣어줘
        else: # 닫힌 괄호인지? 열린 괄호인지?
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s[i])
    return stack

def solution(s):
    ans = 0
    
    for i in range(len(s)):
        s = s[1:] + s[0] # 맨 앞의 괄호를 맨 뒤로 보내기
        if len(check(s)) == 0:
            ans += 1
        
    return ans