def check(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def back(start, eggs):
    global broken
    
    # 맨 오른쪽 계란까지 탐색 했으면 끝
    if start == N:
        # 지금까지 계산된 값과, 현재 달걀들 상태 비교해서 최댓값 갱신
        broken = max(broken, check(eggs))
        return broken

    # 공격 대상의 계란이 깨져있는 경우, 옆의 계란으로 다시 공격해보자
    if eggs[start][0] <= 0:
        back(start+1, eggs)

    # 공격 대상의 계란이 깨져있지 않은 경우, 공격 진행해보자
    else:
        isBroken = True
        for i in range(N):
            # 공격하는 계란이 아니고, 깨진 계란이 아닌 경우
            # 깨진 계란이 아니라는 플래그 False 세우고
            # 백트래킹 진행
            if i != start and eggs[i][0] > 0:
                isBroken = False
                # 공격 개시 (서로 타격을 입음)
                eggs[start][0] -= eggs[i][1]
                eggs[i][0] -= eggs[start][1]
                back(start+1, eggs)
                eggs[start][0] += eggs[i][1]
                eggs[i][0] += eggs[start][1]
        
        # 공격할 수 있는 계란이 없는 경우 (모두 깨져있는 경우)
        # 마지막 계란으로 가 (끝내줘)
        if isBroken:
            back(N, eggs)

N = int(input())
eggs = []

for _ in range(N):
    power, weight = map(int, input().split())
    eggs.append([power, weight])

broken = 0
back(0, eggs)

print(broken)