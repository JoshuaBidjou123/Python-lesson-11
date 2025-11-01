# parent class
class person ( object ):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(person):
     def __init__(self, name, idnumber, salary, post):
         self.salary = salary
         self.post = post

         # invoking the __init__ of the parent class
         person.__init__(self, name, idnumber) 

# creation of an object variable or instance
a = Employee('John', 20210401, 1500, "Calculator")

# calling the function of the class Person using its instance
a.display()