# https://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python

with open( "AmanziInputSpec-v2.3.2-draft.rst", "r" ) as file_rst:
  data = file_rst.read()

print ( "%s" % data )
