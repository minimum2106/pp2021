import math


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
        if not (self.__validate_name(name)):
            print("- The name of the course is not valid")
            return
        if not (self.__validate_credit(credit)):
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
            while not (self.__validate_mark(mark)):
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
