students = []
courses = []
marks = []

def stdNum():
    num = int(input(" The number of students in the class: "))
    return num

def stdInfo():
    stdId = input("This student id: ")
    stdName = input("This student name is: ")
    stdDoB = input("This student DoB: ")
    return {"id": stdId, "name": stdName, "Dob": stdDoB}

def courseNum():
    num = int(input("The number of courses is: "))
    return num

def courseInfo():
    courseId = input("This course id: ")
    courseName = input("This course name is: ")
    return {"id": courseId, "name": courseName}

def insertCourseMark(course) :
    marks.append({course: {}})
    for i in range(len(students)):
        mark = input("Mark of " + students[i]["name"] + " is: ")
        marks[len(marks) - 1][course].update({students[i]["name"]: validatedMark(mark)})

def showCourses():
    print("Courses \n" + str(courses))

def showStudents():
    print("Student \n"+ str(students))

def showSpecificCourseMarks(course):
    print("The mark of this course is: ")
    for i in range(len(marks)):
        markKeys = marks[i].keys()
        if course in markKeys:
            print(marks[i])

def validatedMark(mark):
    try:
        check = float(mark)
        return check
    except ValueError:
        mark = input("Please re enter the mark")
        validatedMark(mark)


def validateCourse(input):
    for course in courses:
        if input == course["name"]:
            return True
    return False

def run():
    num = stdNum()
    for i in range(num):
        print("Student " + str(i + 1) + " info: ")
        std = stdInfo()
        students.append(std)
    num = courseNum()
    for i in range(num):
        print("Course " + str(i + 1) + " info: ")
        course = courseInfo()
        courses.append(course)
    enter = input("Do you want to enter the marks for any registered coures ? yes / no")
    while(enter == "yes"):
        inputCourse = input("The course you want to enter the marks is: ")
        if(validateCourse(inputCourse)):
            insertCourseMark(inputCourse)
            enter = input("Do you want to enter the mark of other course ? yes / no")
        else:
            print("This course does not exist")
            print("Do you want to re enter the name ?")
            enter = input()
    show = input("Do you want to see the student list and course list ? yes / no")
    if (show == "yes"):
        showCourses()
        showStudents()
        specificCourse = input("Enter the course you want to see the mark \n ")
        if (validateCourse(specificCourse)):
            showSpecificCourseMarks(specificCourse)
        else:
            print("You enter a wrong course !!!!")
run() 

