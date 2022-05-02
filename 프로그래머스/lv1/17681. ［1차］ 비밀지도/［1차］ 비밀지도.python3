def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        rlt = bin(a|b)[2:]
        rlt = rlt.zfill(n)
        rlt = rlt.replace('1', '#')
        rlt = rlt.replace('0', ' ')
        answer.append(rlt)
    return answer