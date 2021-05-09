def std_num(stdscr):
    stdscr.addstr(0, 0, '- The number of students in the class: ')
    num = int(stdscr.getstr(1, 0).decode())
    return num


def course_num(stdscr):
    stdscr.addstr(0, 0, '- The number of courses is: ')
    num = int(stdscr.getstr(1, 0).decode())

    test = "hello"

    return num

