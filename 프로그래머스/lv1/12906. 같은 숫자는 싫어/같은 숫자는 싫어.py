# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             answer.append(arr[i])

#     return answer

def solution(arr):
    answer = []
    
    for i in arr:
        # stack이 비어있거나 or stack 마지막에 들어간 숫자랑 다른 숫자면 넣어줘
        if (len(answer) == 0) or (answer[-1] != i):
            answer.append(i)
            
    return answer