# # Read Amanzi *.rst files, extract header hierarchy

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

# marker library
xml=".. code-block:: xml"   # xml
header0="=="                # major heading
header1="--"                # minor heading

# designate source file
file_source="short.rst"

## ## read source file
print ( "reading file %s" % file_source )
# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
with open( file_source ) as f:
    myLines = f.read().splitlines()  # remove \n

numLines = len( myLines )
print ( "%s lines found" % numLines )

# https://stackabuse.com/read-a-file-line-by-line-in-python/
with open( file_source ) as f:
   for cnt, line in enumerate( f ):
       print ( "Line {}: {}".format( cnt, line ) )

print ( "parsing file %s" % file_source )
# https://stackabuse.com/read-a-file-line-by-line-in-python/
# for line in myLines:
#     # mark xml blocks
#     # candidates, header 0
#     # candidates, header 1
#     countLines = 1
#     line = myLines[ countLines ]
#     while line:
#         print("Line {}: {}".format(countLines, line))
#         line = myLines[ countLines ]
#         countLines += 1
    #print ( "%s" % line )
