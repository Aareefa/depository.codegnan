'''
a =int(input("enter the number"))
print(a)

passing two values
------------------
a,b = map(int,input("enter to numbers: ").split())
print(a)                                      #o/p:enter to numbers: 67
print(type(a))

SBI_PIN = input("pls enter 4 digit pin here:")
if len(SBI_PIN) == 4:
    print("welcome to sbi atm")
int data type:

any = int(input("enter the number:"))
print(type(any))

string data type:

any = input("enter the word:")
print(type(any))

List data type
--------------
cv = list(map(int,input("enter the number:").split())) #o/p:enter the number:67 89 78
print(cv)
print(type(cv))                                       #[67, 89, 78]

tuple data type
----------------
an = tuple(map(int,input("enter the numberr:").split()))
print(an)
print(type(an))

a =89
b =7
print("Adding a and b and the result is",a+b)
print(f"Adding a and b and the result is {a+b}")
print(f"{a}+{b} ={a+b}")

if statement
------------
->This is used to check condition is  true or not
ex:
an =9
if an==9:
    print(f"an is equal to {9}")
    
else statement
--------------
->else is fall-back statement ,incase if statement becomes false,it will enter into elsse
ex:
an =9
if an>9:
    print(f"an is greater then {9}")
else:
    print(f"an is not greater the {9}")

a =6
b=7
if a>= b:
    print(f"{a}give the greater value{b}")
else:
    print(f"{a} is lesser {b}")

eval
-----
v= eval(input("enter:"))
print(type(v))
print(v)

age =int(input("enter your age:"))
if age>=18:
    print("you are eligible for the voting ")
else:
    print(f"you have to wait {18-age} more years")
'''

marks =int(input("enter your marks:"))
if marks<35:
    print("your failed")
else:
    print("your pass")


































