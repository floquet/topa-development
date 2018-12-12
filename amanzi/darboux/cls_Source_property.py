#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

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
