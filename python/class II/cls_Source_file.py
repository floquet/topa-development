#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# Source_file class
#  Amanzi manual to be parsed

class Source_file( object ):
    def __init__(self):
        self._file_name = None
        self._file_path = None
        #self._path_name = None

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @property
    def file_name( self ):
        """Name of source file."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name

    @property
    def file_path( self ):
        """Path (absolute) to source file."""
        print( "getter of file_path called: self._file_path = ", self._file_path )
        return self._file_path

    # @property
    # def path_name( self, file_name, path_name ):
    #     """File path and name."""
    #     print( "getter of file_path called: self._path_name = ", self._path_name )
    #     return self._path_name

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

    @file_path.setter
    def file_path( self, value ):
        print("setter of _file_path called: self._file_path = ", value )
        self._file_path = value

    # @path_name.setter
    # def file_path( self ):
    #     self._path_name = self.file_path + self.file_name
    #     print("setter of _file_path called: self._file_path = ", self._path_name )

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

    # @file_name.deleter
    # def file_name( self ):
    #     print( "deleter of file_name called" )
    #     del self._file_name
    #     #del self._path_name # delete because file name is no longer valid
    #
    # @file_path.deleter
    # def file_path( self ):
    #     print( "deleter of file_path called" )
    #     del self._file_path
        #del self._path_name # delete because file path is no longer valid
    # @file_path_name.deleter
    # def path_name( self ):
    #     print( "deleter of path_name called" )

# l127914@pn1249300.lanl.gov:class II $ python cls_Source_file.py

# l127914@pn1249300.lanl.gov:class II $ date
# Mon Dec  3 19:20:31 MST 2018

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II
