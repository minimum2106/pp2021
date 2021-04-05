import math
import curses


class Student:
    __id_count = 0

    def __validate_name(self, name):
        if len(name) > 1:
            return True
        return False

    def __validate_dob(self, dob):
        if len(dob) > 1:
            return True
        return False

    def __init__(self, name, DoB):
        if not(self.__validate_name(name)):
            print("Name is not valid")
            return
        if not(self.__validate_dob(DoB)):
            print("DoB is not valid")
            return

        self.__id = ++self.__id_count
        self.__DoB = DoB
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
        total = 0
        sum = 0
        for value in self.__marks.values():
            total += value[0]
            sum += value[0] * value[1]
        
        return sum / total

    # @staticmethod
    # def repOk(name, dob):
    #     if (__validateName(name) and __validateDoB(dob)):
    #         return True
    #     return False


class Course:
    __id_count = 0

    def __validate_name(self, name):
        if len(name) > 1:
            return True
        return False

    def __validate_mark(self, mark):
        if 0 <= float(mark) <= 100:
            return True
        return False

    def __validate_credit(self, credit):
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

    def floor_mark(self, mark):
        return math.floor(float(mark) * 10) / 10

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if self.__validate_name(name):
            self.__name = name

    def get_id(self):
        return self.__id
    
    def setCredit(self, credit):
        if self.__validate_credit(credit):
            self.__credit = int(credit)

    def get_credit(self):
        return self.__credit

    def set_mark(self, students):
        for student in students:
            std_name = student.getName()
            mark = input(f'   + mark of {std_name}: ')
            while not(self.__validate_mark(mark)):
                print('The input mark is not valid \n')
                mark = input('Please re-enter the mark: ')
            
            mark = self.floor_mark(mark)
            self.__marks.update({std_name: mark})
            student.updateMark(self.__name, self.__credit, mark)
     
    def describe(self):
        print(f'- The marks for {self.__name} is:')
        for key, value in self.__marks.items():
            print(f'   + {key}: {value}')


def std_num():
    num = int(input("- The number of students in the class: "))
    return num


def course_num():
    num = int(input("- The number of courses is: "))
    return num


def show_course(courses):
    print('- All courses that this class is currently taking: ')
    for course in courses:
        print(f'   + {course.get_id()}. {course.get_name()} ')


def show_students(students):
    print('- Student of this class: ')
    for student in students:
        print(f'   + {student.get_id()}. {student.get_name()} ')


def contain_course(course, courses):
    for i in range(len(courses)):
        if course == courses[i].getName():
            return i
    return -1


def sort(students):
    for i in range(len(students) - 1):
        for j in range(len(students) - i - 1):
            if students[j].gpa() < students[j + 1].gpa():
                students[j], students[j + 1] = students[j + 1], students[j] 


def show_gpa(students):
    std_desc = []
    print('Gpa of this class : ')
    for student in students:
        std_desc.append(student)

    sort(std_desc)
            
    for std in std_desc:
        print(f'   + {std.get_name()}: {std.gpa()}')


menu = ['AddStudent', 'AddCourse', 'Exit']


def print_menu(stdscr, selected_row):
    stdscr.clear()

    h, w = stdscr.getmaxyx()

    for index, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu) + index

        if index == selected_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu):
            current_row += 1 
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.refresh()
            stdscr.getch()

            if current_row == len(menu) - 1:
                break
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


if __name__ == "__main__":
    curses.wrapper(main)
    students = []
    courses = []

    for i in range(std_num()):
        print('- Enter information of this student: ')

        name = input('   + Enter student name: ')
        dob = input('   + Enter student dob: ')
    
        students.append(Student(name, dob))

    for i in range(course_num()):
        print('- Enter information of this course: ')
        name = input('   + Enter course name: ')
        # while(not(course.repOk(name))):
        #     print('Your input is not in correct form. Please re-enter')
        #     name = input('   + Enter course name: ')
        credit = input('   + Enter course number of credit: ')
        courses.append(Course(name, credit))
    
    user_input = input("- Do you want to input marks for any course ? ")
    courseIndex = contain_course(user_input, courses)
    if courseIndex < -1:
        print("- There is no course like that")
    else:
        courses[courseIndex].set_mark(students)
        courses[courseIndex].describe()

    ans = input("- Do you want to print out students and courses ? yes/no ")
    if ans == "yes":
        show_students(students)
        show_course(courses)

    show_gpa(students)
