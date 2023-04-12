t = int(input())

def recursion(curr, ans):
    if curr == n+1:
        sol(ans)
        return
    
    for x in op:
        recursion(curr+1, ans+x+str(curr)) # recursion(3, 1+x+2)

def sol(ans):
    # 공백은 붙여주고 계산 검토하자
    temp = ans.replace(' ', '')
    if eval(temp) == 0:
        print(ans)

for _ in range(t):
    n = int(input())
    arr = [] # 숫자와 연산자 조합 받을 리스트
    op = [' ', '+', '-']

    recursion(2, '1') # 일단 1은 넣어주고 시작하자!
    print()