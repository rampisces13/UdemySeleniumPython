#1.Explain Conditional Statements in python with simple examples.

#If, Else, Nested - IF's are the conditional statements in python

#Example:

a = "Ram"
if (a =="Ram1"):
    print("Hi")
else:
    print("Sorry")

print("--------------------------------------------")

#2.Take two inputs as interger from user and print greatest among them.

b = input("Enter first values: ")
c = input("Enter second values: ")
if (b > c):
    print("The first input", b, "is greater than second input", c)
else:
    print("The second input", c, "is greater than first input", b)

print("--------------------------------------------")
#Note If value b is 5 and c is 10, it is executing wrongly

#3.A school has following rules for grading system:  a. Below 35 - C b. 35 to 59 - B  c. 60 to 85 - A  d. Above 85 - A+
# Ask user to enter marks and print the corresponding grade.

d = input("Enter your marks: ")

if(d<"35"):
    print("Hey, your grade is C")

elif (d >= "35" and d <= "59"):
    print("Hey, your grade is B")

elif (d >= "60" and d <= "85"):
    print("Hey, your grade is A")

elif (d >"85" and d <= "99"):
    print("Hey, your grade is A+")
else:
    print("Please enter correct marks")

print("--------------------------------------------")
#Note If value is d= 100,  it is executing wrongly

#4.Example range functon in python with example.

# Generate numbers between 0 to 10
for i in range(10):
    print(i)

print("--------------------------------------------")
#5.Declare list with 1,2,3,4,5 and print each values.
valList = [1, 2, 3, 4, 5]
for j in valList:
    print(j)
print("--------------------------------------------")

#6.Declare list with integers values and print sum of all integers.

intList = [10, 20, 30, 40, 50]
addList = 0
for k in intList:
    addList = addList + k

print(addList)

print("--------------------------------------------")

#7.Declare list with QA, 2, 7, Engineer, True, 3.19, At, Sacumen. Check string values in the list and add it into new list then print it.

newList = ["QA", 2, "Engineer", True, 3.19, "At" , "Sacumen"]

newSubList = []

for l in newList:
    if(type(l) == str):
        newSubList.append(l)

print(newSubList)

print("--------------------------------------------")


#8.Calculate the sum of all numbers from 1 to 10 using while loop

num = 10

sum1 = 0

while(num>0):
    sum1 = sum1+num
    num = num - 1

print(sum1)

print("--------------------------------------------")

#9.Print even numbers from 1 to 10 using while loop

numEven = 10
while(numEven>0):
    if ((numEven % 2) == 0):
        print(numEven)
        numEven = numEven - 1
    else:
        numEven = numEven - 1

print("--------------------------------------------")



#10.Explain break and continue keywords in python with example.

breakList = ["Ram","Thribhuvana", "Manohar" , "Sushma"]

for m in breakList:
    print(m)
    if(m=="Ram"):
        print(m)
        print("I will continue the loop")
        continue
    if(m=="Manohar"):
        print(m)
        print("I'm going to break the loop")
        break

print("--------------------------------------------")


#11.Create a functions to adding and subtraction of two integer numbers.

def AddIntegers(p,q):
    print("Addition of the two values are :", p+q)

def SubIntegers(p,q):
    print("Subtraction of the two values are :", p - q)

AddIntegers(5, 10)

SubIntegers(5, 10)

print("--------------------------------------------")

#12 Exaplain return keyword in python with example.


def multiply(x, y):
    return x*y

z = multiply(5 , 10)
print ("Multiplication of the two values are :", z)

print("--------------------------------------------")

print("Assignment 2 is completed !")