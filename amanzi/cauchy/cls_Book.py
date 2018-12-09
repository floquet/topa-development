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

# classes
import cls_Chapter          # chapter (constains sections, contains requirements)

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Book( object ):
    def __init__(self):
        self._source_object       = None # source file, meta data
        self._numChapters         = None # number of chapters
        self._collection_chapters = list( ) # collection of chapter objects

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
        start_locations = self.mark_chapters_start( )
        self.mark_chapters_stop( start_locations )
        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters_start( self ):
        locations = self.source_object.parse_alpha( "===", 0, self.source_object.numLines )
        ( loc, txt ) = self.source_object.parse_match_lengths( locations )
        count = 0
        for myLoc, myTxt in zip( loc, txt ): # ( myLoc, myTxt ) = 32, Model Description
            count += 1
            myChapter = cls_Chapter.Chapter( )
            myChapter.loc_start = myLoc # first line of chapter
            myChapter.title     = myTxt # chapter title
            myChapter.num       = count # chapter number
            myChapter.key       = str( count ).zfill( 2 )
            self.collection_chapters.append( myChapter )
            print( "myChapter = %s" % myChapter )
        self.numChapters = count
        print( "number of chapters = %s" % count )
        return loc

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters_stop( self, start_locations ):
        del start_locations[ 0 ] # remove first element
        print( "1. start_locations = %s" % start_locations )
        # https://stackoverflow.com/questions/9304408/how-to-add-an-integer-to-each-element-in-a-list
        # https://nedbatchelder.com/text/names1.html
        start_locations = [ l - 1 for l in start_locations ]
        print( "2. start_locations = %s" % start_locations )
        # https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list
        start_locations.append( self.source_object.numLines )
        for ( c, l ) in zip( self.collection_chapters, start_locations ):
            c.loc_stop = l
        for c in self.collection_chapters:
            print( "chapter {}: {}".format( c.num, c.title ) )
            print( "first, last: {}, {}".format( c.loc_start, c.loc_stop ) )
        return


# dantopa@Lax-Millgram:cauchy $ py cls_Book.py

# dantopa@Lax-Millgram:cauchy $ date
# Fri Dec  7 20:07:36 MST 2018

# dantopa@Lax-Millgram:cauchy $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy
