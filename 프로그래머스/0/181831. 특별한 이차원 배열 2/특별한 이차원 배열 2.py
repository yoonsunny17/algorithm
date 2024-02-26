def solution(arr):
    answer, tmp = 0, 0
    
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == arr[j][i]:
                tmp += 1
    
    if tmp == n ** 2:
        answer = 1

    return answer