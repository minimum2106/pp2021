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
        if not (self.__validate_name(name)):
            print("Name is not valid")
            return
        if not (self.__validate_dob(dob)):
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

        if denominator == 0:
            return -1

        return numerator / denominator

    # @staticmethod
    # def repOk(name, dob):
    #     if (__validateName(name) and __validateDoB(dob)):
    #         return True
    #     return False
