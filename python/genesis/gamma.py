# https://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python
from pathlib import Path
# txt = Path( "AmanziInputSpec-v2.3.2-draft.rst" ).read_text()
file_source="short.rst"
txt = Path( file_source ).read_text()

print ( "%s" % txt )

numLines = txt.count( "\n" )

print ( "reading file %s" % file_source )
print ( "%s lines found" % numLines )
