#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa LANL/CCS-2 dantopa@lanl.gov 505 667 0817

# Source class
#  source:  Amanzi manual to be parsed
#  sink:    Excel file with test matrix

import uuid                 # Universal Unique IDentifier
from pathlib import Path    # rename file

class Source( object ):
    def __init__( self ):

        self._title           = None    # from *.rst, line 2
        self._col_lines       = list( ) # text as a collection of lines, EOL removed
        self._numLines        = None    # census
        self._uuid            = None    # de facto time stamp
        # source
        self._input_rst       = None    # AmanziInputSpec-v2.3.2-draft.rst
        self._path_rst        = None    # absolute path
        self._full_rst        = None    # path + file name
        # sink
        self._input_xl        = None    # AmanziInputSpec-v2.3.2-draft.xlsx
        self._path_xl         = None    # absolute path
        self._full_xl         = None    # path + file name

#   P R O P E R T I E S   #

    @property
    def title( self ):
        """Title from source file"""
        return self._title

    @property
    def col_lines( self ):
        """text as a collection of lines, EOL removed"""
        return self._col_lines

    @property
    def numLines( self ):
        """Number of lines read in source file"""
        return self._numLines

    @property
    def uuid( self ):
        """Universal unique identifier: connects requirements to source document"""
        return self._uuid

    @property
    def input_rst( self ):
        """Name of source file"""
        return self._input_rst

    @property
    def path_rst( self ):
        """Path (absolute) to source file"""
        return self._path_rst

    @property
    def full_rst( self ):
        """Path + Name"""
        return self._full_rst

    @property
    def input_xl( self ):
        """Name of source file"""
        return self._input_xl

    @property
    def path_xl( self ):
        """Path (absolute) to output file"""
        return self._path_xl

    @property
    def full_xl( self ):
        """Path + Name"""
        return self._full_xl

#   S E T T E R S   #

    @title.setter
    def title( self, value ):
        self._title = value

    @col_lines.setter
    def col_lines( self, value ):
        self._col_lines = value

    @numLines.setter
    def numLines( self, value ):
        self._numLines = value

    @uuid.setter
    def uuid( self, value ):
        self._uuid = value

    @input_rst.setter
    def input_rst( self, value ):
        self._input_rst = value

    @path_rst.setter
    def path_rst( self, value ):
        self._path_rst = value

    @full_rst.setter
    def full_rst( self, value ):
        self._full_rst = value

    @input_xl.setter
    def input_xl( self, value ):
        self._input_xl = value

    @path_xl.setter
    def path_xl( self, value ):
        self._path_xl = value

    @full_xl.setter
    def full_xl( self, value ):
        self._full_xl = value

#   D E L E T E R S   #

    @title.deleter
    def title( self ):
        del self._title

    @col_lines.deleter
    def col_lines( self ):
        del self._col_lines

    @numLines.deleter
    def numLines( self ):
        del self._numLines

    @uuid.deleter
    def uuid( self ):
        del self._uuid

    @input_rst.deleter
    def input_rst( self ):
        del self._input_rst

    @path_rst.deleter
    def path_rst( self ):
        del self._path_rst

    @full_rst.deleter
    def full_rst( self ):
        del self._full_rst

    @input_xl.deleter
    def input_xl( self ):
        del self._input_xl

    @path_xl.deleter
    def path_xl( self ):
        del self._path_xl

    @full_xl.deleter
    def full_xl( self ):
        del self._full_xl

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def read_file( self ):
        ## ## read source file
        print ( "reading source file %s" % self.full_rst )
        # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
        with open( self.full_rst ) as f:
            self.col_lines = f.read( ).splitlines( )
            self.numLines = len( self.col_lines )
        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def setup_io( self ):
        # combine path and file name
        self.full_rst  = self.path_rst + self.input_rst
        # # output file: same directory
        self.output_xl = Path( self.input_rst ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
        self.path_xl   = self.path_rst
        self.full_xl   = self.path_xl + self.output_xl
        return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    def search_elements_crude( self ):
        # containers for line numbers
        l_reqd = list( )
        l_optl = list( )
        
        # required elements
        k_line = 1
        for line in self.col_lines:
            # required
            if line.find( "Required Elements:" ) != -1:
                print( "line {} = {}".format( k_line, line ) )
                if line.find( "NONE" ) != -1:
                    continue
                l_reqd.append( k_lines )
            k_line += 1
            
        # optional elements
        k_line = 1
        for line in self.col_lines:
            # optional
            if line.find( "Optional Elements:" ) != -1:
                print( "line {} = {}".format( k_line, line ) )
                if line.find( "NONE" ) != -1:
                    continue
                l_optl.append( k_lines )
            k_line += 1
            

        print ( "{} lines with required elements found; locations {}".format( len( l_reqd ), l_reqd ) )
        print ( "{} lines with optional elements found; locations {}".format( len( l_optl ), l_optl ) )

        return ( l_reqd, l_optl )

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #


# user: l127914, CPU: pn1249300, MM v. 11.3.0 for Mac OS X x86
# date: Dec 10, 2018, time: 18:24:50
# nb: /Users/l127914/Mathematica_files/nb/lanl/python/author/class-structures-02.nb

#dantopa@Mittag-Leffler.local:darboux $ python cls_Source.py 

#dantopa@Mittag-Leffler.local:darboux $ date
#Tue Dec 11 19:40:02 MST 2018

#dantopa@Mittag-Leffler.local:darboux $ pwd
#/Volumes/Tethys/repos/GitHub/topa-development/amanzi/darboux
