'''
Exercise 51 included a table that shows
the conversion from letter grades to 
grade points at a particular academic 
institution. In this exercise you will 
compute the grade point average of an 
arbitrary number of letter grades 
entered by the user. The user will enter 
a blank line to indicate that all of the
grades have been provided. For example, 
if the user enters A, followed by C+, 
followed by B, followed by a blank
line then your program should report a
grade point average of 3.1. You may find 
your solution to Exercise 51 helpful 
when completing this exercise. Your 
program does not need to do any error 
checking. It can assume that each value
entered by the user will always be a 
valid letter grade or a blank line.
'''

# Vars
grades = []
grade_points = []
sum = 0

CONVERSION_TABLE = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0,
}

# Input
while True:
    grade = input('Enter a grade: (blank to quit): ')
    if grade == '':
        break
    grades.append(grade)

# Conversion
for item in grades:
    grade_points.append(CONVERSION_TABLE[item])

# Calculation
for item in grade_points:
    sum += item

avg_grade = sum/len(grade_points)

# Output
print(f'The average grade points is {avg_grade}')