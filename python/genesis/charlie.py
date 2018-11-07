# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667-0817

# designate source file
file_source="short.rst"

## ## read source file
print ( "reading file %s" % file_source )
# https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
with open( file_source ) as f:
    content = f.read().splitlines()

print ( "parsing file %s" % file_source )
numLines = len( content )
print ( "%s lines found" % numLines )
