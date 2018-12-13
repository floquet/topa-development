#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa LANL/CCS-2 dantopa@lanl.gov 505 667 0817

import       uuid

# Element class
#  commentary

class Element( object ):
    def __init__( self ):

        self._name            = None    # time_macro
        self._flavor          = None    # REQD or OPTL
        self._status          = None    # PASS | FAIL | NULL
        self._k_index         = None    # counter
        self._my_uuid         = uuid.uuid4( )
        self._k_line          = None    # 205
        self._key_head        = None    # 08-BC.S01.SS02.
        self._key_tail        = None    # OPTL-02
        self._k_chapter       = None    # 11
        self._k_section       = None    # 3
        self._k_subsection    = None    # 2
        self._xl_row          = None    # 5
        self._xl_col          = None    # 3


#   P R O P E R T I E S   #

    @property
    def name( self ):
        """Name of element"""
        return self._name

    @property
    def flavor( self ):
        """Required or Optional"""
        return self._flavor

    @property
    def status( self ):
        """PASS | FAIL | NULL"""
        return self._status

    @property
    def k_index( self ):
        """Element counter"""
        return self._k_index

    @property
    def my_uuid( self ):
        """Universal Unique IDentifier for element"""
        return self._my_uuid

    @property
    def k_line( self ):
        """Line number in source"""
        return self._k_line

    @property
    def key_head( self ):
        """Key portion which places element within document structure"""
        return self._key_head

    @property
    def key_tail( self ):
        """Key portion which places element list of elements"""
        return self._key_tail

    @property
    def k_chapter( self ):
        """Number of host chapter"""
        return self._k_chapter

    @property
    def k_section( self ):
        """Number of host section"""
        return self._k_section

    @property
    def k_subsection( self ):
        """Number of host subsection"""
        return self._k_subsection

    @property
    def xl_row( self ):
        """Row address for test status in spreadsheet"""
        return self._xl_row

    @property
    def xl_col( self ):
        """Col address for test status in spreadsheet"""
        return self._xl_col

#   S E T T E R S   #

    @name.setter
    def name( self, value ):
        self._name = value

    @flavor.setter
    def flavor( self, value ):
        self._flavor = value

    @status.setter
    def status( self, value ):
        self._status = value

    @k_index.setter
    def k_index( self, value ):
        self._k_index = value

    @k_line.setter
    def k_line( self, value ):
        self._k_line = value

    @key_head.setter
    def key_head( self, value ):
        self._key_head = value

    @key_tail.setter
    def key_tail( self, value ):
        self._key_tail = value

    @k_chapter.setter
    def k_chapter( self, value ):
        self._k_chapter = value

    @k_section.setter
    def k_section( self, value ):
        self._k_section = value

    @k_subsection.setter
    def k_subsection( self, value ):
        self._k_subsection = value

    @xl_row.setter
    def xl_row( self, value ):
        self._xl_row = value

    @xl_col.setter
    def xl_col( self, value ):
        self._xl_col = value

#   D E L E T E R S   #

    @name.deleter
    def name( self ):
        del self._name

    @flavor.deleter
    def flavor( self ):
        del self._flavor

    @status.deleter
    def status( self ):
        del self._status

    @k_index.deleter
    def k_index( self ):
        del self._k_index

    @my_uuid.deleter
    def my_uuid( self ):
        del self._my_uuid

    @k_line.deleter
    def k_line( self ):
        del self._k_line

    @key_head.deleter
    def key_head( self ):
        del self._key_head

    @key_tail.deleter
    def key_tail( self ):
        del self._key_tail

    @k_chapter.deleter
    def k_chapter( self ):
        del self._k_chapter

    @k_section.deleter
    def k_section( self ):
        del self._k_section

    @k_subsection.deleter
    def k_subsection( self ):
        del self._k_subsection

    @xl_row.deleter
    def xl_row( self ):
        del self._xl_row

    @xl_col.deleter
    def xl_col( self ):
        del self._xl_col

# user: dantopa, CPU: Lax-Millgram, MM v. 11.3.0 for Mac OS X x86,
# date: Dec 12, 2018, time: 16:03:48,
# nb: /Users/dantopa/Mathematica_files/nb/lanl/python/author/class-structures-03.nb

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def build_tail_key():
        self.tail_key = self.flavor + str( self.k_index ).zfill( 2 )
        return

# dantopa@Lax-Millgram:darboux $ py cls_Elements.py

# dantopa@Lax-Millgram:darboux $ date
# Wed Dec 12 16:09:21 MST 2018

# dantopa@Lax-Millgram:darboux $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/darboux
