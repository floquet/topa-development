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
        self._source_object = None

    @property
    def source_object( self ):
        """Source file."""
        print( "getter of source_object called: self._source_object = ", self._source_object )
        return self._source_object
    # def file_path( self ):
    #     """I'm the file_path property."""
    #     print( "getter of file_path called: self._file_path = ", self._file_path )
    #     return self._file_path

    @source_object.setter
    def source_object( self, value ):
        print("setter of _file_name called: self._source_object = ", value )
        self._source_object = value

    @source_object.deleter
    def source_object( self ):
        print( "deleter of source_object called" )
        del self._source_object

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# dantopa@Lax-Millgram:class $ mypy cls_Book.py

# dantopa@Lax-Millgram:class $ date
# Tue Dec  4 20:26:53 MST 2018

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/aqua/class
