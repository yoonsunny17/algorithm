def solution(myString):
    arr = sorted(i for i in myString.split('x') if i)
    return arr