# https://stackoverflow.com/questions/1252163/printing-python-version-in-output
import platform  # python_version
import sys       # version_info

print( platform.python_version( ) )

print( "The Python version is %s.%s.%s" % sys.version_info[:3] )

print( "python version:" )
print( sys.version )
