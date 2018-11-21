# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x( self ):
        """I'm the 'x' property."""
        print( "getter of x called: self._x = ", self._x )
        return self._x

    @x.setter
    def x( self, value ):
        print("setter of x called: self._x = ", value )
        self._x = value

    @x.deleter
    def x( self ):
        print( "deleter of x called" )
        del self._x
        print( "\nattempting to print self._x: disaster entails" )
        print( "self._x = ", self._x )

c = C()
c.x = "my value"    # setter called
foo = c.x           # getter called
del c.x             # deleter called

# l127914@pn1249300.lanl.gov:class $ python objects-python-A.py
# setter of x called: self._x =  foo
# getter of x called: self._x =  foo
# deleter of x called
#
# attempting to print self._x: disaster entails
# Traceback (most recent call last):
#   File "objects-python-A.py", line 28, in <module>
#     del c.x      # deleter called
#   File "objects-python-A.py", line 23, in x
#     print( "self._x = ", self._x )
# AttributeError: 'C' object has no attribute '_x'

# l127914@pn1249300.lanl.gov:class $ date
# Wed Nov 21 10:25:02 MST 2018

# l127914@pn1249300.lanl.gov:class $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class
