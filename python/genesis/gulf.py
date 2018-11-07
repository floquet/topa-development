# # Read Amanzi *.rst files, extract header hierarchy

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

def main():

    myLines = reader( "short.rst" ) # read file as split lines
    ( loc_xml, loc_candidate_header0, loc_candidate_header1 ) = parse1( myLines )  # first parse: candidate headers
    parse2( myLines, loc_candidate_header0 )

## ## end of program unit main

def reader( file_source ):
    ## ## read source file
    print ( "reading file %s" % file_source )
    # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
    with open( file_source ) as f:
        myLines = f.read().splitlines()  # remove \n

        numLines = len( myLines )
        print ( "%s lines found" % numLines )
    return myLines;

## ## end of program unit reader

def parse1( myLines ):
    # marker library
    xml = ".. code-block:: xml"   # xml
    header0 = "=="                # major heading
    header1 = "__"                # minor heading

    ## ## parse source file: pass 1
    loc_xml = list()                # locations container
    loc_candidate_header0 = list()  # locations container
    loc_candidate_header1 = list()  # locations container

    numLines = 0
    for line in myLines:
        numLines += 1
        print ( "Line {}: {}".format( numLines, line ) )
        # xml blocks
        if line.find( xml ) != -1:
            print( "xml found in line %s" % numLines )
            loc_xml.append( numLines )
        # header 0 blocks ==========
        elif line.find( header0 ) != -1:
            if line.find( "+" ) != -1:
                continue
            print( "possible header 0 in line %s" % numLines )
            loc_candidate_header0.append( numLines )
        # header 1 blocks __________
        elif line.find( header1 ) != -1:
            print( "possible header 1 in line %s" % numLines )
            loc_candidate_header1.append( numLines )

    print ( "{} xml blocks found; locations {}".format( len( loc_xml ), loc_xml ) )
    print ( "{} header0 candidates found; locations {}".format( len( loc_candidate_header0 ), loc_candidate_header0 ) )
    print ( "{} header1 candidates found; locations {}".format( len( loc_candidate_header1 ), loc_candidate_header1 ) )

    return ( loc_xml, loc_candidate_header0, loc_candidate_header1 );

## ## end of program unit parse1

def parse2( myLines, loc_candidate_header0 ): # vet candidates
    loc_actual_header0 = list()  # location of header0
    txt_actual_header0 = list()  # text of header0
    for lineNum in loc_candidate_header0:
        lineLengthA = len( myLines[ lineNum - 1 ] )
        lineLengthB = len( myLines[ lineNum - 2 ] )
        if lineLengthA == lineLengthB:
            loc_actual_header0.append( lineNum - 2 )
            txt_actual_header0.append( myLines[ lineNum - 2 ] )
        print( "header0 found in line {}: {} ".format( lineNum - 2, myLines[ lineNum - 2 ] ) )
    return;

main()
