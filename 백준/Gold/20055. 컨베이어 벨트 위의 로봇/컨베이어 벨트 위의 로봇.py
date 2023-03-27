from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*N)
res = 0

while True:
    # 조건 1
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 # 로봇이 빠지는 부분이니까 0

    if sum(robot): # 로봇이 존재한다면,
        for i in range(N-2, -1, -1): # 로봇이 내려가는 부분의 인덱스가 i-1이니까 그 전인 i-2부터 역행 검사
            # 조건 2-1
            # 로봇이 이동하려는 칸에 로봇이 없고, 벨트 내구도가 1 이상일 때 가능
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                # 로봇 이동시켜주고, 내구도 1 감소시켜줘
                robot[i], robot[i+1] = 0, 1
                belt[i+1] -= 1
        robot[-1] = 0 # 그리고 마지막에 있는 로봇도 빼줘
    
    # 조건 3
    # 만약에 맨 앞에 로봇이 없고, 맨 앞 벨트 내구도가 1이상이면
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    res += 1

    # 조건 4
    # 벨트 내구도가 0인 칸 개수가 K개 이상인 경우 종료해줘
    if belt.count(0) >= K:
        break

print(res)
