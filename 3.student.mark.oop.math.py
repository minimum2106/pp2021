class Student:
    __id_count = 0

    def __validateName(self, name):
        if (len(name) > 1):
            return True
        return False

    def __validateDoB(self, dob):
        if (len(dob) > 1):
            return True
        return False

    def __init__(self, name, DoB):
        if (self.__validateName(name) == False):
            print("Name is not valid")
            return
        if (self.__validateDoB(DoB) == False):
            print("DoB is not valid")
            return

        self.__id = ++self.__id_count
        self.__DoB = DoB
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        if (self.__validateName(name)):
            self.__name = name
            return
        print("Name is not valid")

    def getId(self):
        return self.__id

    def getDoB(self):
        return self.__DoB

    def setDoB(self, dob):
        self.__DoB = dob

    # @staticmethod
    # def repOk(name, dob):
    #     if (__validateName(name) and __validateDoB(dob)):
    #         return True
    #     return False


class Course:
    __id_count = 0

    def __validateName(self, name):
        if (len(name) > 1):
            return True
        return False

    def __validateMark(self, mark):
        if (float(mark) >= 0 and float(mark) <= 100):
            return True
        return False

    def __init__(self, name):
        if (not (self.__validateName(name))):
            print(" The name of the course is not valid")
            return

        self.__name = name
        self.__id = ++self.__id_count
        self.__marks = {}

    # @staticmethod
    # def repOk(name):
    #     if (__validateName(name)):
    #         return True
    #     return False

    def getName(self):
        return self.__name

    def setName(self, name):
        if (__validateName(name)):
            self.__name = name

    def getId(self):
        return self.__id

    def setMark(self, students):
        for student in students:
            stdName = student.getName()
            mark = input(f'Enter mark of {stdName}: ')
            while (not (self.__validateMark(mark))):
                print('The input mark is not valid \n')
                mark = input('Please re-enter the mark: ')
            self.__marks.update({stdName: mark})

    def describe(self):
        print(f'- The marks for {self.__name} is:')
        for key, value in self.__marks.items():
            print(f'   + {key}: {value}')


def stdNum():
    num = int(input("- The number of students in the class: "))
    return num


def courseNum():
    num = int(input("- The number of courses is: "))
    return num


def showCourses(courses):
    print('- All courses that this class is currently taking: \n')
    for course in courses:
        print(f'   + {course.getId()}. {course.getName()} \n')


def showStudents(students):
    print('- Student of this class: \n')
    for student in students:
        print(f'   + {student.getId()}. {student.getName()} \n')


def containCourse(course, courses):
    for i in range(len(courses)):
        if (course == courses[i].getName()):
            return i
    return -1


if __name__ == "__main__":
    students = []
    courses = []

    for i in range(stdNum()):
        print('- Enter information of this student: ')

        name = input('   + Enter student name: ')
        dob = input('   + Enter student dob: ')

        students.append(Student(name, dob))

    for i in range(courseNum()):
        print('- Enter information of this course: ')
        name = input('   + Enter course name: ')
        # while(not(course.repOk(name))):
        #     print('Your input is not in correct form. Please re-enter')
        #     name = input('   + Enter course name: ')

        courses.append(Course(name))

    user_input = input("- Do you want to input marks for any course ? ")
    courseIndex = containCourse(user_input, courses)
    if (courseIndex < -1):
        print("- There is no course like that")
    else:
        courses[courseIndex].setMark(students)
        courses[courseIndex].describe()

    ans = input("- Do you want to print out students and courses ? yes/no ")
    if (ans == "yes"):
        showStudents(students)
        showCourses(courses)





