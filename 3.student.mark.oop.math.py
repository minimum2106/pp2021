import math
import curses


class Student:
    __id_count = 0

    @staticmethod
    def __validate_name(name):
        if len(name) > 1:
            return True
        return False

    @staticmethod
    def __validate_dob(dob):
        if len(dob) > 1:
            return True
        return False

    def __init__(self, name, dob):
        if not(self.__validate_name(name)):
            print("Name is not valid")
            return
        if not(self.__validate_dob(dob)):
            print("DoB is not valid")
            return

        self.__id = ++self.__id_count
        self.__DoB = dob
        self.__name = name
        self.__marks = {}
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if self.__validate_name(name):
            self.__name = name
            return 
        print("Name is not valid")
    
    def get_id(self):
        return self.__id
    
    def get_dob(self):
        return self.__DoB

    def set_dob(self, dob):
        self.__DoB = dob
    
    def update_mark(self, course, credit, mark):
        self.__marks.update({course: [credit, mark]})

    def gpa(self):
        denominator = 0
        numerator = 0
        for value in self.__marks.values():
            denominator += value[0]
            numerator += value[0] * value[1]
        
        return numerator / denominator

    # @staticmethod
    # def repOk(name, dob):
    #     if (__validateName(name) and __validateDoB(dob)):
    #         return True
    #     return False


class Course:
    __id_count = 0

    @staticmethod
    def __validate_name(name):
        if len(name) > 1:
            return True
        return False

    @staticmethod
    def __validate_mark(mark):
        if 0 <= float(mark) <= 100:
            return True
        return False

    @staticmethod
    def __validate_credit(credit):
        if 1 <= int(credit) <= 4:
            return True
        return False 
    
    def __init__(self, name, credit):
        if not(self.__validate_name(name)):
            print("- The name of the course is not valid")
            return 
        if not(self.__validate_credit(credit)):
            print("- The number of credits is not valid")
        
        self.__name = name
        self.__id = ++self.__id_count
        self.__credit = int(credit)
        self.__marks = {}
    
    # @staticmethod
    # def repOk(name):
    #     if (__validateName(name)):
    #         return True
    #     return False

    @staticmethod
    def floor_mark(mark):
        return math.floor(float(mark) * 10) / 10

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if self.__validate_name(name):
            self.__name = name

    def get_id(self):
        return self.__id
    
    def set_credit(self, credit):
        if self.__validate_credit(credit):
            self.__credit = int(credit)

    def get_credit(self):
        return self.__credit

    def set_mark(self, students, stdscr):
        for student in students:
            std_name = student.get_name()
            stdscr.addstr(3, 0, f"Mark of {student.get_name()}: ")
            mark = stdscr.getstr(4, 0).decode()
            while not(self.__validate_mark(mark)):
                stdscr.addstr(5, 0, 'The input mark is not valid')
                mark = stdscr.getstr(6, 0).decode()
            
            mark = self.floor_mark(mark)
            self.__marks.update({std_name: mark})
            student.update_mark(self.__name, self.__credit, mark)

            # stdscr.refresh()
     
    def describe(self):
        print(f'- The marks for {self.__name} is:')
        for key, value in self.__marks.items():
            print(f'   + {key}: {value}')


def std_num(stdscr):
    stdscr.addstr(0, 0, '- The number of students in the class: ')
    num = int(stdscr.getstr(1, 0).decode())
    return num


def course_num(stdscr):
    stdscr.addstr(0, 0, '- The number of courses is: ')
    num = int(stdscr.getstr(1, 0).decode())
    return num


def show_course(courses, stdscr):
    stdscr.addstr(0, 0, '- All courses that this class is currently taking: ')
    for index, course in enumerate(courses):
        stdscr.addstr(index + 2, 0, f"{course.get_id()} : {course.get_name()}")


def show_students(students, stdscr):
    stdscr.addstr(0, 0, '- Student of this class: ')
    for index, student in enumerate(students):
        stdscr.addstr(index + 2, 0, f"{student.get_id()} : {student.get_name()}")


def contain_course(course, courses):
    for i in range(len(courses)):
        if course == courses[i].get_name():
            return i
    return -1


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


menu = ['Number of student',
        'Number of courses',
        "Add course mark",
        'Show student list',
        'Show course list',
        'Show class gpa',
        'Exit']


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
        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 0:
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

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 1:
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

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 2:
            stdscr.clear()
            curses.echo()

            stdscr.addstr(0, 0, "- Which course do you want to add marks")
            course_name = stdscr.getstr(1, 0).decode()
            course_index = contain_course(course_name, courses)
            if course_index < 0:
                stdscr.addstr(2, 0, "This course does not exist")
            else:
                courses[course_index].set_mark(students, stdscr)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 3:
            stdscr.clear()
            curses.echo()

            show_students(students, stdscr)

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 17]) and current_row == 4:
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
