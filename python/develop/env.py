# https://stackoverflow.com/questions/4906977/how-do-i-access-environment-variables-from-python
import os

print( "$HOME     = ", os.environ['HOME'] )
print( "$USER     = ", os.environ['USER'] )
print( "$HOSTNAME = ", os.environ['HOSTNAME'] )

print( "\nall environment variables" )
print( os.environ )
