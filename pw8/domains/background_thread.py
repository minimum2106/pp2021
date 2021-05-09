import threading
import pickle


class BackgroundThread(threading.Thread):
    def __init__(self, path, stdscr):
        threading.Thread.__init__(self)
        self.path = path
        self.__stdscr = stdscr

    def add_objects(self, students, courses):
        file = open(self.path, 'wb')
        pickle.dump(students, file)
        pickle.dump(courses, file)
        file.close()
        self.__stdscr.refresh()
