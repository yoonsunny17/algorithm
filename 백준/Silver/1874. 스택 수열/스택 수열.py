n = int(input())
stack, rlt = [], []  # 숫자 받을 스택, 연산 받을 스택
temp, flag = 1, True  # 숫자 변수, 연산 가능 여부 변수

for _ in range(n):
    numb = int(input())
    # temp 가 numb 보다 작거나 같은 동안에
    while temp <= numb:
        # stack에 temp 넣어주기 && temp 1씩 늘리기 && '+' 연산 넣기
        stack.append(temp)
        temp += 1
        rlt.append('+')
    
    # temp > numb 인 경우 => stack 맨 위에 숫자가 numb랑 같은지 비교해봐
    if stack[-1] == numb:
        # pop 해주기 && '-' 연산 넣기
        stack.pop()
        rlt.append('-')
    
    # 모든 경우 해당 안되면 불가능한 경우겠지
    else:
        flag = False

if flag == False:
    print('NO')
else:
    for i in rlt:
        print(i)