## Classes/Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def message(sender):
        print("Hello my name is", sender.name)

p1 = Person("Son", 30)
p1.message()
