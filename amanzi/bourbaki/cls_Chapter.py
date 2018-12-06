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
        self._loc_start     = None # starting line in source document
        self._num_sections  = None
        self._num_required  = None
        self._num_optional  = None
        self._list_required = None
        self._list_optional = None

    @property
    def title( self ):
        """Chapter title."""
        return self._title
    def key( self ):
        """Chapter title."""
        return self._key
    def loc_start( self ):
        """Chapter title."""
        return self._loc_start
    def num_sections( self ):
        """Chapter title."""
        return self._num_sections
    def num_required( self ):
        """Chapter title."""
        return self._num_required
    def num_optional( self ):
        """Chapter title."""
        return self._num_optional
    def list_required( self ):
        """Chapter title."""
        return self._list_required
    def list_optional( self ):
        """Chapter title."""
        return self._list_optional

    @title.setter
    def title( self, value ):
        self._title = value
    def key( self, value ):
        self._key = value
    def loc_start( self, value ):
        self._loc_start = value
    def num_sections( self, value ):
        self._num_sections = value
    def num_required( self, value ):
        self._num_required = value
    def num_optional( self, value ):
        self._num_optional = value
    def list_required( self, value ):
        self._list_required = value
    def list_optional( self, value ):
        self._list_optional = value

    @title.deleter
    def title( self ):
        del self._title
    def key( self ):
        del self._key
    def loc_start( self ):
        del self._loc_start
    def num_sections( self ):
        del self._num_sections
    def num_required( self ):
        del self._num_required
    def num_optional( self ):
        del self._num_optional
    def list_required( self ):
        del self._list_required
    def list_optional( self ):
        del self._list_optional

# l127914@pn1249300.lanl.gov:bourbaki $ python cls_Chapter.py

# l127914@pn1249300.lanl.gov:bourbaki $ date
# Thu Dec  6 15:46:44 MST 2018

# l127914@pn1249300.lanl.gov:bourbaki $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki
