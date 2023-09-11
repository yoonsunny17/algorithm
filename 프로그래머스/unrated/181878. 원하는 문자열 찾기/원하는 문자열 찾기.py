def solution(myString, pat):
    my = myString.lower()
    p = pat.lower()
    
    if p in my:
        return 1
    else:
        return 0
