import curses
import os

from output import show_students, show_course, show_gpa
from input import std_num, course_num

from domains.student import Student
from domains.course import Course


menu = ['Number of student',
        'Number of courses',
        "Add course mark",
        'Show student list',
        'Show course list',
        'Show class gpa',
        'Exit']


def contain_course(course, courses):
    for i in range(len(courses)):
        if course == courses[i].get_name():
            return i
    return -1


def print_menu(stdscr, selected_row):
    stdscr.clear()

    h, w = stdscr.getmaxyx()

    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index

        if index == selected_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    students = []
    courses = []
    current_row = 0

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu):
            current_row += 1
        elif key == curses.KEY_ENTER and current_row == 0:
            stdscr.clear()
            curses.echo()

            std_number = std_num(stdscr)

            for i in range(std_number):
                stdscr.clear()
                stdscr.addstr(0, 0, f"- Student number {i + 1} info is: ")
                stdscr.addstr(2, 0, "   + Student name: ")
                student_name = stdscr.getstr(3, 0).decode()
                stdscr.addstr(4, 0, '   + Student DoB: ')
                dob = stdscr.getstr(5, 0).decode()

                students.append(Student(student_name, dob))
                stdscr.refresh()

            with open("student.txt", "w") as sf:
                for student in students:
                    sf.write(f"{student.get_id()} : {student.get_name()} : {student.get_dob()} \n")

            stdscr.getch()

        elif key == curses.KEY_ENTER and current_row == 1:
            stdscr.clear()
            curses.echo()

            course_number = course_num(stdscr)

            for i in range(course_number):
                stdscr.addstr(0, 0, f"- Course number {i + 1} info is: ")
                stdscr.addstr(1, 0, f"   + Course  {i + 1} name: ")
                course_name = stdscr.getstr(2, 0).decode()
                stdscr.addstr(3, 0, f"   + Course {i + 1} credit: ")
                course_credit = stdscr.getstr(4, 0).decode()

                courses.append(Course(course_name, course_credit))
                stdscr.refresh()

            with open("course.txt", "w") as cf:
                for course in courses:
                    cf.write(f"{course.get_id()}: {course.get_name()} with {course.get_credit()} credit \n")

            stdscr.getch()

        elif key == curses.KEY_ENTER and current_row == 2:
            stdscr.clear()
            curses.echo()

            stdscr.addstr(0, 0, "- Which course do you want to add marks")
            course_name = stdscr.getstr(1, 0).decode()
            course_index = contain_course(course_name, courses)
            if course_index < 0:
                stdscr.addstr(2, 0, "This course does not exist")
            else:
                courses[course_index].set_mark(students, stdscr)
                with open("mark.txt", "w") as mf:
                    mf.write(f"{course_name} \n")
                    for name, mark in courses[course_index].get_mark().items():
                        mf.write(f"{name} : {mark} \n")
                    mf.write("\n")

            stdscr.getch()

        elif key == curses.KEY_ENTER and current_row == 3:
            stdscr.clear()
            curses.echo()

            show_students(students, stdscr)

            stdscr.getch()

        elif key == curses.KEY_ENTER and current_row == 4:
            stdscr.clear()
            curses.echo()

            show_course(courses, stdscr)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 5:
            stdscr.clear()
            curses.echo()

            show_gpa(students, stdscr)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 6:
            break

        print_menu(stdscr, current_row)


if __name__ == "__main__":
    curses.wrapper(main)
