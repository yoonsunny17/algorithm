def solution(myString, pat):
    temp = myString.replace('A', 'C').replace('B', 'A')
    
    s = temp.replace('C', 'B')
    
    if pat in s:
        return 1
    else:
        return 0
