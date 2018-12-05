#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Source_file class
#  source:  Amanzi manual to be parsed
#  sink:    Excel file with test matrix

class Source_file( object ):
    def __init__( self ):
        self._title     = None # from *.rst, line 2
        self._numLines  = None
        # source
        self._input_rst = None # AmanziInputSpec-v2.3.2-draft.rst
        self._path_rst  = None
        self._full_rst  = None # path + file name
        # sink
        self._output_xl = None # AmanziInputSpec-v2.3.2-draft.xlsx
        self._path_xl   = None
        self._full_xl   = None # path + file name

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @property
    def title( self ):
        """Title from source file."""
        return self._title
    @property
    def numLines( self ):
        """Number of lines read in source file."""
        return self._numLines
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

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.setter
    def title( self, value ):
        self._title = value
    @numLines.setter
    def numLines( self, value ):
        self._numLines = value
    # sink
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

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.deleter
    def title( self ):
        del self._title
    # source
    @input_rst.deleter
    def input_rst( self ):
        del self._input_rst
        #del self._full_rst # delete because file name is no longer valid
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

# dantopa@Lax-Millgram:class $ mypy cls_Source_file.py

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/aqua/class

# dantopa@Lax-Millgram:class $ date
# Tue Dec  4 20:24:14 MST 2018
