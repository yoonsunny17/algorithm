def solution(arr):
    stk = []
    idx = 0
    
    while len(arr) > idx:
        if not len(stk):
            stk.append(arr[idx])
            idx += 1
        else:
            if stk[-1] < arr[idx]:
                stk.append(arr[idx])
                idx += 1
            else:
                stk.pop()
    return stk