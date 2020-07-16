#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Section class
#  composed of sections, subsection

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Section( object ):
    def __init__(self):
        self._title                  = None # section title
        self._level                  = None # section or subsection
        self._key                    = None # SS02
        self._num                    = None # 3
        self._loc_start              = None # starting line in source document
        self._loc_stop               = None # last line in source document
        self._num_sections           = None # number of subsections
        self._collection_subsections = list( ) # collection of subsections

    @property
    def title( self ):
        """Section title."""
        return self._title
    @property
    def level( self ):
        """Section = 1, subsection = 2."""
        return self._level
    @property
    def key( self ):
        """Unique key to distinguish section."""
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
        """Number of subsections included."""
        return self._num_sections
    @property
    def collection_subsections( self ):
        """Subsections included."""
        return self._collection_subsections

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
    @collection_subsections.setter
    def collection_subsections( self, value ):
        self._collection_subsections = value

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
    @collection_subsections.deleter
    def collection_subsections( self ):
        del self._collection_subsections

# dantopa@Lax-Millgram:cauchy $ py cls_Section.py

# dantopa@Lax-Millgram:cauchy $ date
# Sat Dec  8 17:44:23 MST 2018

# dantopa@Lax-Millgram:cauchy $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy
