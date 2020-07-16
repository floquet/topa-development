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
        self._collection_chapters = None # collection of chapter objects

    @property
    def source_object( self ):
        """Source file object."""
        return self._source_object
    @property
    def collection_chapters( self ):
        """Collection of chapter objects."""
        return self._collection_chapters

    @source_object.setter
    def source_object( self, value ):
        self._source_object = value
    @collection_chapters.setter
    def collection_chapters( self, value ):
        self._collection_chapters = value

    @source_object.deleter
    def source_object( self ):
        del self._source_object
    @collection_chapters.deleter
    def collection_chapters( self ):
        del self.collection_chapters

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# l127914@pn1249300.lanl.gov:bourbaki $ python cls_Book.py

# l127914@pn1249300.lanl.gov:bourbaki $ date
# Thu Dec  6 15:56:44 MST 2018

# l127914@pn1249300.lanl.gov:bourbaki $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki
