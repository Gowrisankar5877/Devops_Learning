class Person:
    def __init__(self, fname="Raj", lname="Sankar",age=10):
        self.firstname = fname
        self.secondname = lname
        self.age = age
        self.skills=[]
    def print(self):
        print(f'{self.age},{self.firstname},{self.secondname},{self.skills}' )
    def skills_(self):
        n = int(input("Enter the number of skills you want to enter"))
        for i in range(n):
            skill = input("Enter the skill you posess")
            self.skills.append(skill)
class Student(Person):
    def __init__(self, fname="Raj", lname="Sankar", age=10,section="B"):
        super().__init__(fname, lname, age)
        self.section = section
    def print(self):
        print("Calling from Student class")
s1 = Student()
s1.skills_()
s1.print()
print(s1.skills)