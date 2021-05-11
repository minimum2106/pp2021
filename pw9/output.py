import tkinter as tk


def show_course(courses, window):
    frame = tk.Frame(window)
    label = tk.Label(frame, text="- All courses that this class is currently taking: ")
    label.pack()
    for index, course in enumerate(courses):
        tk.Label(window, text=f"{course.get_id()} : {course.get_name()}").pack()


def show_students(students, window):
    frame = tk.Frame(window)
    label = tk.Label(frame, text="- Student of this class: ")
    label.pack()
    for index, student in enumerate(students):
        tk.Label(frame, text=f"{student.get_id()} : {student.get_name()}").pack()


def sort(students):
    for i in range(len(students) - 1):
        for j in range(len(students) - i - 1):
            if students[j].gpa() < students[j + 1].gpa():
                students[j], students[j + 1] = students[j + 1], students[j]


def show_gpa(students, window):
    std_desc = []

    frame = tk.Frame(window)
    label = tk.Label(frame, text="- Gpa of this class: ")
    label.pack()
    for student in students:
        std_desc.append(student)

    sort(std_desc)

    for idx, std in enumerate(std_desc):
        tk.Label(frame, text=f'   + {std.get_name()}: {std.gpa()}').pack()
