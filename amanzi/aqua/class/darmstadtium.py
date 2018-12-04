#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# # imports
import datetime             # timestamps
import os                   # opeating system
import sys                  # python version
import uuid                 # Universal Unique IDentifier
from pathlib import Path    # rename file
# home brew
import cls_Book             # Book (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
import tools_xl             # spreadsheet authoring tools
import xlsxwriter   # API for Excel

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    mySource = cls_Source_file.Source_file( ) # instantiate
    mySource.file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/"    # setter called
    mySource.file_name = "short.rst"    # setter called
    mySource.path_name = mySource.file_path + mySource.file_name # setter called
    mySource.output_xl = Path( mySource.file_name ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    print( "mySource.output_xl = ", mySource.output_xl )

    myBook = cls_Book.Book( ) # instantiate
    myBook.file_name = mySource.file_path + mySource.file_name
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    myBook = cls_Book.Book( ) # instantiate
    myBook.source_file = mySource
    print( "myBook.source_file.file_name = %s" % myBook.source_file.file_name )
    print( "myBook.source_file.output_xl = %s" % myBook.source_file.output_xl )
    print( "myBook.source_file.output_xl = ",    myBook.source_file.output_xl )

    my_workbook = xlsxwriter.Workbook( mySource.file_path + "test.xlsx" )
    my_workbook.close( )
    # print( "open Excel file for output" )
    # tools_xl.xl_new_workbook( "delete.xlsx" )
    #tools_xl.xl_new_workbook( mySource.output_xl )
    #tools_xl.xl_new_workbook( myBook.source_file.output_xl )

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
