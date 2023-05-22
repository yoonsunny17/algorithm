def solution(n, left, right):
    ans = []
    
    for i in range(left, right+1):
        arr = []
        arr.append(i//n)
        arr.append(i%n)
        ans.append(max(arr)+1)

    return ans


###### time over...!!!!!! ######
# def solution(n, left, right):
#     answer = []
#     matrix = list([0 for _ in range(n)] for _ in range(n))
    
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 matrix[i][j] = i+1
#             else:
#                 matrix[i][j] = max(i, j)+1
    
#     arr = []
#     for i in range(n):
#         for j in range(n):
#             arr.append(matrix[i][j])

#     return arr[left:right+1]