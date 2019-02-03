# # Read Amanzi *.rst files, extract header hierarchy

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

# marker library
xml = ".. code-block:: xml"   # xml
header0 = "=="                # major heading
header1 = "__"                # minor heading

# designate source file
file_source="short.rst"

## ## read source file
print ( "reading file %s" % file_source )
# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
with open( file_source ) as f:
    myLines = f.read().splitlines()  # remove \n

    numLines = len( myLines )
    print ( "%s lines found" % numLines )

## ## parse source file: pass 1
lines_xml = list( )      # container
lines_header0 = list( )  # container
lines_header1 = list( )  # container
countLines = 0
for line in myLines:
    countLines += 1
    print ( "Line {}: {}".format( countLines, line ) )
    # xml blocks
    if line.find( xml ) != -1:
        print( "xml found in line %s" % countLines )
        lines_xml.append( countLines )
    # header 0 blocks
    if line.find( header0 ) != -1:
        print( "possible header 0 in line %s" % countLines )
        lines_header0.append( countLines )
    # header 1 blocks
    if line.find( header1 ) != -1:
        print( "possible header 1 in line %s" % countLines )
        lines_header1.append( countLines )

print ( "{} xml blocks found; locations {}".format( len( lines_xml ), lines_xml ) )
print ( "{} header0 candidates found; locations {}".format( len( lines_header0 ), lines_header0 ) )
print ( "{} header1 candidates found; locations {}".format( len( lines_header1 ), lines_header1 ) )
