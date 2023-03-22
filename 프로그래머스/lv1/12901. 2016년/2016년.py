# 1월 1일이 금요일이므로 days에 금요일부터 넣어준다
# 1월부터 차례대로 날짜 넣어준다
# 지난 일수 다 더한 뒤 7로 나눈 나머지를 day로 출력하면 된다

def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
        answer += months[i]
    
    answer += b-1
    answer = answer%7
    return days[answer]