# parent is the base class
# child is the derived class
 
# eg

# create a class named person, with firstname and last name properties and print name method.
 
class person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(self.firstname, self.lastname)
        # print(f"name: {self.firstname} {self.lastname}")
x = person("john", "doe")
x.print_name()

# create a class named student which will inherit the properties and methods from the person class
class student(person):
    # we have added the innit function and kept the inheritance of the parent class to add the functionality of init use the super() function
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.firstname = firstname
        self.lastname = lastname
        self.graduationyear = year
        # person.__init__(self, firstname, lastname)

def hi(self):
  print("hi", self.firstname, self.lastname, "your graduation year is ", self.graduationyear)
y = student("mike", "tyson", 2025)
y.print_name()
# print(y.graduationyear)

# add init function to the inheritence class 
