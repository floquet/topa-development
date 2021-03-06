#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters

# # imports
import datetime         # timestamps
import os               # opeating system
import sys              # python version
import uuid             # Universal Unique IDentifier
# home brew
import cls_Book         # Book (constains sections, contains requirements)
import cls_Source_file  # e.q. Amanzi XML Input Specification (Version 2.3-draft)

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    mySource = cls_Source_file.Source_file( ) # instantiate
    mySource.file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/"    # setter called
    mySource.file_name = "short.rst"    # setter called
    #print( "mySource.path_name = %s", mySource.path_name )
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    # myBook = cls_Book.Book( ) # instantiate
    # mySource.file_name = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/short.rst"    # setter called
    # foo = mySource.file_name           # getter called
    # bar = os.path.basename( mySource.file_name )
    # print( "myBook.file_name = ", mySource.file_name )
    # print( "foo = ", foo )
    # print( "bar = ", bar )
    # del mySource.file_name             # deleter called

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:class II $ python book_delta.py
# setter of _file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# setter of _file_name called: self._file_name =  short.rst
# uuid = 174f8440-5e59-4710-9272-3db669e832ba
#
#  2018-12-03 20:12:42.908499
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II/book_delta.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
