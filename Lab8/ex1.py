class Person(): #คลาสบุคคล
    def __init__(self):
        # List of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'Name: {self.name} Age: {self.age} Gender: {self.gender}')

class Employee(): #คลาสพนักงาน
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.emp_id = ""
        self.position =""

    def info(self):
        print(f'Name: {self.name} '
        f'Age: {self.age}'
        f'Gender: {self.gender}'
        f'emp_id: {self.emp_id}'
        f'position:{self.position}')

class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.id = 0
        self.group = ""
        self.University =""

    def info(self):
        print(f'Name: {self.name} '
        f'Age: {self.age}'
        f'Gender: {self.gender}'
        f'id: {self.id}'
        f'group:{self.group}'
        f'University:{self.University}')

#ceate object
p1 = Person()
p1.name = "Nattakarn Phaewkasin"
p1.age = 21
p1.gender = "female"

emp1 = Employee()
emp1.name = "Peerapon Klang"
emp1.age = 22
emp1.gender = "Male"
emp1.emp_id = "EMPMT01"
emp1.position = "Lecturer"

s1 = Student
s1.name = "Nattakarn Phaewkasin"
s1.age = 21
s1.gender = "female"
s1.id = 364411760013
s1.group = "Information technology management"
s1.University = "RUTS"

p1.info()
emp1.info()
s1.info()

lst = [p1,emp1,s1]

for obj in lst:
    print(obj.__class__.__name__, end=" ")
    obj.info()




s1 = Student
s1.name = "Nattakarn Phaewkasin"
s1.age = 21
s1.gender = "female"
s1.id = 364411760013
s1.group = "Information technology management"
s1.University = "RUTS"

p1.info()
emp1.info()
s.info()

lst = [p1,emp1,s1]

for std in lst:
    print(std.__class__.__name__, end=" ")
    std.info()