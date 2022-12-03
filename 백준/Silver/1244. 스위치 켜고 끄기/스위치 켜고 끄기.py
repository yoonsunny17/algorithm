N = int(input())  # 스위치 개수
switches = [-1] + list(map(int, input().split()))  # 스위치 상태 0, 1
students = int(input())  # 학생 수

def switching(numb):
    if switches[numb] == 1:
        switches[numb] = 0
    else:
        switches[numb] = 1

for _ in range(students):
    gender, numb = map(int, input().split())

    if gender == 1:
        for i in range(numb, N+1):
            if i % numb == 0:
                switching(i)

            else:
                continue

    # 여학생인 경우
    elif gender == 2:
        switching(numb)
        for j in range(1, N//2):
            if (numb + j) > N or (numb - j) < 0:
                break

            if switches[numb - j] == switches[numb + j]:
                switching(numb + j)
                switching(numb - j)

            else:
                break

for i in range(1, N+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print('')