n = int(input())

temp = ''  # 숫자 더해줄 변수
lst = []  # temp에 더한 숫자 넣어줄 리스트

for _ in range(n):
    words = list(map(str, input()))

    for word in words:
        # 그 단어가 숫자라면 temp에 숫자 더해줘
        if word.isdigit():
            temp += word
        # 문자라면, temp에 더해져있는게 있는지 확인해보고
        else:
            if temp:
                # lst에 temp를 숫자로 더해줘
                lst.append(int(temp))
                temp = ''  # temp 초기화
    # temp 에 더해진거 남아있으면 그거 lst에 넣어줘
    if temp:
        lst.append(int(temp))
        temp = ''  # 다음 문장 확인해야하니까 이번에도 초기화 진행

# lst 정렬해줘
lst.sort()
for i in lst:
    print(i)
