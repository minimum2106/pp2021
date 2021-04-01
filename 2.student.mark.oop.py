class Student:
    count = 0

    def __init__(self, name, DoB):
        if (not(__validateName(name))):
            print("Name is not valid")
            return
        if (not(__validateDoB(DoB))):
            print("DoB is not valid")
            return

        self.id = ++count
        self.DoB = DoB
        self.name = name

    def __validateName(self, name) :
        if (len(name) > 1 ):
            return True
        return False

    def __validateDoB(self, dob):
        if (len(dob) > 1):
            return True
        return False
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        if(__validateName(name)):
            self.name = name
            return 
        print("Name is not valid")
    
    def getId(self):
        return self.id
    
    def getDoB(self):
        return self.DoB

    def setDoB(self, dob):
        self.DoB = dob
    


class Course:
    count = 0
    
    def __init__(self, name):
        if(not(__validateName(name))):
            print("The name of the course is not valid")
            return 
        
        self.name = name
        self.id = ++count
            
    def __validateName(self, name):
        if(len(name) > 1):
            return True
        return False



# if __name__ == "__main__":
    



