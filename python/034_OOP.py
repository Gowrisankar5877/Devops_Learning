class Person:
    def __init__(self, fname="Raj", lname="Sankar",age=10):
        self.firstname = fname
        self.secondname = lname
        self.age = age
        self.skills=[]
    def print(self):
        print(f'{self.age},{self.firstname},{self.secondname}' )
    def skills_(self):
        n = int(input("Enter the number of skills you want to enter"))
        for i in range(n):
            skill = input("Enter the skill you posess")
            self.skills.append(skill)

p = Person(age=22)
print(p)
print(p.age)
print(p.firstname)
p.print()
p.skills_()
print(p.skills)