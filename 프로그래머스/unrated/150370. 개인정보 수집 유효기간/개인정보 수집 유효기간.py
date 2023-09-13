def convert_time(t):
    y, m, d = map(int, t.split('.'))
    
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    term_dic = dict()
    today = convert_time(today)
    
    for term in terms:
        name, period = term.split() # name = 약관 종류, period = 약관 기간
        term_dic[name] = int(period) * 28

    for idx, privacy in enumerate(privacies):
        start, name = privacy.split() # start = 시작 날짜
        end = convert_time(start) + term_dic[name] # end = 종료 날짜
        
        if today >= end:
            answer.append(idx+1)
    
    return answer
