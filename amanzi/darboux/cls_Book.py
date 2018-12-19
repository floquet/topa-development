#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi

# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa   LANL/CCS-2   dantopa@lanl.gov 505 667 0817

# Book class
#  commentary

# home brew
# classes
import cls_Chapter          # chapter (constains sections)

class Book( object ):
    def __init__( self ):

        self._title           = None    # Amanzi XML Input Specification (Version 2.3-draft)
        self._k_index         = None    # chapter number
        self._k_start         = None    # 5
        self._k_stop          = None    # 231
        self._source          = None    # input source
        self._xl_file         = None    # output
        self._col_chapters    = list( ) # collection of chapters
        self._col_elements    = list( ) # collection of elements

#   P R O P E R T I E S   #

    @property
    def title( self ):
        """Title of book"""
        return self._title
 
    @property
    def k_index( self ):
        """Chapter number"""
        return self._k_start

    @property
    def k_start( self ):
        """First line number of searchable text"""
        return self._k_start

    @property
    def k_stop( self ):
        """Last line number of searchable text"""
        return self._k_stop

    @property
    def source( self ):
        """Source file"""
        return self._source

    @property
    def xl_file( self ):
        """Excel spreadsheet"""
        return self._xl_file

    @property
    def col_chapters( self ):
        """Collection of chapter objects"""
        return self._col_chapters

    @property
    def col_elements( self ):
        """Collection of element objects"""
        return self._col_elements

#   S E T T E R S   #

    @title.setter
    def title( self, value ):
        self._title = value

    @k_index.setter
    def k_index( self, value ):
        self._k_index = value

    @k_start.setter
    def k_start( self, value ):
        self._k_start = value

    @k_stop.setter
    def k_stop( self, value ):
        self._k_stop = value

    @source.setter
    def source( self, value ):
        self._source = value

    @xl_file.setter
    def xl_file( self, value ):
        self._xl_file = value

    @col_chapters.setter
    def col_chapters( self, value ):
        self._col_chapters = value

    @col_elements.setter
    def col_elements( self, value ):
        self._col_elements = value

#   D E L E T E R S   #

    @title.deleter
    def title( self ):
        del self._title

    @k_index.deleter
    def k_index( self ):
        del self._k_index

    @k_start.deleter
    def k_start( self ):
        del self._k_start

    @k_stop.deleter
    def k_stop( self ):
        del self._k_stop

    @source.deleter
    def source( self ):
        del self._source

    @xl_file.deleter
    def xl_file( self ):
        del self._xl_file

    @col_chapters.deleter
    def col_chapters( self ):
        del self._col_chapters

    @col_elements.deleter
    def col_elements( self ):
        del self._col_elements

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters( self ):
        start_locations = self.mark_chapters_start( )
        self.mark_chapters_stop( start_locations )
        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters_start( self ):
        locations = self.source.parse_alpha( "===", 0, self.source.numLines )
        ( loc, txt ) = self.source.parse_match_lengths( locations )
        count = 0
        for myLoc, myTxt in zip( loc, txt ): # ( myLoc, myTxt ) = 32, Model Description
            myChapter           = cls_Chapter.Chapter( )
            count              += 1
            myChapter.title     = myTxt # chapter title
            myChapter.k_start   = myLoc # first line of chapter
            myChapter.k_index   = count # chapter number
            myChapter.key       = str( count ).zfill( 2 )
            self.col_chapters.append( myChapter )
        return loc

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def mark_chapters_stop( self, start_locations ):
        del start_locations[ 2 ] # remove first element
        print( "1. start_locations = %s" % start_locations )
        # https://stackoverflow.com/questions/9304408/how-to-add-an-integer-to-each-element-in-a-list
        # https://nedbatchelder.com/text/names1.html
        start_locations = [ l - 3 for l in start_locations ]
        print( "2. start_locations = %s" % start_locations )
        # https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list
        start_locations.append( self.source.numLines )
        for ( c, l ) in zip( self.col_chapters, start_locations ):
            c.k_stop = l
        for c in self.col_chapters:
            print( "chapter {}: {}".format( c.k_index, c.title ) )
            print( "first, last: {}, {}".format( c.k_start, c.k_stop ) )
        return

    #  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #


# user: l127914, CPU: pn1249300, MM v. 11.3.0 for Mac OS X x86

# date: Dec 12, 2018, time: 18:55:09

# nb: /Users/l127914/Mathematica_files/nb/lanl/python/author/class-structures-04.nb
