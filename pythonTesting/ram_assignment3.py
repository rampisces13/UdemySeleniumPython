#1. Explain class and objects in Python with basic example.

class Student: # Classes are user-defined Prototype or Blueprint . If we are devloping a mobile app, we should define like what operations this mobile app will do.
    age = 12
    gender = 'Male'

    def __init__(self):
        print("The constructor method is getting executed first")


    def greetMe(self):
        print('Hi , Ramkumar')


# Output of the class/global variables
print(Student.age)
print(Student.gender)

# Output of the method inside the class
obj = Student()
# An object is also called an instance of a class and the process of creating this object is called instantiation.
# To access the properties of the class (variables, methods of the class) outside from the class, we need to create an obj to the class.
obj.greetMe()
print ("------------------------------------------------------------------")
#2. Explain constructor in python with example.
#Constructor is a method , it will be called automatically when we create an object to the class
#When the constructor is not created , when we create an object to the class, constructor code will run automatically
#__init__ is the keyword to create a constructor for any classes
#To show the example, created constructor method to run automatically when the object is created to the class


#3. What is self keyword? why we use it python programming.

#To receive the values to the instance variables, self key word is used
# When the method of the class is beign called by passing the parameters, those paramters will be initiated using self key word in the constructors


class Student1:
    section = "A"

    def __init__(self, name): #Paramaterised constructor
        self.firstName = name

    def studentName(self):
        print("The student", self.firstName, "is deployed in the section:" , self.section)

#note: We could see, even though we assigned the received value to the instance variable in the constructor,
#We are calling those varaibles(either instance/global variable) using self keyword only. so using of self keyword is madatory to call the variables


obj1 = Student1("Ramkumar S ")

obj1.studentName()

print ("------------------------------------------------------------------")
#4.Write a python program using class and object to perform addition, subtraction and multiplication of two numbers.

class Calculator:

    def __init__(self, a , b):
        self.firstNumber = a
        self.secondNumber = b

    def Addition(self):
        return self.firstNumber + self.secondNumber


    def Sub(self):
        return self.firstNumber - self.secondNumber


    def Mul(self):
        return self.firstNumber * self.secondNumber


obj3 = Calculator(5, 10)

print(obj3.Addition())
print ("------------------------------------------------------------------")
print(obj3.Sub())
print ("------------------------------------------------------------------")
print(obj3.Mul())
print ("------------------------------------------------------------------")


#5.What is inheritance? explain with basic example.

#In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class.
# A child class can also provide its specific implementation to the functions of the parent class.

class childCalc(Calculator): #Here while creating the class, we passed other class "Calculator" as parameter to the class which denotes it is the parent of the "childCalc"

    def __init__(self):
        Calculator.__init__(self, 63, 9) #The parent class contructor is expecting the value, so in the child class contructor we called the parent class's contructor

    def Divide(self):
        return self.firstNumber / self.secondNumber


obj4 = childCalc()
print(obj4.Divide())
print ("------------------------------------------------------------------")

#6. Write a python program to demonstrate inheritance, points to cover in code,
     # a Create parent class and declare method
     # b. Create child class and use parent method


class Company:

    def __init__(self, companyname):
        self.companyname = companyname


    def printCompanyName(self):
        print("The Company name is : " + self.companyname)


#7.What is string in python?

#A string is a sequence of characters.

my_string = "Hello"
print(my_string)

print ("------------------------------------------------------------------")

#8.Declare variable with 'Quality Engineer at Sacumen',
   # 1.Check datatype of the declared variable

newstr = 'Quality Engineer at Sacumen'

print(newstr)
print ("------------------------------------------------------------------")
# 2.Print each charaters in variable
print(type(newstr))
# 3.Add ', Bangalore' into  variable

newstr1 = 'Bangalore'

newstr = newstr + ' ' + newstr1

print(newstr)

print ("------------------------------------------------------------------")
# 4. Split varible  by  space

newstr2 = newstr.split(' ')
print(newstr2)

print ("------------------------------------------------------------------")

# 5. Trim ',' from variable

newstr3 = "  Sachin "

print(newstr3.strip()) #trim at start and end
print ("------------------------------------------------------------------")
print(newstr3.lstrip()) #trim at start
print ("------------------------------------------------------------------")
print(newstr3.rstrip()) #trim at end
print ("------------------------------------------------------------------")

# 6. Replace 'Quality' with 'Automation'

newstr2[0] = "Automation"

print(newstr2)

print ("------------------------------------------------------------------")

print("Assignment 3 is completed !")