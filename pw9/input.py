import tkinter as tk


def std_num(window):
    frame = tk.Frame(window)
    frame.pack()
    str_var = tk.StringVar()
    label = tk.Label(frame, text="Number of students")
    label.pack()
    input_num = tk.Entry(frame,  textvariable=str_var)
    input_num.pack()
    return str_var.get()


def course_num(window):
    frame = tk.Frame(window)
    frame.pack()
    str_var = tk.StringVar()
    label = tk.Label(frame, text="Number of courses")
    label.pack()
    input_num = tk.Entry(frame, textvariable=str_var)
    input_num.pack()
    return str_var.get()
