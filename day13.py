'''
->Function
----------
->This is a block of code that can be reusable
->A function can only run when it is called
->def is the keyword is to define the function
syntax
-------
def func_name(parameters):
    ---------
    ---------
func_name(arguments)

ex:
num = 9
def even_odd(num):
    if num % 2 ==0:
        print(f"[num} is even numbers")
    else:
        print(f"{num} is odd number")
even_odd(num)
even_odd(120)


->Required Arguments
--------------------
->A function must called with correct number of arguments,that means if function excepts 2 arguments,
we have to call function with 2 arguments not less or not more

ex:
def even_odd(num,num_2):
    print(num+num_2)
even_odd(8,9)

       #(or)
def even_odd(num,num_2):   #this will throw an error 
    print(num+num_2)
even_odd(8,9,10)

->Default Arguments
-------------------
->By default, value is taken from the calling function

ex:
def even_odd(name="Aareefa"):
    print(f"hai {name}")
even_odd("hanifa")
even_odd("puji")
even_odd()

num = 9
def even_odd(num_1):
    print(num_1)
even_odd(num)

->Keyword Arguments
-------------------
->Here, we can send arguments with hey = value syntax.By this the order of arguments does not matter
ex:
def  even_odd(num_2,num_3,num):
    print(num+num_2+num_3)
even_odd(num=9,num_2=5,num_3=5)

->Variable length Argument
--------------------------
->Adding a atar(*) before the parameter name in the funtion,receive a tuple of arguments and can be access items with indexing

ex:

def  even_odd(*name):
    print(name[2])
even_odd("aareefa","puji","mouni","hanifa","indu")
'''


