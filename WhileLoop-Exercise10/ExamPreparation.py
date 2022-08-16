poor_grades = int(input())

sum_grades = 0
count_grades = 0
last_problem = ''
input_line = input()
count_poor_grade = 0
has_failed = 0
while input_line != 'Enough':
    problem_name = input_line
    grade = int(input())
    if grade <= 4:
        count_poor_grade += 1

    last_problem = input_line
    sum_grades += grade
    count_grades += 1

    if poor_grades == count_poor_grade:
        has_failed = True
        break

    input_line = input()

if has_failed:
    print(f'You need a break, {count_poor_grade} poor grades.')
else:
    avg_grades = sum_grades / count_grades

    print(f'Average score: {avg_grades:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')
