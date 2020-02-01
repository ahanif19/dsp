def find_first_names(students_input):
    '''
        Given a list of student names (students_input), return a list of the
        students' first names in alphabetical order
    '''
    return sorted([name.split()[0].capitalize() for name in students_input])

print(bool('students_input' in find_first_names.__doc__))
