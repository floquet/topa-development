#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # File parsing tools
# xl_new_workbook( workbook_title )

# # imports

def reader( file_source ):
    ## ## read source file
    print ( "reading file %s" % file_source )
    # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
    with open( file_source ) as f:
        myLines = f.read().splitlines()  # remove \n

        numLines = len( myLines )
        print ( "%s lines found" % numLines )
    return ( numLines, myLines );

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #
