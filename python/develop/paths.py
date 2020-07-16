# https://stackoverflow.com/questions/8248397/how-to-know-change-current-directory-in-python-shell
import os           # probe, change directories
import sys          # python version
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

print( "file:     ", os.path.basename( __file__ ) )
print( "directory:", os.getcwd( ) )

print( "\njumping up one level")
os.chdir( '..' )

print( "os.getcwd():", os.getcwd( ) )

print( "jumping to /Users/dantopa/Documents/GitHub/topa-development")
os.system( "cd /Users/dantopa/Documents/GitHub/topa-development" ) # Windows only?
print( "os.getcwd():", os.getcwd( ) )
os.chdir( "/Users/dantopa/Documents/GitHub/topa-development" ) # bueno
print( "os.getcwd():", os.getcwd( ) )

print( "\npython version:" )
print( sys.version )

print( datetime.datetime.now( ) )

# dantopa@Lax-Millgram:develop $ py paths.py
# file:      paths.py
# directory: /Users/dantopa/Documents/GitHub/topa-development/python/develop
#
# jumping up one level
# os.getcwd(): /Users/dantopa/Documents/GitHub/topa-development/python
# jumping to /Users/dantopa/Documents/GitHub/topa-development
# os.getcwd(): /Users/dantopa/Documents/GitHub/topa-development/python
# os.getcwd(): /Users/dantopa/Documents/GitHub/topa-development
#
# python version:
# 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
# 2018-11-20 22:31:38.527072
