
def show_course(courses, stdscr):
    stdscr.addstr(0, 0, '- All courses that this class is currently taking: ')
    for index, course in enumerate(courses):
        stdscr.addstr(index + 2, 0, f"{course.get_id()} : {course.get_name()}")


def show_students(students, stdscr):
    stdscr.addstr(0, 0, '- Student of this class: ')
    for index, student in enumerate(students):
        stdscr.addstr(index + 2, 0, f"{student.get_id()} : {student.get_name()}")


def sort(students):
    for i in range(len(students) - 1):
        for j in range(len(students) - i - 1):
            if students[j].gpa() < students[j + 1].gpa():
                students[j], students[j + 1] = students[j + 1], students[j]


def show_gpa(students, stdscr):
    std_desc = []

    stdscr.addstr(0, 0, '- Gpa of this class: ')
    for student in students:
        std_desc.append(student)

    sort(std_desc)

    for idx, std in enumerate(std_desc):
        stdscr.addstr(idx + 1, 0, f'   + {std.get_name()}: {std.gpa()}')
