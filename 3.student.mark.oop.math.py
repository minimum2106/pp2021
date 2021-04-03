import math 
import numpy as np

class Student:
    __id_count = 0

    def __validateName(self, name):
        if (len(name) > 1 ):
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
        self.__marks = {}
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        if(self.__validateName(name)):
            self.__name = name
            return 
        print("Name is not valid")
    
    def getId(self):
        return self.__id
    
    def getDoB(self):
        return self.__DoB

    def setDoB(self, dob):
        self.__DoB = dob
    
    def updateMark(self,course, credit, mark):
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

    def __validateName(self, name):
        if(len(name) > 1):
            return True
        return False

    def __validateMark(self, mark):
        if ( float(mark) >= 0 and float(mark) <= 100):
            return True
        return False

    def __validateCredit(self, credit):
        if (int(credit) >=1 and int(credit) <= 4):
            return True
        return False 
    
    def __init__(self, name, credit):
        if(not(self.__validateName(name))):
            print("- The name of the course is not valid")
            return 
        if(not(self.__validateCredit(credit))):
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

    def floorMark(self, mark):
        return math.floor(float(mark) * 10) / 10

    def getName(self):
        return self.__name
    
    def setName(self, name):
        if (self.__validateName(name)):
            self.__name = name

    def getId(self):
        return self.__id
    
    def setCredit(self, credit):
        if(self.__validateCredit(credit)):
            self.__credit = int(credit)
    
    def getCredit(self):
        return self.__credit
    
    def setMark(self, students):
        for student in students:
            stdName = student.getName()
            mark = input(f'   + mark of {stdName}: ')
            while (not(self.__validateMark(mark))):
                print('The input mark is not valid \n')
                mark = input('Please re-enter the mark: ')
            
            mark = self.floorMark(mark)
            self.__marks.update({stdName: mark})
            student.updateMark(self.__name, self.__credit, mark)
     
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
    print('- All courses that this class is currently taking: ')
    for course in courses:
        print(f'   + {course.getId()}. {course.getName()} ')

def showStudents(students):
    print('- Student of this class: ')
    for student in students:
        print(f'   + {student.getId()}. {student.getName()} ')

def containCourse(course, courses):
    for i in range(len(courses)):
        if (course == courses[i].getName()):
            return i
    return -1

def showGpa(students):
    print('Gpa of this class : ')
    for student in students:
        print(f'   + {student.getName()}: {student.gpa()} ')
    

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
        credit = input('   + Enter the number of credit of this course: ')
        courses.append(Course(name, credit))
    
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

    showGpa(students)
    



