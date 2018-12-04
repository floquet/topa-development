class Source_file( object ):
    def __init__(self):
        self._file_name = None
        self._file_path = None

    @property
    def file_name( self ):
        """Name of source file."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name

    def file_path( self ):
        """Path (absolute) to source file."""
        print( "getter of file_path called: self._file_path = ", self._file_path )
        return self._file_path

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

    @file_path.setter
    def file_path( self, value ):
        print("setter of _file_path called: self._file_path = ", value )
        self._file_path = value

# l127914@pn1249300.lanl.gov:class II $ python laboratory.py
# Traceback (most recent call last):
#   File "laboratory.py", line 1, in <module>
#     class Source_file( object ):
#   File "laboratory.py", line 22, in Source_file
#     @file_path.setter
# AttributeError: 'function' object has no attribute 'setter'

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II

# l127914@pn1249300.lanl.gov:class II $ date
# Mon Dec  3 17:56:37 MST 2018
