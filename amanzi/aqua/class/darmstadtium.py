#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

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

    myBook = cls_Book.Book( ) # instantiate
    myBook.file_name = mySource.file_path + mySource.file_name
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    myBook = cls_Book.Book( ) # instantiate
    myBook.source_file = mySource
    print( "myBook.source_file.file_name = %s" % myBook.source_file.file_name )
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

# l127914@pn1249300.lanl.gov:class $ python darmstadtium.py
# setter of _file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# setter of _file_name called: self._file_name =  short.rst
# getter of file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# getter of file_name called: self._file_name =  short.rst
# setter of _file_name called: self._file_name =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/short.rst
# uuid = 5dc86d74-1865-4e05-9f58-6e174a26ac03
# getter of file_name called: self._file_name =  short.rst
# myBook.source_file.file_name = short.rst

#  2018-12-04 09:51:44.149161
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/class/darmstadtium.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
