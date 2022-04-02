N = int(input())
grades = list(map(int, input().split()))
max_grade = max(grades)
fixed_grades = []

for grade in grades:
    grade = (grade/max_grade)*100
    fixed_grades.append(grade)

new_avg = sum(fixed_grades) / N
print(new_avg)