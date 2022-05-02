"""
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
"""


def gradingStudents(grades):
    ret = []
    for grade in grades:
        if grade % 5 >= 3 and grade >= 38:
            ret.append((grade // 5 + 1) * 5)
        else:
            ret.append(grade)
    return ret