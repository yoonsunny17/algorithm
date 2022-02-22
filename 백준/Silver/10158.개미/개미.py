w, h = map(int, input().split()) # w = 가로축, h = 세로축
p, q = map(int, input().split()) # 개미의 현재 위치 (p = w의 좌표, q = h의 좌표)
time = int(input()) # 개미가 움직이는 시간

# dp, dq는 실제 좌표계 내에서 개미가 몇번 왔다갔다 했는지 (순환했는지) 체크 가능
dp = (p + time) // w 
dq = (q + time) // h

# dp
if dp % 2 == 0:
    x = (p + time) % w

else:
    x = w - (p + time) % w

# dq
if dq % 2 == 0:
    y = (q + time) % h

else:
    y = h - (q + time) % h

print(f'{x} {y}')