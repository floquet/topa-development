# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

class Book(object):
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

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    myBook = Book()
    myBook.file_name = "file.rst"    # setter called
    foo = myBook.file_name           # getter called
    print( "myBook.file_name = ", myBook.file_name )
    print( "foo = ", foo )
    del myBook.file_name             # deleter called
    print( "myBook.file_name = ", myBook.file_name )

# l127914@pn1249300.lanl.gov:class II $ python book_basics.py
# setter of _file_name called: self._file_name =  file.rst
# getter of file_name called: self._file_name =  file.rst
# getter of file_name called: self._file_name =  file.rst
# myBook.file_name =  file.rst
# foo =  file.rst
# deleter of x called
# Traceback (most recent call last):
#   File "book_basics.py", line 38, in <module>
#     print( "myBook.file_name = ", myBook.file_name )
#   File "book_basics.py", line 11, in file_name
#     print( "getter of file_name called: self._file_name = ", self._file_name )
# AttributeError: 'Book' object has no attribute '_file_name'

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II

# l127914@pn1249300.lanl.gov:class II $ date
# Mon Dec  3 12:09:29 MST 2018
