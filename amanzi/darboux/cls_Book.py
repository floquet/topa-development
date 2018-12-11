#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa LANL/CCS-2 dantopa@lanl.gov 505 667 0817

# Book class
#  commentary

class Book( class ):
    def __init__( self ):

        self._title           = None    # Model Description
        self._number          = None    # 8
        self._key             = None    # 08-MD
        self._k_start         = None    # line number
        self._k_stop          = None    # line number
        self._col_elements    = list( ) # collection of elements
        self._col_sections    = list( ) # collection of sections


#   P R O P E R T I E S   #\:f3b5

    @property
    def title( self ):
        """Title of chapter"""
        return self._title

    @property
    def number( self ):
        """Chapter number"""
        return self._number

    @property
    def key( self ):
        """Unique key to tag chapter"""
        return self._key

    @property
    def k_start( self ):
        """Line number where chapter text starts"""
        return self._k_start

    @property
    def k_stop( self ):
        """Line number where chapter text starts"""
        return self._k_stop

    @property
    def col_elements( self ):
        """Collection of elements"""
        return self._col_elements

    @property
    def col_sections( self ):
        """Collection of sections"""
        return self._col_sections

#   S E T T E R S   #

    @title.setter
    def title( self, value ):
        self._title = value

    @number.setter
    def number( self, value ):
        self._number = value

    @key.setter
    def key( self, value ):
        self._key = value

    @k_start.setter
    def k_start( self, value ):
        self._k_start = value

    @k_stop.setter
    def k_stop( self, value ):
        self._k_stop = value

    @col_elements.setter
    def col_elements( self, value ):
        self._col_elements = value

    @col_sections.setter
    def col_sections( self, value ):
        self._col_sections = value

#   D E L E T E R S   #

    @title.deleter
    def title( self ):
        del self._title

    @number.deleter
    def number( self ):
        del self._number

    @key.deleter
    def key( self ):
        del self._key

    @k_start.deleter
    def k_start( self ):
        del self._k_start

    @k_stop.deleter
    def k_stop( self ):
        del self._k_stop

    @col_elements.deleter
    def col_elements( self ):
        del self._col_elements

    @col_sections.deleter
    def col_sections( self ):
        del self._col_sections

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# user: l127914, CPU: pn1249300, MM v. 11.3.0 for Mac OS X x86, date: Dec 10, 2018, time: 18:00:16, nb: /Users/l127914/Mathematica_files/nb/lanl/python/author/class-structures-02.nb
