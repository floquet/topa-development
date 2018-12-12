#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa LANL/CCS-2 dantopa@lanl.gov 505 667 0817

import        cls_Chapter # chapter (constains sections)

# Book class
#  commentary

class Book( object ):
    def __init__( self ):

        self._title           = None    # Amanzi XML Input Specification (Version 2.3-draft)
        self._k_start         = None    # 5
        self._k_stop          = None    # 231
        self._col_chapter     = list( ) # collection of chapters


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
    def col_chapter( self ):
        """Collection of chapter objects"""
        return self._col_chapter

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

    @col_chapter.setter
    def col_chapter( self, value ):
        self._col_chapter = value

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

    @col_chapter.deleter
    def col_chapter( self ):
        del self._col_chapter

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# user: dantopa, CPU: Lax-Millgram, MM v. 11.3.0 for Mac OS X x86,
# date: Dec 12, 2018, time: 16:37:20,
# nb: /Users/dantopa/Mathematica_files/nb/lanl/python/author/class-structures-03.nb

# dantopa@Lax-Millgram:darboux $ py cls_Book.py 

# dantopa@Lax-Millgram:darboux $ date
# Wed Dec 12 16:42:40 MST 2018

# dantopa@Lax-Millgram:darboux $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/darboux
