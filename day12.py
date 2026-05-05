'''so = eval(input("enter items of lsit:"))
empty =[]
for i in so:
    if i not in empty:
        empty.append(i)
print(empty)


num =[10,20,30,40,50]
max1 =0
max2 =0
for i in num:
    if i >max1:
        max2 =max1
        max1 = i
print(max2)'''

nums = [10, 2, 20, 76,  4, 45,  99, 98]
max_1 = 0
max_2 = 0

for num in nums:
    if num > max_1:
        max_2 = max_1
        max_1 = num
print(f"{max_2} is the number in th elist {nums}")

num = int(input("enter a nuber:"))
if num>1:
    for i in range(2,int(num**2)+1):
        if num%1 ==0:
            print(num,"it is not a prime number")
            break
    else:
        print(num,"it is not a prime number")
else:
    print(num,"it is a not a prime")
             
        
