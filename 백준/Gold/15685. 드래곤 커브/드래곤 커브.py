N = int(input())

# d 우 상 좌 하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

matrix = [[0] * 101 for _ in range(101)]

for _ in range(N):
    sj, si, d, g = map(int, input().split())
    curve = [d]
    dragons = [[si, sj], [si+di[d], sj+dj[d]]] # 0세대까지 저장해주자
    
    for _ in range(g): # 세대만큼 반복해줄거야 (1세대부터 ~ g세대까지)
        for i in range(len(curve)-1, -1, -1): # 가장 마지막의 커브부터 역순으로 회전 후 다시 리스트에 저장
            rot = (curve[i]+1) % 4 # 회전의 규칙성
            curve.append(rot)
    
    for i in range(1, len(curve)):
        ci, cj = dragons[-1]
        ni, nj = ci+di[curve[i]], cj+dj[curve[i]]
        dragons.append([ni, nj])

    for dragon in dragons:
        matrix[dragon[0]][dragon[1]] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
            cnt +=1
print(cnt)