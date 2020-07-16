# https://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python
from pathlib import Path # 3.7 feature

# marker library
eol="\n"                    # end of line
xml=".. code-block:: xml"   # xml
header0="==\n"              # major heading
header1="--\n"              # minor heading

# txt = Path( "AmanziInputSpec-v2.3.2-draft.rst" ).read_text()
# designate source file
file_source="short.rst"

# gobble up the text
print ( "reading file %s" % file_source )
txt = Path( file_source ).read_text() # no open and close
# print ( "text found:\n %s" % txt )  # debug
print ( "%s characters in file\n" % len( txt ) ) # debug

print ( "parsing file %s...\n" % file_source )

# count lines of text
numLines = txt.count( eol )
print ( "%s lines found" % numLines )

# count xml blocks
numXml = txt.count( xml )
print ( "%s xml blocks found" % numXml )

numCandidataHeading0 = txt.count( xml )

# list of eol locations: defines lines
pos_eol = [ i for i, a in enumerate( txt ) if a == eol ]
print ( "eol positions: %s" % pos_eol )

print ( "characters 54:59 = %s" % txt[100:195] )
