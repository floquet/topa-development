#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Source_file class
#  source:  Amanzi manual to be parsed
#  sink:    Excel file with test matrix

import uuid                 # Universal Unique IDentifier

class Source_file( object ):
    def __init__( self ):
        self._title         = None # from *.rst, line 2
        self._myLines       = None # text as a collection of lines, \n removed
        self._numLines      = None
        self._uuid          = uuid.uuid4( ) # de facto time stamp
        # source
        self._input_rst     = None # AmanziInputSpec-v2.3.2-draft.rst
        self._path_rst      = None
        self._full_rst      = None # path + file name
        # sink
        self._output_xl     = None # AmanziInputSpec-v2.3.2-draft.xlsx
        self._path_xl       = None
        self._full_xl       = None # path + file name
        # Excel rows
        self._row_PASS      = None
        self._row_FAIL      = None
        self._row_NULL      = None
        # census
        self._count_PASS    = None
        self._count_FAIL    = None
        self._count_NULL    = None
        # line numbers
        self._list_header0  = None

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @property
    def title( self ):
        """Title from source file."""
        return self._title
    @property
    def myLines( self ):
        """Text as a collection of lines with EOL removed."""
        return self._myLines
    @property
    def numLines( self ):
        """Number of lines read in source file."""
        return self._numLines
    @property           # https://docs.python.org/3/library/uuid.html
    def uuid( self ):   # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python
        """Universal unique identifier: connects requirements to source document."""
        return self._uuid
    # source
    @property
    def input_rst( self ):
        """Name of source file."""
        return self._input_rst
    @property
    def path_rst( self ):
        """Path (absolute) to source file."""
        return self._path_rst
    @property
    def full_rst( self ):
        """Path and file name."""
        return self._full_rst
    # sink
    @property
    def output_xl( self ):
        """Name of sink file."""
        return self._output_xl
    @property
    def path_xl( self ):
        """Path (absolute) to source file."""
        return self._path_xl
    @property
    def full_xl( self ):
        """Path and file name."""
        return self._full_xl
    # Excel rows
    @property
    def row_PASS( self ):
        """Row for next entry of requirements PASSed."""
        return self._row_PASS
    @property
    def row_FAIL( self ):
        """Row for next entry of requirements FAILed."""
        return self._row_FAIL
    @property
    def row_NULL( self ):
        """Row for next entry of requirements NULLed."""
        return self._row_NULL
    # census
    @property
    def count_PASS( self ):
        """Number of requirements PASSed."""
        return self._count_PASS
    @property
    def count_FAIL( self ):
        """Number of requirements FAILed."""
        return self._count_FAIL
    @property
    def count_NULL( self ):
        """Number of requirements NULLed."""
        return self._count_NULL
    # line numbers
    @property
    def list_header0( self ):
        """Culled list of === headers."""
        return self._list_header0

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.setter
    def title( self, value ):
        self._title = value
    @numLines.setter
    def numLines( self, value ):
        self._numLines = value
    @myLines.setter
    def myLines( self, value ):
        self._numLines = value
    # no @uuid.setter - accomplished at instantiation
    @input_rst.setter
    def input_rst( self, value ):
        self._input_rst = value
    @path_rst.setter
    def path_rst( self, value ):
        self._path_rst = value
    @full_rst.setter
    def full_rst( self, value ):
        self._full_rst = value
    # source
    @output_xl.setter
    def output_xl( self, value ):
        self._output_xl = value
    @path_xl.setter
    def path_xl( self, value ):
        self._path_xl = value
    @full_xl.setter
    def full_xl( self, value ):
        self._full_xl = value
    @row_PASS.setter
    def row_PASS( self, value ):
        self._row_PASS = value
    @row_FAIL.setter
    def row_FAIL( self, value ):
        self._row_FAIL = value
    @row_NULL.setter
    def row_NULL( self, value ):
        self._row_NULL = value
    # line numbers
    @list_header0.setter
    def list_header0( self, value ):
        self._list_header0 = value

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.deleter
    def title( self ):
        del self._title
    @myLines.deleter
    def myLines( self ):
        del self._myLines
    @numLines.deleter
    def numLines( self ):
        del self._numLines
    @uuid.deleter
    def uuid( self ):
        del self._uuid
    # source
    @input_rst.deleter
    def input_rst( self ):
        del self._input_rst
    @path_rst.deleter
    def path_rst( self ):
        del self._path_rst
    @full_rst.deleter
    def path_name( self ):
        del self._full_rst
    # sink
    @output_xl.deleter
    def output_xl( self ):
        del self._output_xl
    @path_xl.deleter
    def path_xl( self ):
        del self._path_xl
    @full_xl.deleter
    def full_xl( self ):
        del self._full_xl
    # Excel rows
    @row_PASS.deleter
    def row_PASS( self ):
        del self._row_PASS
    @row_FAIL.deleter
    def row_FAIL( self ):
        del self._row_FAIL
    @row_NULL.deleter
    def row_NULL( self ):
        del self._row_NULL
    # census values
    @count_PASS.deleter
    def count_PASS( self ):
        del self._count_PASS
    @count_FAIL.deleter
    def count_FAIL( self ):
        del self._count_FAIL
    @count_NULL.deleter
    def count_NULL( self ):
        del self._count_NULL
    # line numbers
    @list_header0.deleter
    def list_header0( self ):
        del self._list_header0

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def parse_master( self ):
        self.myLines = self.read_file( )
        self.title = self.myLines[ 1 ]
        ( loc_xml, loc_candidate_header0, loc_candidate_header1, loc_candidate_header2 ) = self.parse_candidates( self.myLines )  # first parse: candidate headers
        # find chapter headings ====
        self.parse_match_lengths( self.myLines, loc_candidate_header0 )
        # find chapter headings ---
        self.parse_match_lengths( self.myLines, loc_candidate_header1 )
        # find chapter headings ___
        self.parse_match_lengths( self.myLines, loc_candidate_header2 )

        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def read_file( self ):
        ## ## read source file
        print ( "reading source file %s" % self.full_rst )
        # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
        with open( self.full_rst ) as f:
            self.myLines = f.read( ).splitlines( )  # remove \n
            print( "self.myLines.myLines = %s" % self.myLines )
            self.numLines = len( self.myLines )

        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def parse_candidates( self ):
        # marker library
        xml = ".. code-block:: xml"   # xml
        header0 = "=="                # major heading
        header1 = "--"                # sub heading
        header2 = "__"                # subsub heading

        ## ## parse source file: pass 1
        loc_xml               = list( )  # xml locations container
        loc_header0           = list( )  # === locations container
        loc_candidate_header1 = list( )  # --- locations container
        loc_candidate_header2 = list( )  # ___ locations container

        lineNum = 0
        for line in self.myLines:
            lineNum += 1
            # xml blocks
            if line.find( xml ) != -1:
                loc_xml.append( lineNum )
                # header 0 blocks ==========
            elif line.find( header0 ) != -1:
                if line.find( "+" ) != -1:
                    continue
                loc_header0.append( lineNum )
            # header 1 blocks ----------
            elif line.find( header1 ) != -1:
                if line.find( "+" ) != -1:
                    continue
                loc_candidate_header1.append( lineNum )
            # header 2 blocks __________
            elif line.find( header2 ) != -1:
                loc_candidate_header2.append( lineNum )

        loc_candidate_header0 = loc_header0[ 4: ] # knock off title block, Overview, Amanzi Input

        print ( "{} xml blocks found; locations {}".format( len( loc_xml ), loc_xml ) )
        print ( "{} header0 '===' candidates found; locations {}".format( len( loc_candidate_header0 ), loc_candidate_header0 ) )
        print ( "{} header1 '---' candidates found; locations {}".format( len( loc_candidate_header1 ), loc_candidate_header1 ) )
        print ( "{} header2 '___' candidates found; locations {}".format( len( loc_candidate_header2 ), loc_candidate_header2 ) )

        return ( loc_xml, loc_candidate_header0, loc_candidate_header1, loc_candidate_header2 );

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def parse_match_lengths( self, loc_list ): # vet candidates
        loc = list( )  # location
        txt = list( )  # text
        for lineNum in loc_list:
            lineLengthA = len( self.myLines[ lineNum - 1 ] )
            lineLengthB = len( self.myLines[ lineNum - 2 ] )
            if lineLengthA == lineLengthB:
                loc.append( lineNum - 2 )
                txt.append( self.myLines[ lineNum - 2 ] )
                print( "header found in line {}: {} ".format( lineNum - 2, self.myLines[ lineNum - 2 ] ) )
        return

# dantopa@Lax-Millgram:cauchy $ py cls_Source_file.py

# dantopa@Lax-Millgram:cauchy $ date
# Fri Dec  7 18:38:46 MST 2018

# dantopa@Lax-Millgram:cauchy $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy
