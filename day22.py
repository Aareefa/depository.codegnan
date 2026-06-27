'''
Inheritance
-----------
->Inheriting the methods from the base to child
ex:
class parent:
    pass
class child(parent):
    pass

single inheritance
-----------------
->a child class inherits from one base class
ex:
class animal:
    def sound(self):
        print("Animals make sounds")
        
class dog(animal):
    def bark(self):
        print("Dog Barks")

D = dog()
D.sound()
D.bark()

(or)
class fruits:
    def types(self):
        print("This is the fruit")

class fruit(fruits):
    def mango(self):
        print("orange,guava")

A = fruit()
A.types()
A.mango()

Multiple inheritance
--------------------
->A child class inheritance more than one class is called 
ex:
class Father:
    def skill_1(self):
        print("Driving")

class Mother:
    def skill_2(self):
        print("Cooking")

class child(Father,Mother):
    def All_skills(self):
        print("Coding")

c =child()
c.skill_1()
c.skill_2()
c.All_skills()

Multi-level inheritance
----------------------
->inheritance from another child class
ex:
class grandfather:
    def house(self):
        print("Grandfather's house")
class father(grandfather):
    def land(self):
        print("Father's land")
class son(father):
    def flat(self):
        print("son's flat")
s =son()
s.house()
s.land()
s.flat()

Hierarchical inheritance
-----------------------
->Multiple child class inherits from one base class
ex:
class father:
    def property(self):
        print("Fther property")
class child_1(father):
    def car(self):
        print("first child car")
class child_2(father):
    def house(self):
        print("second child house")
c1 = child_1()
c2 = child_2()

c1.property()
c1.car()

c2.property()
c2.house()

Hybrid inheritance
------------------
->
ex:
class A:
    def methodA(self):
        print("class A")
class B(A):
    def methodB(self):
        print("class B")
class C(A):
    def methodC(self):
        print("class C")
class D(B,C):
    def methodD(self):
     print("class D")
any = D()
any.methodA()
any.methodB()
any.methodC()
any.methodD()

super() method
-------------
->Asuper method is used to call methods or constructor from the parent class
'''
class parent:
    def __init__(self):
        print("parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
        
c =child()

































































        
