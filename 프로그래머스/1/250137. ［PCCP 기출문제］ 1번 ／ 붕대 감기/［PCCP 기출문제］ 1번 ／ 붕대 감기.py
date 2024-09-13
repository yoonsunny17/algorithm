def solution(bandage, health, attacks):
    t, x, y = bandage
    time, hp, cnt = 0, health, 0
    
    while attacks:
        # 시간 1초씩 카운팅 해줘
        time += 1

        # 공격 시간이라면, 체력 깎임
        if attacks[0][0] == time:
            hp -= attacks[0][1]
            
            # 체력이 0 이하인 경우 -1 return
            if hp <= 0:
                return -1
            # 연속 공격 cnt 초기화
            cnt = 0
            attacks.pop(0)

        # 공격 시간이 아니라면,
        else:
            # 연속 공격 스택 쌓아주고, 회복 x만큼씩 진행
            cnt += 1
            hp += x

            # 시전 시간이 쌓이면 추가 체력 y만큼 체력 회복하고, cnt 초기화
            if cnt == t:
                hp += y
                cnt = 0

            # 최대 체력을 넘어설 수는 없음
            if hp > health:
                hp = health
    
    return hp