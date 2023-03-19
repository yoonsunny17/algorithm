def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        # 1. 중복 단어가 있거나  2. 앞 단어랑 이어지지 않는 경우
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]

    return answer