#1. How to open and close file? Also give the Syntax for same.

#We can read the file in 2 ways !

#a.
file = open('Ram.txt')

file.close()

#b.

with open('Ram.txt') as reader:
    pass

#2. Write a Python program to read an entire text file.

text = open('Ram.txt')

print(text.read())

text.close()

print ("------------------------------------------------------------------")

#3. What is the difference between read() and readline()?

#Ans : read() will read the entire file,  readline() will read only the next line

#4. Write a Python program to read a file line by line and store it into a list.

with open('Ram.txt') as file1:
    for list in file1.readlines():
        print(list)


print ("------------------------------------------------------------------")


#5. Write a Python program to write text into file and print it.


with open('Ram.txt','a+') as file2:
    file2.write("\n")
    file2.write("Sacumen")
    for list1 in file2.readlines():
        print(list1)
print ("------------------------------------------------------------------")
#Note : Here used "a+" instead of "w" intentially, because if I use "w" it clears the existing content first and then writing the new text

#"a+" denotes for append mode (both read and write)

#Here I'm facing the issue, My existing texts are "QA Test Udemy", I'm adding "Sacumen" in line 42. But when I print on Line 44, "Sacumen" is not printed.
#when I run for the second time, I can see the sacumen prints for line 19.
#Not sure whether I'm missing anything or its a python issue

#Issue: Written content on the file is not printing the same run !

#6. Explain Exception handling in Python with example.

#Ans : When the known issues occurs during the run-time, as a Automation developer, We are handing the exceptions by catching it instead of stopping the execution

#Example :

name = "Ramkumar"

if name == "Ramkumar":
    print("Hi,", name)

else:
    raise Exception ("Hey who is this !")


#Output will be

#Traceback (most recent call last):
 # File "/home/sacumen/PycharmProjects/pythonTesting/ramAssignment4.py", line 68, in <module>
  #  raise Exception ("Hey who is this !")
#Exception: Hey who is this !

#Note : Change the value of the name, to see the exception in the output console

#7. What are raise and assert keywords in python? wth examples

# Ans :
# Raise : As explained in the 6th question, raise is used to shout out the error by raising the exceptions. W
# We can print the user-defined texts.
#Refer, 6th question for example of raise

# Asserts : Asserts are used to validate whether the condition is met or not.
# It will stop the program if the validation fails with the error " AssertionError"

#Example of Assertion error"

x = 10

assert x > 5


#Output:

#Traceback (most recent call last):
 # File "/home/sacumen/PycharmProjects/pythonTesting/ramAssignment4.py", line 94, in <module>
  #  assert x < 5
#AssertionError

#Note : Comment the 6th question code and change the assert condition to x<5 to check the assertion error in the console

#8. Explain try, catch and finally keys in Excepton handling.

#Ans :
# Try Block : Here we are testing our code, if the test fails, we are catching the errors in the "except" block

#Finally Block : It will executes irrespective whether try executes without error or any error catched on except block.

#Finally is Independent body

#Example of try block :

#Example 1 :

try:
    print(y)

except:
    print("Dude the varible is not declared at all")  # Here printing the customised error instead of actual error from try block

print ("------------------------------------------------------------------")
#Example 2 :

try:
    print(y)

except Exception as e:
    print(e)   # Here printing the actual error from try block
print ("------------------------------------------------------------------")

#Example 3:

try:
    print(y)

except Exception as e:
    print(e)   # Here printing the actual error from try block


finally:
    print("I dont mind your errors, because i'm finally block")

print ("------------------------------------------------------------------")

#9. What is the difference between Syntax Error and Exceptions.

#Syntax Errors : When the proper syntax of the language is not followed then a syntax error is thrown.

#We cannot run the program with Syntax errors.

#Example , without a semi-colon in the looping condition, indentation issues in coding are syntax errors

#File "/home/sacumen/PycharmProjects/pythonTesting/ramAssignment4.py", line 146
 #   finally:
  #  ^
#SyntaxError: invalid syntax


#Exceptions: It will happen during the execution of the code

#Example : When we are trying to read the text of an element which is not present in the page




#10. Write a python program to handle ZeroDivisionError exception.

a = 0
b = 0
try:
    c = a/ b
except ZeroDivisionError:
    c = 0

print("The value of c is : ",c)

print ("------------------------------------------------------------------")


print("Assignment 4 is completed !")