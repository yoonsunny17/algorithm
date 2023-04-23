import math

def solution(n):
    answer = []
    arr = [True] * (n+1) # 모든 수가 소수라고 초기화
    
    # 2부터 n 제곱근까지 모든 수 확인해볼거임
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == True: # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 수 소수 제외해줘
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
                
    # 모든 소수 출력하기
    for i in range(2, n+1):
        if arr[i]:
            answer.append(i)
    return len(answer)