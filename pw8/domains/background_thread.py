import threading
import pickle


class BackgroundThread(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path

    def add_objects(self, students, courses):
        file = open(self.path, 'wb')
        pickle.dump(students, file)
        pickle.dump(courses, file)
        file.close()
