'''
elif stament
-----------
->This statement gives more options to get result of that program
ex:
marks=int(input("enter the marks:"))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("B")
elif marks>=50:
    print("C+")
else:
    print("Failed")

Nested if statement
-------------------
->if statement in side another if statement is  called Nested if statement
ex:
user_SBI_info ={"ATM PIN":"7869"}
user_pin = input("enter your ATM:")
if len(user_pin) == 4:
    if user_pin in user_SBI_info['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("plese enter the correct pin")
else:
    print("plese enter 4 digit pin:")

for statement
-------------
->A for statement used to iterate over items like (string,list,tuple) with fixed number of itterations
ex:
any =[23,45,6,78]
for j in any:
    print(j)
else statement in for
---------------------
->After Completing all iterations this else statement will excute
ex:
any =[23,45,6,78]
for j in any:
    print(j)
else:
    print("Loop Finished")

First Program

'''
so ="madam"
empty=''
for j in so:
    empty = j+empty
if empty == so:
    print("it is palindrome")
else:
    print("not a palindrome")
