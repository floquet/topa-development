# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

class C(object):
    def __init__(self):
        self._file_name = None
#        self._file_path = None

    @property
    def file_name( self ):
        """I'm the file_name property."""
        print( "getter of file_name called: self._file_name = ", self._file_name )
        return self._file_name
    # def file_path( self ):
    #     """I'm the file_path property."""
    #     print( "getter of file_path called: self._file_path = ", self._file_path )
    #     return self._file_path

    @file_name.setter
    def file_name( self, value ):
        print("setter of _file_name called: self._file_name = ", value )
        self._file_name = value

    @file_name.deleter
    def file_name( self ):
        print( "deleter of x called" )
        del self._file_name
        print( "\nattempting to print self._file_name: disaster entails" )
        print( "self._file_name = ", self._file_name )

c = C()
c.file_name = "file.rst"    # setter called
foo = c.file_name           # getter called
print( "foo = ", foo )
del c.file_name             # deleter called

# l127914@pn1249300.lanl.gov:class $ python objects-python-A.py
# setter of x called: self._file_name =  foo
# getter of x called: self._file_name =  foo
# deleter of x called
#
# attempting to print self._file_name: disaster entails
# Traceback (most recent call last):
#   File "objects-python-A.py", line 28, in <module>
#     del c.x      # deleter called
#   File "objects-python-A.py", line 23, in x
#     print( "self._file_name = ", self._file_name )
# AttributeError: 'C' object has no attribute '_file_name'

# l127914@pn1249300.lanl.gov:class $ date
# Wed Nov 21 10:25:02 MST 2018

# l127914@pn1249300.lanl.gov:class $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class
