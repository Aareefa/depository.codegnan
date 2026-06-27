'''
Error Handling
--------------
1.try
---
->The try bolck , that will test a block of code for errors
eg:

try:
   print(num)

2.except
--------
->This block will handle the error, which are written in the try block
eg:

try:
    print(num) #this is NameError
    print("python.exe" + 9)   #This handles TypeError
except NameError:
    print("it is handling NameError")
except TypeError:
    print("handling TypeError")

else:
----
->The else keyword to define a block of code to be executed if no error were raised
eg:

try:
    print("hi")
except:
    print("it is handling some error")
else:
    print("no error")

Finally
-------
->The finally block will execute either try block raise an error or not

'''
try:
    print("hi ")
except NameError:
    print("It is handling NameError")
else:
    print("no error")
finally:
    print("bye bye")
