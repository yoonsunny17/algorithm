H, M = input().split()
H = int(H)
M = int(M)
# 0 <= H <= 23, 0 <= M <= 59
# 입력이 현재 상근이 알람시계 설정이고, 출력이 -45M임
if 0 <= M < 45:
    if H != 0:
        H -= 1
        M += 15
    else:
        H += 23
        M += 15

else:
    M -= 45

print(H, M)