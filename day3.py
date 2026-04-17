'''
-->Operator
1.Arithmetic Operator
2.Assignment Operator
3.COmparision Operator
4.Logical Operator
5.Identity Operator
6.Membership Operator
7.Bitwise Operator
'''
'''
-->1.Arithmetic Operator:
--> +,-,*,%,**(power),//(floor division which gives the perfect value)
'''
num = 45
num_2 = 67  #o/p:201
num_3 = 89
print(num+num_2+num_3)

Num = 56
_2Num = 8  #o/p: 48
print(Num - _2Num)

X=8
Y=2  #o/p:0
print(X%Y)

digi_ = 9
digi_2 = 3 #o/p:27
print(digi_ * digi_2 )

a = 4
b = 4
print(4 ** 4)

_num1 = 10.27
_num2 = 3.7 #o/p:2.0
print(_num1 // _num2)

'''
-->2.Assignment Operator:
-->=,+=,-=,*=,**=,//=
--> to asssign the datatype to the variable'''

num =45
num_2 =56
print(num + num_2)

number =9
number +=1 #o/p:10
print(number)

number =10
number = number+6  #o/p : 16
print(number)

value = 26
value = value-6  #o/p:20
print(value)

numb = 9
numb *= 4  #o/p:36 (for ** o/p:6561)
print(numb)

'''
-->3.COmparision Operator:
--> ==, != , > ,< >= , <=
'''
a =9
b=6 # o/p : False
print(a==b)

a = 9
b=6 #o/p:True
print(a != b)

a = 7
b = 6 #o/p:false
print(a < b)

b = 8
a = 5 #o/p:true
print(b>a)

c = 78
d = 65   #o/p: true
print(c >= d)

g = 7
h = 10  #o/p:false
print(h <= g)

'''
-->4.Logical Operator:
->and : the 2 conditions should be true
->or : any one condition is satisfied the will be true
->not : it is used to reverse the output
'''
A = 5
B = 7  #o/p:true
print( A <10 and B < 10)

T  =7
H = 9  #o/p:true
print(T < 10 or H > 10)

A = 5
B = 7  #o/p:false
print( not(A <10 and B < 10))


'''
-->5.Identity Operator:
-->is  : this operator is used to check the object
--> is not :this operator is used to check the object not same'''
y =5
k =7
print(type(y  is k))

list_ =[1,2]
list_2=[1,2]
list_3 =list_
print(id(list_ is list_3))

list_ =[1,2]
list_2=[1,2]
print(list_ is list_2)
print(list_ == list_2) #note:

list_ =[1,2]
list_2=[1,2]
print(list_ is not list_2)


'''
-->6.Membership Operator:in, not in
--> in is used to check ,it is present init
-->not  is used to check,it is not there then also it shows that it present
'''
list_ =[1,2]
print(5 not in list_)
''''
-->7.Bitwise Operator: &,|,^,~,<<,>>
-->& bitwise AND
5-->0101
3-->0011
------
1-->0001
'''
print(5&3)
'''
-->^ Bitwise XOR
5-->0101
3-->0011
--------
6-->0110'''
print(5^3)
'''
-->| Bitwise OR
5-->0101
3-->0011
--------
7-->0111'''
print(5|3)

































