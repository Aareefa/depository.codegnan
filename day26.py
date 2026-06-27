'''
File Handling
-------------
->File Handler is an object of a file to maintain several functions of file like creating, reading, updating
and deleting the files...

->two ways to open a file
-------------------------
1.open()
--------
Syntax -->file handler = open("filename.txt","mode")
          -------------------
          -------------------
          file handler.close()

eg:
---
any = open("demo.txt","r")
print(any.read())
any.close()

2.with open()
-------------
syntax->with(keyword)open("filename:,"mode")as file handler:
        ----------------------------
        ----------------------------
eg:
---
with open("demo.txt","r") as so:
    print(so.read())

With keyword
------------
->using this with keyword no need close the file in the lines, it will close the file autometically..

Modes
-----
r->used to file and through error if the file does not exist..

a->used to add the text at last, if the file does not exist it will create
eg:
with open("demo.txt","a") as so:
    print(so.write("\n hello" ))

w->used to add new text as override the txt in the file, if the file does not exist it will create
eg:
with open("demo.txt","w") as so:
    print(so.write("\n hello" ))
x->is used to create a file and through error if the file exist
eg:
with open("aaree.txt","x") as so:
    print(so.write("hello"))

read()
-----
->The read method can read the entire file chunk by chunk where we can specify size

eg:
--
with open("demo.txt","r")as so:
    print(so.read(4))

readline
--------
->this method can read one line at a time
eg:
--
with open("demo.txt","r")as so:
    print(so.readline())

note
----
->foe "w" mode and "a" mode we will use write() method
eg:
--
with open("demo.txt","w")as so:
    print(so.write("somthing"))ar
'''























