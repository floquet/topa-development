class Source_file( object ):
    def __init__( self ):
        self._file_path = None
        self._file_name = None
        self._path_name = None

    @property
    def file_path( self ):
        """Path (absolute) to source file."""
        print( "getter of file_path called: self._file_path = ", self._file_path )
        return self._file_path

    @property
    def file_name( self ):
        """Name of source file."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name

    @property
    def path_name( self ):
        """Full path and file name."""
        print( "getter of file_name called: self._file_name = ", self._path_name )
        return self._path_name

    @file_path.setter
    def file_path( self, value ):
        print("setter of _file_path called: self._file_path = ", value )
        self._file_path = value

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

    @path_name.setter
    def path_name( self, value ):
        self._path_name = self._file_path + self._file_name
        print("setter of _path_name called: self._path_name = ", value )

# l127914@pn1249300.lanl.gov:class II $ python laboratory.py

# l127914@pn1249300.lanl.gov:class II $ date
# Mon Dec  3 19:20:56 MST 2018

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II
