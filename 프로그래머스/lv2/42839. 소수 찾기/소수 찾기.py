from itertools import permutations

def find(number):
    numb = int(number)
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perms = []
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            perms.append(''.join(list(perm)))
    
    perms = list(set(perms))
    for num in perms:
        if num != '1' and num[0] != '0':
            if find(num) == True:
                answer += 1
    

    return answer