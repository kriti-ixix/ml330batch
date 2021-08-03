class Student:
    def __init__(self, n, r):
        self.name = n
        self.rollno = r
        #subject = "Python"
        #self.name = subject + ": " + self.name

    def greetingStudent(self):
        print("Hi ", self.name)

class Teacher:
    def __init__(self):
        self.name = "Ma'am/Sir"
        self.salary = 0

class Exams(Student):
    def __init__(self, n, r):
        Student.__init__(self, n, r)
        self.subject = "Subject"
        self.marks = 0

'''
student1 = Student()
#print(student1.name)
student1.name = 'Garima'
student1.rollno = 4
student1.greetingStudent()
#print("\nAfter changing:")
#print(student1.name)
#print(student1.rollno)

student2 = Student()
student2.name = 'Deepanshu'
student2.rollno = 1000
student2.greetingStudent()
#print("\nDeepanshu:")
#print(student2.name)
#print(student2.rollno)

teacher1 = Teacher()
print(teacher1)
'''

print("")
#Inheritance
exams1 = Exams("Kriti", 45)
print(exams1.name, exams1.rollno)
print("")
exams2 = Exams("Naveen", 100)
print(exams2.name, exams2.rollno)
print("")
