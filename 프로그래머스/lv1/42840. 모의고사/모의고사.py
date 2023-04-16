def solution(answers):
    answer = []
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]
    
    for i in range(len(students)):
        for j in range(len(answers)):
            if answers[j] == students[i][j % (len(students[i]))]:
                scores[i] += 1
    
    for i, k in enumerate(scores):
        if k == max(scores):
            answer.append(i+1)
    
    return answer