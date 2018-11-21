# https://stackoverflow.com/questions/1252163/printing-python-version-in-output
import platform  # python_version
import sys       # version_info

print( platform.python_version( ) )

print( "The Python version is %s.%s.%s" % sys.version_info[:3] )

print( "python version:" )
print( sys.version )

# dantopa@Lax-Millgram:develop $ date
# Tue Nov 20 21:05:21 MST 2018

# dantopa@Lax-Millgram:develop $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/develop

# dantopa@Lax-Millgram:develop $ py version.py
# 3.6.7
# The Python version is 3.6.7
# python version:
# 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
