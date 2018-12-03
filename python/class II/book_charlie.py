#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

# # imports
import datetime         # timestamps
import os               # opeating system
import classes          # Book, Chapter, Section, etc.

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    myBook = classes.Book()
    myBook.file_name = "file.rst"    # setter called
    foo = myBook.file_name           # getter called
    print( "myBook.file_name = ", myBook.file_name )
    print( "foo = ", foo )
    del myBook.file_name             # deleter called
    print( datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "myBook.file_name = ", myBook.file_name )

# l127914@pn1249300.lanl.gov:class II $ python book_basics.py
# setter of _file_name called: self._file_name =  file.rst
# getter of file_name called: self._file_name =  file.rst
# getter of file_name called: self._file_name =  file.rst
# myBook.file_name =  file.rst
# foo =  file.rst
# deleter of x called
# 2018-12-03 12:16:34.725406
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II/book_basics.py
# Traceback (most recent call last):
#   File "book_basics.py", line 46, in <module>
#     print( "myBook.file_name = ", myBook.file_name )
#   File "book_basics.py", line 17, in file_name
#     print( "getter of file_name called: self._file_name = ", self._file_name )
# AttributeError: 'Book' object has no attribute '_file_name'
