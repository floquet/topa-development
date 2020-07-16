# https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-notebook-name
# https://stackoverflow.com/questions/4152963/get-the-name-of-current-script-with-python
import os
import sys

#nb_full_path = os.path.join(os.getcwd(), nb_name)

print( "directory = ", os.path )
print( "using os:", os.path.basename( __file__ ) )
print( "using sys:", sys.argv[0] )

# dantopa@Lax-Millgram:develop $ date
# Tue Nov 20 21:34:31 MST 2018

# dantopa@Lax-Millgram:develop $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/develop

# dantopa@Lax-Millgram:develop $ python --version
# Python 3.6.7
# dantopa@Lax-Millgram:develop $ py nemo.py
# directory =  <module 'posixpath' from '/opt/local/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/posixpath.py'>
# using os: nemo.py
# using sys: nemo.py
