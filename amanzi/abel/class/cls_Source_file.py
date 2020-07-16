#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Source_file class
#  source:  Amanzi manual to be parsed
#  sink:    Excel file with test matrix

class Source_file( object ):
    def __init__( self ):
        self._title     = None # from *.rst, line 2
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
        print( "getter of file_path called: self._title = ", self._title )
        return self._title
    # source
    @property
    def input_rst( self ):
        """Name of source file."""
        print( "getter of file_name called: self._input_rst = ", self._input_rst )
        return self._input_rst
    @property
    def path_rst( self ):
        """Path (absolute) to source file."""
        print( "getter of file_path called: self._path_rst = ", self._path_rst )
        return self._path_rst
    @property
    def full_rst( self ):
        """Path and file name."""
        print( "getter of file_path called: self._full_rst = ", self._full_rst )
        return self._full_rst
    # sink
    @property
    def output_xl( self ):
        """Name of sink file."""
        print( "getter of file_path called: self._output_xl = ", self._output_xl )
        return self._output_xl
    @property
    def path_xl( self ):
        """Path (absolute) to source file."""
        print( "getter of file_path called: self._path_xl = ", self._path_xl )
        return self._path_xl
    @property
    def full_xl( self ):
        """Path and file name."""
        print( "getter of file_path called: self._full_xl = ", self._full_xl )
        return self._full_xl

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.setter
    def title( self, value ):
        self._title = value
    # sink
    @input_rst .setter
    def file_name( self, value ):
        print("setter of _input_rst called: self._input_rst = ", value )
        self._input_rst = value
    @path_rst.setter
    def path_rst( self, value ):
        print("setter of _path_rst called: self._path_rst = ", value )
        self._path_rst = value
    @full_rst.setter
    def full_rst( self, value ):
        print("setter of _path_rst called: self._full_rst = ", value )
        self._full_rst = value
    # source
    @output_xl.setter
    def output_xl( self, value ):
        self._output_xl = value
    @path_xl.setter
    def path_xl( self, value ):
        print("setter of _path_rst called: self._path_xl = ", value )
        self._path_xl = value
    @full_xl.setter
    def full_xl( self, value ):
        print("setter of _path_xl called: self._full_xl = ", value )
        self._full_xl = value

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @title.deleter
    def title( self ):
        print( "deleter of title called" )
        del self._title
    # source
    @input_rst.deleter
    def input_rst( self ):
        print( "deleter of input_rst called" )
        del self._input_rst
        #del self._full_rst # delete because file name is no longer valid
    @path_rst.deleter
    def path_rst( self ):
        print( "deleter of path_rst called" )
        del self._path_rst
    @full_rst.deleter
    def path_name( self ):
        print( "deleter of full_rst called" )
        del self._full_rst
    # sink
    @output_xl.deleter
    def output_xl( self ):
        print( "deleter of output_xl called" )
        del self._output_xl
    @path_xl.deleter
    def path_xl( self ):
        print( "deleter of path_xl called" )
        del self._path_xl
    @full_xl.deleter
    def full_xl( self ):
        print( "deleter of full_xl called" )
        del self._full_xl

# dantopa@Lax-Millgram:class $ mypy cls_Source_file.py

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/aqua/class

# dantopa@Lax-Millgram:class $ date
# Tue Dec  4 20:24:14 MST 2018
