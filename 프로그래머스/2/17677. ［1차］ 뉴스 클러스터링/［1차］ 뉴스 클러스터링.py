from collections import Counter

def solution(str1, str2):
    # 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 2글자씩 자르기
    def make_two(s):
        multiset = []
        for i in range(len(s)-1):
            word = s[i:i+2]
            # 두글자 모두 알파벳인 경우에만 추가하기
            if word.isalpha():
                multiset.append(word)
        return multiset
    
    # 다중집합 생성
    arr1 = make_two(str1)
    arr2 = make_two(str2)
    
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    
    # intersection
    intersection = sum((counter1 & counter2).values())
    # union
    union = sum((counter1 | counter2).values())
    
    # 유사도 계산
    if union == 0: # 둘 다 공집합인 경우 > union = 0
        return 65536
    else:
        rlt = intersection / union
        return int(rlt * 65536)
