N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def check(line, L):
    # 경사로 설치 여부
    visited = [False for _ in range(N)]
    
    for i in range(N-1):
        # 바로 다음 위치가 동일한 높이면 그냥 ㄱㄱ
        if line[i] == line[i+1]:
            continue
        # 다음 위치랑 높이 차이가 1보다 크면 안됨
        elif abs(line[i]-line[i+1]) > 1:
            return False
        # 현재 높이가 다음 높이보다 높은 경우 >> 오른쪽 L만큼 체크
        elif line[i] > line[i+1]:
            tmp = line[i+1]
            for j in range(i+1, i+L+1): # i번째 칸부터 L개를 체크
                # 경사 길이가 범위 내라면
                if 0 <= j < N:
                    # 경사 놓으려는 곳의 높이가 하나라도 다른 경우 >> 설치 불가
                    if tmp != line[j]:
                        return False
                    # 높이는 동일한데 이미 경사로가 설치된 곳이면 >> 설치 불가
                    elif visited[j]:
                        return False
                    # 경사로 설치
                    visited[j] = True
                # 경사로 길이가 범위 벗어나면 >> 설치 불가
                else:
                    return False
        # 현재 높이가 다음 높이보다 낮은 경우 >> 자기 자신 포함 왼쪽 L개를 체크
        else:
            tmp = line[i]
            for j in range(i, i-L, -1): # 자기 자신부터 L개를 체크
                # 경사 길이가 범위 내라면
                if 0 <= j < N:
                    # 경사 놓으려는 곳의 높이가 하나라도 다른 경우 >> 설치 불가
                    if tmp != line[j]:
                        return False
                    # 높이는 동일한데 이미 경사로가 설치된 곳이면 >> 설치 불가
                    elif visited[j]:
                        return False
                    # 경사로 설치
                    visited[j] = True
                # 경사로 길이가 범위 벗어나면 >> 설치 불가
                else:
                    return False
    
    return True

ans = 0
# 1. 가로 체크
for i in matrix:
    if check(i, L):
        ans += 1

# 2. 세로 체크 >> 가로로 만들어서 확인해보자
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(matrix[j][i])
    if check(tmp, L):
        ans += 1

print(ans)