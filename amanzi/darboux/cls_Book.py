#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi

# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa   LANL/CCS-2   dantopa@lanl.gov 505 667 0817

import        cls_Chapter # chapter (constains sections)

# Book class
#  commentary

class Book( object ):
    def __init__( self ):

        self._title           = None    # Amanzi XML Input Specification (Version 2.3-draft)
        self._k_start         = None    # 5
        self._k_stop          = None    # 231
        self._source          = None    # input source
        self._xl_file         = None    # output
        self._col_chapters    = list( ) # collection of chapters


#   P R O P E R T I E S   #

    @property
    def title( self ):
        """Title of book"""
        return self._title

    @property
    def k_start( self ):
        """First line number of searchable text"""
        return self._k_start

    @property
    def k_stop( self ):
        """Last line number of searchable text"""
        return self._k_stop

    @property
    def source( self ):
        """Source file"""
        return self._source

    @property
    def xl_file( self ):
        """Excel spreadsheet"""
        return self._xl_file

    @property
    def col_chapters( self ):
        """Collection of chapter objects"""
        return self._col_chapters

#   S E T T E R S   #

    @title.setter
    def title( self, value ):
        self._title = value

    @k_start.setter
    def k_start( self, value ):
        self._k_start = value

    @k_stop.setter
    def k_stop( self, value ):
        self._k_stop = value

    @source.setter
    def source( self, value ):
        self._source = value

    @xl_file.setter
    def xl_file( self, value ):
        self._xl_file = value

    @col_chapters.setter
    def col_chapters( self, value ):
        self._col_chapters = value

#   D E L E T E R S   #

    @title.deleter
    def title( self ):
        del self._title

    @k_start.deleter
    def k_start( self ):
        del self._k_start

    @k_stop.deleter
    def k_stop( self ):
        del self._k_stop

    @source.deleter
    def source( self ):
        del self._source

    @xl_file.deleter
    def xl_file( self ):
        del self._xl_file

    @col_chapters.deleter
    def col_chapters( self ):
        del self._col_chapters

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# user: dantopa, CPU: Lax-Millgram, MM v. 11.3.0 for Mac OS X x86, date: Dec 12, 2018, time: 16:53:13, nb: /Users/dantopa/Mathematica_files/nb/lanl/python/author/class-structures-03.nb
