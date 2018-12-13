#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa   LANL/CCS-2   dantopa@lanl.gov 505 667 0817

# Chapter class
#  commentary

class Chapter( object ):
    def __init__( self ):

        self._title           = None    # Model Description
        self._key             = None    # 08-MD
        self._k_start         = None    # 5
        self._k_stop          = None    # 231
        self._col_sections    = list( ) # collection of sections

#   P R O P E R T I E S   #

    @property
    def title( self ):
        """Chapter title"""
        return self._title

    @property
    def key( self ):
        """Unique key to tag chapter"""
        return self._key

    @property
    def k_start( self ):
        """First line number of searchable text"""
        return self._k_start

    @property
    def k_stop( self ):
        """Last line number of searchable text"""
        return self._k_stop

    @property
    def col_sections( self ):
        """Collection of section objects"""
        return self._col_sections

#   S E T T E R S   #

    @title.setter
    def title( self, value ):
        self._title = value

    @key.setter
    def key( self, value ):
        self._key = value

    @k_start.setter
    def k_start( self, value ):
        self._k_start = value

    @k_stop.setter
    def k_stop( self, value ):
        self._k_stop = value

    @col_sections.setter
    def col_sections( self, value ):
        self._col_sections = value

#   D E L E T E R S   #

    @title.deleter
    def title( self ):
        del self._title

    @key.deleter
    def key( self ):
        del self._key

    @k_start.deleter
    def k_start( self ):
        del self._k_start

    @k_stop.deleter
    def k_stop( self ):
        del self._k_stop

    @col_sections.deleter
    def col_sections( self ):
        del self._col_sections

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# user: dantopa, CPU: Lax-Millgram, MM v. 11.3.0 for Mac OS X x86, date: Dec 12, 2018, time: 16:40:24, nb: /Users/dantopa/Mathematica_files/nb/lanl/python/author/class-structures-03.nb

# dantopa@Lax-Millgram:darboux $ py cls_Chapter.py

# dantopa@Lax-Millgram:darboux $ date
# Wed Dec 12 16:43:28 MST 2018

# dantopa@Lax-Millgram:darboux $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/darboux
