'''
while statement
--------------
->This while statement will keep on executing until unless condition becomes true
ex:
v=1
while v<=5:
      print(v)
      v+=1
Range()
------
->This range() will generate sequence numbers upto the limit
syntax--> range(starting,ending,step)
ex:;
choice_u = int(input("Enter the limit:"))
for j in range(100,choice_u,2):
    print(j)
break
-----
->This break statement will exit if the condition becomes true,and never enter into next loops
ex:
any =["aareefa","hanifa","puji","mouni","indrani"]   
for i in any:
    print(i)
    if i =="puji":
        break
continue
--------
->This statement will skip that particular itteration and goes to next itteratios
ex:
any =["aareefa","hanifa","puji","mouni","indrani"]   
for i in any:
    if i =="puji":
        continue
    print(i)
pass
----
->pass is space holder,holds the space not to get any  error
ex:
a =9
b =90
if a>=b:
   pass
nested loop
-----------
->A loop in side the loop is called nested loop
'''

for j in range(2,100):
    count =0
    for an in range(1,j+1):
        if j % an ==0:
            count +=1
    if count ==2:
        print(f"{j} is a prime")
    else:
        print(f"{j} is not a prime")





























