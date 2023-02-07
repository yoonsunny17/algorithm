C = int(input())
for tc in range(1, C+1):
    info = list(map(int, input().split()))

    scores = sum(info[1:])
    average = scores // info[0]

    cnt = 0  # 평균 넘는 학생 수
    for i in range(1, len(info)):
        if info[i] > average:
            cnt += 1
    
    print('{:.3f}%'.format(cnt / info[0] * 100))