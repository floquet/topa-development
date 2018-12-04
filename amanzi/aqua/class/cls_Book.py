#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# https://en.wikipedia.org/wiki/Document_Object_Model
# What is the Document Object Model?
# # https://www.w3.org/TR/WD-DOM/introduction.html
# Python and the XML Document Object Model (DOM) with 4Suite
# # https://infohost.nmt.edu/tcc/help/pubs/pyxml/

# Data Structures and Algorithms with Python: trees
# # http://knuth.luther.edu/~leekent/CS2Plus/chap6/chap6.html

# How to Think Like a Computer Scientist: Learning with Python - trees
# # https://www.openbookproject.net/thinkcs/python/english2e/ch21.html

# Book class
#  composed of sections

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Book( object ):
    def __init__(self):
        self._file_name = None
#        self._file_path = None

    @property
    def file_name( self ):
        """I'm the file_name property."""
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

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #
