
class Student:
    __id_count = 0

    def __validateName(self, name) :
        if (len(name) > 1 ):
            return True
        return False

    def __validateDoB(self, dob):
        if (len(dob) > 1):
            return True
        return False

    def __init__(self, name, DoB):
        if (__validateName(name) != False):
            print("Name is not valid")
            return
        if (not(__validateDoB(DoB))):
            print("DoB is not valid")
            return

        self.__id = ++__id_count
        self.__DoB = DoB
        self.__name = name
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        if(__validateName(name)):
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
    __marks = {}
    
    def __init__(self, name):
        if(not(__validateName(name))):
            print("The name of the course is not valid")
            return 
        
        self.__name = name
        self.__id = ++__id_count
            
    def __validateName(self, name):
        if(len(name) > 1):
            return True
        return False

    def __validateMark(self, mark):
        if ( mark >= 0 and mark <= 100):
            return True
        return False
    
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
    
    def setMark(self, students):
        for student in students:
            stdName = student.getName()
            mark = input(f'Enter mark of {stdName}: ')
            while (not(__validateMark(mark))):
                print('The input mark is not valid \n')
                mark = input('Please re-enter the mark: ')
            __marks.update({stdName: mark})
     
    def describe(self):
        print(f'- The marks for {self.name} is: \n')
        for key, value in __marks.items():
            print(f'   + {key}: {value}')

def stdNum():
    num = int(input("- The number of students in the class: "))
    return num

def courseNum():
    num = int(input("- The number of courses is: "))
    return num

def showCourses(courses):
    print('- All courses that this class is currently taking: \n')
    for course in course:
        print(f'   + {course.getId()}. {course.getName()} \n')

def showStudents(students):
    print('- Student of this class: \n')
    for student in students:
        print(f'   + {student.getId()}. {student.getName()} \n')

if __name__ == "__main__":
    students = []
    courses = []

    for i in range(stdNum()):
        print('- Enter information of this student: \n')

        name = input('   + Enter student name: ')
        dob = input('   + Enter student dob: ')
    
        students.append(Student(name, dob))

    for i in range(courseNum()):
        print('- Enter information of this course: \n')
        course = Course()
        name = input('   + Enter course name: ')
        # while(not(course.repOk(name))):
        #     print('Your input is not in correct form. Please re-enter')
        #     name = input('   + Enter course name: ')
        
        course.setName(name)
        courses.append(course)

    



