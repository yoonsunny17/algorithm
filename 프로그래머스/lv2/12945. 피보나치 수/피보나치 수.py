# def solution(n):
#     answer = 0
    
#     def fibonacci(numb):
#         if numb == 0:
#             return 0
#         elif numb == 1:
#             return 1
#         else:
#             return fibonacci(numb-1)+fibonacci(numb-2)

#     answer = fibonacci(n) % 1234567
#     return answer

def solution(n):
    answer = 0
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append((fibo[i-1] + fibo[i-2])%1234567)
    return fibo[-1]