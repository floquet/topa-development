#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Source_file class
#  Amanzi manual to be parsed

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Source_file( object ):
    def __init__(self):
        self._file_name = None
#        self._file_path = None

    @property
    def file_name( self ):
        """Name of source file."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name
    # def file_path( self ):
    #     """I'm the file_path property."""
    #     print( "getter of file_path called: self._file_path = ", self._file_path )
    #     return self._file_path

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

    @file_name.deleter
    def file_name( self ):
        print( "deleter of x called" )
        del self._file_name
