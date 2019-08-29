class Person:
    
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def print (self):
        print(f'My name is {self.name} and I am {self.age}')

me = Person('maria',22)
me.print()