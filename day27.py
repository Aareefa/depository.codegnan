'''
regx or regular expression is a sequence of character that forms a searching pattern
->To use this regx have to import module(package) called re
syntax->import re

functtions
--------
findall()
search()

eg
import re
s="python is a language"
a=re.search("[a]",s)
print(a)

Metachaaracters
---------------
1[]-->A-Z,a-z,[ahg]
eg:
import re
some ="Python is a language"
any = re.findall("[a-z]",some)
print(any)

2 .-->it will take any character but one dot is one character
eg:
import re
some ="Python is a language"
any = re.findall("P..h..",some)
print(any)

3 ^->checks the string with starting  with or not
eg:
import re
some ="Python is a language"
any = re.findall("^P",some)
print(any)

4 $->
eg:
import re
some ="Python is a language"
any = re.findall("language$",some)
print(any)

4 *->zero to n umber of characters
eg:
import re
some ="Python is a language"
any = re.findall("P.*",some)
print(any)

5 +->atleasst one or more characters
eg:
import re
some ="Python is a language"
any = re.findall("P.+n",some)
print(any)

6 {}->form the pattern based on the size mentioned in the {}
eg:
import re
some ="Python is a language"
any = re.findall("P.{10}",some)
print(any)




'''

import re
some ="Python is a language"
any = re.findall("P.{10}",some)
print(any)
