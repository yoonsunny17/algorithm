def solution(s):
    numbs = list(map(int, s.split()))
    
    return str(min(numbs)) + " " + str(max(numbs))