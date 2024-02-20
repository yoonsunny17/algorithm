def solution(a, b):
    first = int(str(a) + str(b))
    second = 2 * a * b
    
    if first >= second:
        return first
    else:
        return second
