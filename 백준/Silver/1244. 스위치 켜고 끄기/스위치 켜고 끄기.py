def switching(numb):   # 스위치 상태 바뀌는 함수 정의
    if switches[numb] == 1:
        switches[numb] = int(not switches[numb])
    else:
        switches[numb] = int(not switches[numb])
    return

N = int(input()) # 스위치 개수
switches = [-1] + list(map(int, input().split())) # 각 스위치 상태, i번째 = switches[i] 되도록 앞에 요소 추가
students = int(input()) # 학생 수

for _ in range(students):
    gender, numb = map(int, input().split()) # 각 학생의 성별 및 부여받은 번호

    # 남자인 경우
    if gender == 1:
        for i in range(numb, N+1):
            if i % numb == 0:
                switching(i)

    # 여자인 경우
    elif gender == 2:
        switching(numb) # 해당 번호 먼저 바꿈
        for j in range(1, N//2): # 좌우대칭 최대 반복 횟수 = 전체 스위치 개수//2
            if (numb + j) > N or (numb - j) < 0:
                break # 범위 넘어가는 경우 종료

            # 조건 충족하는 동안 상태 바꾸기                    
            if switches[numb-j] == switches[numb+j]:
                switching(numb-j)
                switching(numb+j)

            else:
                break

for i in range(1, N+1):
    print(switches[i], end=' ')
    if i % 20 == 0: # 20개 넘어가는 경우 줄바꿈
        print('')