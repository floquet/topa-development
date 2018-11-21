# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import os           # file name
import sys          # python version

class Employee:
    def __init__( self, first, last, pay ):
        self.first = first  # Daniel
        self.last  = last   # Topa
        self.pay   = pay    # 10000
        self.email = first + "." + last + "@abc.com" # Daniel.Topa@abc.com

emp_1 = Employee( "Daniel", "Topa", 10000 )
emp_2 = Employee( "Charles-Louis", "Montesquieu", 10000 )

print( "emp_1.email: ", emp_1.email )
print( "emp_2.email: ", emp_2.email )

print( "who am I?: ", emp_1.first, emp_1.last )


print( "\npython version:" )
print( sys.version )

print( "\nsource file", os.path.basename( __file__ ) )

dir_path = os.path.dirname(os.path.realpath( __file__ ) )
print( "directory", dir_path )

print( datetime.datetime.now( ) )

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
