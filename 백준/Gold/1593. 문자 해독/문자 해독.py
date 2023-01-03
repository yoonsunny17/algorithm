g, s = map(int, input().split())
W = input()
S = input()

answer = 0

# 아스키코드로 변환해주자
# 소문자가 65 - 90, 대문자가 97 - 122
# 귀찮으니까 65 - 122 라고 보고 길이가 58인 리스트 만들기
wa = [0] * 58
sa = [0] * 58

for i in W:
    wa[ord(i) - 65] += 1

# 구간 비교 시작할 시작점 start와 현재 카운팅한 알파벳 길이 length를 초기화하고 시작한다
start, length = 0, 0
for j in range(s):
    sa[ord(S[j]) - 65] += 1
    length += 1

    # 길이가 W의 길이와 같을 때
    if length == g:
        # 둘이 동일하다면
        if wa == sa:
            # 경우의 수 하나 더해주기
            answer += 1
        # 전체 문자열에서 하나 빼줄 것
        # 시작 지점은 오른쪽으로 하나 이동시키고, 길이는 하나 더 줄여줄 것
        sa[ord(S[start]) - 65] -= 1
        start += 1
        length -= 1

print(answer)