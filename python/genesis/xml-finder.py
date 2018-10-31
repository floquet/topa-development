# find xml code blocks
input_file = open( "AmanziInputSpec-v2.3.2-draft.rst", "r" )
count_lines = 0

for line in input_file:
    count_lines += 1
    if line.find('.. code-block:: xml'):
        print('code block in line ',count_lines)
print ('number of lines: %s', count_lines)
