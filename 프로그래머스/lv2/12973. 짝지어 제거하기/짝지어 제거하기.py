def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0: # stack이 비어있으면, 문자열 넣어줘
            stack.append(s[i])
            
        else: # stack이 비어있지 않으면, 확인해줘야겠지
            if stack[-1] == s[i]: # stack 맨 위에 있는 알파벳이랑 지금 넣으려는 애랑 같으면
                stack.pop() # pop 해주고 넘어가
                continue
            else:
                stack.append(s[i])

    # stack이 비어있으면 성공, 아니면 실패
    return 1 if len(stack) == 0 else 0
