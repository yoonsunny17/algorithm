from collections import deque

def solution(numbers, hand):
    answer = ''
    
    # 처음 왼손, 오른손 위치 초기화
    left, right = [3, 0], [3, 2]
    
    # 숫자 패드 위치 딕셔너리로 저장
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]
    }
    
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for numb in numbers:
        # 왼쪽 손으로 눌러야 하는 자판인 경우
        if numb in [1, 4, 7]:
            answer += 'L' # 왼쪽 표시하고
            left = keypad[numb] # 현재 왼손 위치 갱신하자
            
        # 오른쪽 손으로 눌러야 하는 자판인 경우
        elif numb in [3, 6, 9]:
            answer += 'R' # 오른쪽 표시하고
            right = keypad[numb] # 현재 오른손 위치 갱신하자
            
        # 2, 5, 8, 0인 경우, 어느 손이 더 가까운지 확인
        else:
            left_dis = abs(left[0] - keypad[numb][0]) + abs(left[1] - keypad[numb][1])
            right_dis = abs(right[0] - keypad[numb][0]) + abs(right[1] - keypad[numb][1])
            
            # 왼손이 가까운 경우
            if left_dis < right_dis:
                answer += 'L'
                left = keypad[numb]
            
            # 오른손이 가까운 경우
            elif left_dis > right_dis:
                answer += 'R'
                right = keypad[numb]
                
            # 거리가 동일한 경우
            else:
                if hand == 'left':
                    answer += 'L'
                    left = keypad[numb]
                else:
                    answer += 'R'
                    right = keypad[numb]
            
    return answer