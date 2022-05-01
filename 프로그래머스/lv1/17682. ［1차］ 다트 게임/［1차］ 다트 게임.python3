def solution(dartResult):
    stack = []
    dartResult = dartResult.replace('10', 'X')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i.isdigit() or i == 'X':
            stack.append(10 if i == 'X' else int(i))
        elif i in ('S', 'D', 'T'):
            numb = stack.pop()
            stack.append(pow(numb, bonus[i]))
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            numb = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(numb*2)
                
    rlt = sum(stack)
    return rlt