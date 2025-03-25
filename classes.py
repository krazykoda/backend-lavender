class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # talk
    def speak(self):
        print(f"My name is ")

    def getAgeInFuture(self, number):
        print(self.age + number)


class Student:
    def __init__(self, name="", age=0, program=None, level="100", **kwargs):
        self.name = name
        self.age = age
        self.progam= program
        self.level= level
        for key, value in kwargs.items():
            setattr(self, key, value)

class Program:
    name= ""
    department=""


geography = Program()

enoch = Student(name="Enoch", age=12, level="200", program=geography, grade="70", hostel="Pent")
print(vars(enoch))
# enoch.program = geagraphy


person1 = Person("Sam", 12, "Male")
# print(person1.name)



person2 = Person("Mina", 18, "Female")
# print(person2.name)


