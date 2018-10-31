# https://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python

from pathlib import Path
txt = Path( "AmanziInputSpec-v2.3.2-draft.rst" ).read_text()

print ( "%s" % txt )
