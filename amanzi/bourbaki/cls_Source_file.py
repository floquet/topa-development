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
        self._title      = None # from *.rst, line 2
        self._numLines   = None
        self._uuid       = uuid.uuid4( ) # de facto time stamp
        # source
        self._input_rst  = None # AmanziInputSpec-v2.3.2-draft.rst
        self._path_rst   = None
        self._full_rst   = None # path + file name
        # sink
        self._output_xl  = None # AmanziInputSpec-v2.3.2-draft.xlsx
        self._path_xl    = None
        self._full_xl    = None # path + file name
        # Excel rows
        self._row_PASS   = 0
        self._row_FAIL   = 0
        self._row_NULL   = 0
        # census
        self._count_PASS = 0
        self._count_FAIL = 0
        self._count_NULL = 0

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @property
    def title( self ):
        """Title from source file."""
        return self._title
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
    def count_FAIL( self ):
        """Number of requirements FAILed."""
        return self._count_FAIL
    def count_NULL( self ):
        """Number of requirements NULLed."""
        return self._count_NULL


#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.setter
    def title( self, value ):
        self._title = value
    @numLines.setter
    def numLines( self, value ):
        self._numLines = value
    # no @uuid.setter - accomplished at instantiation
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

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.deleter
    def title( self ):
        del self._title
    @numLines.deleter
    def numLines( self ):
        del self._numLines
    @uuid.deleter
    def uuid( self ):
        del self._uuid
    # source
    # @input_rst.deleter
    # def input_rst( self ):
    #     del self._input_rst
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
    # @count_PASS.deleter
    # def count_PASS( self ):
    #     del self._count_PASS
    # @count_FAIL.deleter
    # def count_FAIL( self ):
    #     del self._count_FAIL
    # @count_NULL.deleter
    # def count_NULL( self ):
    #     del self._count_NULL

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def parse_candidates( self, myLines ):
        # marker library
        xml = ".. code-block:: xml"   # xml
        header0 = "=="                # major heading
        header1 = "--"                # sub heading
        header2 = "__"                # subsub heading

        ## ## parse source file: pass 1
        loc_xml               = list()  # xml locations container
        loc_candidate_header0 = list()  # === locations container
        loc_candidate_header1 = list()  # --- locations container
        loc_candidate_header2 = list()  # ___ locations container

        lineNum = 0
        for line in myLines:
            lineNum += 1
            # xml blocks
            if line.find( xml ) != -1:
                loc_xml.append( lineNum )
                # header 0 blocks ==========
            elif line.find( header0 ) != -1:
                if line.find( "+" ) != -1:
                    continue
                loc_candidate_header0.append( lineNum )
            # header 1 blocks ----------
            elif line.find( header1 ) != -1:
                if line.find( "+" ) != -1:
                    continue
                loc_candidate_header1.append( lineNum )
            # header 2 blocks __________
            elif line.find( header2 ) != -1:
                loc_candidate_header2.append( lineNum )

        print ( "{} xml blocks found; locations {}".format( len( loc_xml ), loc_xml ) )
        print ( "{} header0 '===' candidates found; locations {}".format( len( loc_candidate_header0 ), loc_candidate_header0 ) )
        print ( "{} header1 '---' candidates found; locations {}".format( len( loc_candidate_header1 ), loc_candidate_header1 ) )
        print ( "{} header2 '___' candidates found; locations {}".format( len( loc_candidate_header2 ), loc_candidate_header2 ) )

        return ( loc_xml, loc_candidate_header0, loc_candidate_header1, loc_candidate_header2 );

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def parse_match_lengths( self, myLines, loc_list ): # vet candidates
        loc = list( )  # location
        txt = list( )  # text
        for lineNum in loc_list:
            lineLengthA = len( myLines[ lineNum - 1 ] )
            lineLengthB = len( myLines[ lineNum - 2 ] )
            if lineLengthA == lineLengthB:
                loc.append( lineNum - 2 )
                txt.append( myLines[ lineNum - 2 ] )
                print( "header found in line {}: {} ".format( lineNum - 2, myLines[ lineNum - 2 ] ) )
        return

# l127914@pn1249300.lanl.gov:bourbaki $ python catullus.py
# mySource.uuid = 6ca4262b-74c7-4ba8-afe2-ea6e67cb6123
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# 231 lines found
# 16 xml blocks found; locations [28, 38, 56, 81, 101, 113, 122, 128, 134, 140, 149, 162, 170, 185, 198, 207]
# 6 header0 '===' candidates found; locations [1, 3, 9, 18, 34, 97]
# 8 header1 '---' candidates found; locations [48, 65, 69, 71, 73, 75, 109, 145]
# 8 header2 '___' candidates found; locations [48, 65, 69, 71, 73, 75, 109, 145]
# header found in line 7: Overview
# header found in line 16: Amanzi Input
# header found in line 32: Model Description
# header found in line 95: Definitions
# header found in line 46: Units
# header found in line 67: | length_unit    | m or cm        |
# header found in line 69: | time_unit      | y, d, h, or s  |
# header found in line 71: | mass_unit      | kg             |
# header found in line 73: | conc_unit      | molar, SI      |
# header found in line 107: Constants
# header found in line 143: Macros
# header found in line 156: Time_macro
# header found in line 178: Cycle_macro
# header found in line 192: Variable_macro

#  2018-12-06 14:39:25.069898
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki/catullus.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
