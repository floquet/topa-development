#! /usr/bin/python
# # Daniel Topa dantopa@lanl.gov 505 667 0817

# # Read Amanzi *.rst files, extract header hierarchy

# # imports
import os           # probe, change directories
import sys          # python version
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

# # globals
dingbat_block = "* * *"

# # classes
class Book:
    """parsed, structured contents of #.rst file"""

    def __init__( self ): #, file_name, file_path, number_lines, number_sections ):
        self._file_name       = ""
        self._file_path       = ""
        self._file_source     = self.file_path + self.file_name
        self._number_lines    = -1
        self._number_sections = -1
    # getters
    @property
    def file_name( self ):
        """I'm the file_name property."""
        print( "getter of file_name called: self.file_name = ", self._file_name )
        return self._file_name;
    @property
    def file_path( self ):
        """I'm the file_path property."""
        print( "getter of file_path called: self.file_path = ", self._file_path )
        return self._file_path;
    @property
    def number_lines( self ):
        """I'm the number_lines property."""
        print( "getter of number_lines called: self.number_lines = ", self._number_lines )
        return self._number_lines;

    # setters
    # @number_lines.setter
    # def number_lines( self, count ):
    #     self.number_lines = count

    @file_name.setter
    def file_name( self, myFile ):
        self._file_name = myFile

    @file_path.setter
    def file_path( self, myPath ):
        self._file_path = myPath

# # program blocks
def rst_file_harvest( myFile ):
    print( "\n", dingbat_block, "rst_file_harvest ", datetime.datetime.now( ) )

    file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"
    myBook = Book( )  # instantiate Book object
    myBook.file_name = myFile
    myBook.file_path = myPath

    ## ## read source file
    print ( "reading file %s" % myBook.file_source )
    # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
    with open( myBook.file_source ) as f:
        myLines = f.read().splitlines()  # remove \n

    numLines = len( myLines )
    print ( "%s lines found" % numLines )
    return myLines;

def rst_file_process( myFile ):
    print( "\n", dingbat_block, "rst_file_process ", datetime.datetime.now( ) )

    return;

def publish_xlsx( ):
    print( "\n", dingbat_block, "publish_xlsx ", datetime.datetime.now( ) )

    return;

def emulate_process( ):
    print( "\n", dingbat_block, "emulate_process ", datetime.datetime.now( ) )

    return;

def session_tag( ):
    print( "\n", dingbat_block, "session_tag ", datetime.datetime.now( ) )

    # forensic data
    print( "\npython version")
    print( sys.version )

    print( "\nfile:     ", os.path.basename( __file__ ) )
    print(   "directory:", os.getcwd( ) )

    print( datetime.datetime.now( ) )


# #    # #    # #    # #    # #    # #

if __name__ == "__main__":

    file_name = "sample.txt"

    myLines = rst_file_harvest( file_name )
    rst_file_process( myLines )
    publish_xlsx( )
    session_tag( )

# l127914@pn1249300.lanl.gov:prototype $ python argon.py
#
#  * * * rst_file_harvest  2018-11-21 10:30:29.947896
# reading file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/sample.txt
# 22 lines found
#
#  * * * rst_file_process  2018-11-21 10:30:29.948332
#
#  * * * publish_xlsx  2018-11-21 10:30:29.948361
#
#  * * * session_tag  2018-11-21 10:30:29.948383
#
# python version
# 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
#
# file:      argon.py
# directory: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/prototype
# 2018-11-21 10:30:29.948526
