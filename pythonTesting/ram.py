#Write python program to greet user as "Hi, Good Morning", "Have a nice day".
name = input("What is your name?")

print("Hi", name, "," "Good Morning", "," "Have a nice day")

a = "Python Programming"
b = 2022
c = 1.05
d = 1 + 2j
e = True

print(type(a) , type(b), type(c), type(d) , type(e))

#How to concate values in print statement in runtime?

var1 = 4

var2 = "Test"

print(var1,"is concatinated with",var2)
print("{} {}".format("value of var1 is", var1))

#List
list1 = [1, 2, 3, "a", "b", 1.234, 1+2j, True]
# print 1 and a

print(list1[0],list1[3])

#print last value

print(list1[-1])

#print from 3 to 1+2j

print(list1[2:7])

#Add 'Sacumen' into list

list1.append("Sacumen")
print(list1)

#Delete 'a' from list
del list1[3]
print(list1)
#Delete list
del list1[:]
print(list1)

#Tuple

values1 = (2022, "a", 2.13, 1+2j, False)
#Delete tuple
#del (values1[0])

# Got error while saving the Tuple
#TypeError: 'tuple' object doesn't support item deletion
print(values1)

#Dictionary

dic = {"name": "Ram", "job": "QA", "company": "Sacumen", "location" : "Bengaluru"}

print(dic)

#print name
print(dic["name"])

# Update location
dic["location"] = "Chennai"
print(dic["location"])

#add new field as experience

dic["experience"] = "9 years"

print(dic)

#delete location

del dic["location"]
print(dic)

#delete dictionary

dic.clear()
print(dic)
