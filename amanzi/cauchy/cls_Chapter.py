#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Chapter class
#  composed of sections (Constants, Macros, etc)

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Chapter( object ):
    def __init__(self):
        self._title         = None # chapter title
        self._key           = None # 01-MD
        self._num           = None # 01-MD
        self._loc_start     = None # starting line in source document
        self._loc_stop      = None # last line in source document
        self._num_sections  = None
        self._num_required  = None
        self._num_optional  = None
        self._list_required = None
        self._list_optional = None

    @property
    def title( self ):
        """Chapter title."""
        return self._title
    @property
    def key( self ):
        """Unique key to distinguish chapter."""
        return self._key
    @property
    def num( self ):
        """Chapter number."""
        return self._num
    @property
    def loc_start( self ):
        """Line number where chapter starts in source document."""
        return self._loc_start
    @property
    def loc_stop( self ):
        """Line number where chapter end in source document."""
        return self._loc_stop
    @property
    def num_sections( self ):
        """Number of sections within."""
        return self._num_sections
    @property
    def num_required( self ):
        """Count of required."""
        return self._num_required
    @property
    def num_optional( self ):
        """Count of optional."""
        return self._num_optional
    @property
    def list_required( self ):
        """List of keys for required."""
        return self._list_required
    @property
    def list_optional( self ):
        """List of keys for optional."""
        return self._list_optional

    @title.setter
    def title( self, value ):
        self._title = value
    @key.setter
    def key( self, value ):
        self._key = value
    @num.setter
    def num( self, value ):
        self._num = value
    @loc_start.setter
    def loc_start( self, value ):
        self._loc_start = value
    @loc_stop.setter
    def loc_stop( self, value ):
        self._loc_stop = value
    @num_sections.setter
    def num_sections( self, value ):
        self._num_sections = value
    @num_required.setter
    def num_required( self, value ):
        self._num_required = value
    @num_optional.setter
    def num_optional( self, value ):
        self._num_optional = value
    @list_required.setter
    def list_required( self, value ):
        self._list_required = value
    @list_optional.setter
    def list_optional( self, value ):
        self._list_optional = value

    @title.deleter
    def title( self ):
        del self._title
    @key.deleter
    def key( self ):
        del self._key
    @num.deleter
    def num( self ):
        del self._num
    @loc_start.deleter
    def loc_start( self ):
        del self._loc_start
    @loc_stop.deleter
    def loc_stop( self ):
        del self._loc_stop
    @num_sections.deleter
    def num_sections( self ):
        del self._num_sections
    @num_required.deleter
    def num_required( self ):
        del self._num_required
    @num_optional.deleter
    def num_optional( self ):
        del self._num_optional
    @list_required.deleter
    def list_required( self ):
        del self._list_required
    @list_optional.deleter
    def list_optional( self ):
        del self._list_optional

# dantopa@Lax-Millgram:cauchy $ py cls_Chapter.py

# dantopa@Lax-Millgram:cauchy $ date
# Fri Dec  7 19:41:36 MST 2018

# dantopa@Lax-Millgram:cauchy $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy
