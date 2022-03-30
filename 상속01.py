class Person:
    numofpeople=0
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        Person.numofpeople+=1
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    numofstudent=0
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
        Student.numofstudent+=1
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)
print(Person.numofpeople)
print(Student.numofstudent)

p.printInfo()
s.printInfo()
