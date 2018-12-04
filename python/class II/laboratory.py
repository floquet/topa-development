class Source_file( object ):
    def __init__(self):
        self._file_name = None

    @property
    def file_name( self ):
        """Name of source file."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

# l127914@pn1249300.lanl.gov:class II $ python laboratory.py

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II

# l127914@pn1249300.lanl.gov:class II $ date
# Mon Dec  3 17:53:40 MST 2018
