N = int(input())
codes = input()
numb = [int(input()) for _ in range(N)] # 알파벳 개수만큼 숫자 입력받기
memo = [] # empty stack

for code in codes:
    if code.isalpha(): # code가 알파벳인 경우에는,
        memo.append(numb[ord(code) - ord('A')]) # 스택에 숫자를 넣어줄건데, idx는 [ord(code) - ord('A')]야
    else: # code가 연산자라면, pop 해서 계산하자
        if len(memo) >= 2: # stack에 숫자 두 개 이상 들어있는 경우 두개 pop 해줘
            n2 = memo.pop()
            n1 = memo.pop()

            if code == '+':
                n = n1 + n2
                memo.append(n)
            elif code == '-':
                n = n1 - n2
                memo.append(n)
            elif code == '*':
                n = n1 * n2
                memo.append(n)
            elif code == '/':
                n = n1 / n2
                memo.append(n)

# 소수점 두번째 자리수까지 출력해줭
print(f'{memo[-1]:.2f}')