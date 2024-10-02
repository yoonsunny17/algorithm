from collections import deque

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    commands = deque(commands)
    video_len, pos, op_start, op_end = video_len.split(":"), pos.split(":"), op_start.split(":"), op_end.split(":")
    
    video_len, pos, op_start, op_end = int(video_len[0]) * 60 + int(video_len[1]), int(pos[0]) * 60 + int(pos[1]), int(op_start[0]) * 60 + int(op_start[1]), int(op_end[0]) * 60 + int(op_end[1])
    
    # 수행할 명령이 남아있을 때까지 반복
    while commands:
        # 현재 위치가 오프닝 구간 사이라면, 오프닝 끝으로 이동해줘
        if op_start <= pos <= op_end:
            pos = op_end
        
        # 명령을 수행해줘
        command = commands.popleft()
        if command == "next":
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos += 10
        elif command == "prev":
            if pos - 10 < 0:
                pos = 0
            else:
                pos -= 10
    
    # 마지막 command까지 수행했을 때, 오프닝 구간 사이라면 오프닝 끝으로 이동해줘
    if op_start <= pos <= op_end:
        pos = op_end

    a = pos // 60
    b = pos % 60

    return f'{a:02}:{b:02}'