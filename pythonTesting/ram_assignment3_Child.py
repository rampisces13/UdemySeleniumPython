from ram_assignment3 import Company


class Person(Company):

  def __init__(self):

    Company.__init__(self, "Sacumen")

  def PersonInfo(self, name):
      self.firstname = name
      print("I'm executing from the child class")
      print("The Person name is :", self.firstname)


obj1 = Person()

obj1.PersonInfo("Ram")
obj1.printCompanyName()

print ("------------------------------------------------------------------")

