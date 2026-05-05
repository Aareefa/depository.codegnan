#
'''num = int(input("enter number:"))
for i in range(num,0,-1):
        print("*",end="")
    print()'''
#
'''num = int(input("enter number:"))
for i in range(num):
    for j in range(num-i-1,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()'''
#
num_ =int(input("enter the first number:"))
num_2 =int(input("enter the second number:"))
choice_ = int(input("\n1.add \n2.sub"))
if choice_ ==1:
    print(num_ +num_2)
elif choice_ ==2:
    print(num_ -num_2)
