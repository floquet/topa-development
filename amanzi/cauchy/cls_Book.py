#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
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
#  composed of chapters

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Book( object ):
    def __init__(self):
        self._source_object       = None # source file, meta data
        self._numChapters         = None # number of chapters
        self._collection_chapters = None # collection of chapter objects

    @property
    def source_object( self ):
        """Source file object."""
        return self._source_object
    @property
    def numChapters( self ):
        """Number of chapter objects."""
        return self._numChapters
    @property
    def collection_chapters( self ):
        """Collection of chapter objects."""
        return self._collection_chapters

    @source_object.setter
    def source_object( self, value ):
        self._source_object = value
    @numChapters.setter
    def numChapters( self, value ):
        self._numChapters = value
    @collection_chapters.setter
    def collection_chapters( self, value ):
        self._collection_chapters = value

    @source_object.deleter
    def source_object( self ):
        del self._source_object
    @numChapters.deleter
    def numChapters( self ):
        del self.numChapters
    @collection_chapters.deleter
    def collection_chapters( self ):
        del self.collection_chapters

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters( self ):
        print( "self.source_object.parse_alpha" )
        locations = self.source_object.parse_alpha( "===" )
        myResults = self.source_object.parse_match_lengths( locations )
        print( "myResults = %s" % myResults )
        count = 0
        for loc, txt in myResults:
            self.collection_chapters.append( Chapter( loc_start = loc, title = txt ) )
            count += 1
        self.numChapters = count
        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def create_chapters( self, locations ):
        locations = self.source_object.parse_alpha( "===" )
        locations.append( self.source_object.numLines )
        return locations
        locations.append( self.source_object.numLines )

# dantopa@Lax-Millgram:cauchy $ py cls_Book.py

# dantopa@Lax-Millgram:cauchy $ date
# Fri Dec  7 20:07:36 MST 2018

# dantopa@Lax-Millgram:cauchy $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy
