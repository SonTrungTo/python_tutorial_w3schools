from classes import Person

class Student(Person):
    def __init__(self, name, age, gradYear):
        super().__init__(name, age)
        self.gradYear = gradYear
    
    def welcome(self):
        print("Welcome " + self.name + ". I am " + str(self.age) + " years old and graduate at " + str(self.gradYear))

s1 = Student("Son", 30, 2016)
s1.welcome()
