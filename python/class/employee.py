# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
import sys # python version

class Employee:
    pass

print( "python version:" )
print( sys.version )

emp_1 = Employee( )
emp_2 = Employee( )

print( emp_1 )
print( emp_2 )

emp_1.last  = "Topa"
emp_1.first = "Daniel"
emp_1.email = "private@gmail.com"
emp_1.phone = "505 667 0817"

print( "who am I?: ", emp_1.first, emp_1.last )

# dantopa@Lax-Millgram:class $ py employee.py
# python version:
# 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
# <__main__.Employee object at 0x10aed7550>
# <__main__.Employee object at 0x10aed75c0>
# who am I?:  Daniel Topa

# dantopa@Lax-Millgram:class $ date
# Tue Nov 20 22:05:40 MST 2018

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/class

# dantopa@Lax-Millgram:class $ python --version
# Python 3.6.7
