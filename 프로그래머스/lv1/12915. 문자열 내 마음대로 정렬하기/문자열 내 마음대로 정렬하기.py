def solution(strings, n):
    strings.sort(reverse=False, key=lambda x: (x[n], x))
    return strings