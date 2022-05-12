from collections import defaultdict

student_grades = {
    "Jack" : [85, 91],
    "Jill" : [86, 89]
}

# Best solution. Default dict.
# If the key does not exist, it will create the new key and bind the default value to it.

student_grades = defaultdict(list, student_grades)
def set_grades_best_solution(name, score):
    student_grades[name].append(score)

def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]
    return []

def get_grades_better(name):
    default = [] # Optional, if no default value is specified, None is returned by default.
    return student_grades.get(name, default)

def get_grades_with_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]

def get_grades_with_assignment_better(name):
    return student_grades.setdefault(name, [])

def set_grades_naive(name, score):
    if name in student_grades:
        student_grades[name].append(score)
    else:
        student_grades[name] = [score]

def set_grades_better(name, score):
    student = get_grades_with_assignment(name)
    student.append(score)
