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
import xlsxwriter           # API for Excel
# home brew
import cls_Book             # Book (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
import tools_parse          # file parsing tools
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    mySource = cls_Source_file.Source_file( ) # instantiate
    mySource.file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/"    # setter called
    mySource.file_name = "short.rst"    # setter called
    print( "b" )
    mySource.path_name = mySource.file_path + mySource.file_name # setter called
    print( "mySource.path_name = ", mySource.path_name )
    # # output file
    mySource.output_xl = Path( mySource.file_name ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    print( "c" )

    myBook = cls_Book.Book( ) # instantiate
    myBook.source_object = mySource
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    # print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    my_workbook = tools_xl.xl_new_workbook( mySource.file_path + mySource.output_xl )
    print( "created ", mySource.file_path + mySource.output_xl )
    print( "mySource.path_name = ", mySource.path_name )
    print( "# # # mySource.path_name = ", mySource.path_name )
    ( numLines, myLines ) = tools_parse.reader( mySource.path_name ) # read file as split lines
    my_workbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:class $ python darmstadtium.py
# setter of _file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# setter of _file_name called: self._file_name =  short.rst
# getter of file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# getter of file_name called: self._file_name =  short.rst
# getter of file_name called: self._file_name =  short.rst
# getter of file_path called: self._title =  short.xlsx
# mySource.output_xl =  short.xlsx
# getter of file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/
# getter of file_name called: self._file_name =  short.rst
# uuid = 3050d2bf-592d-477b-96ca-b07d6d3f9c75
# setter of _file_name called: self._source_file =  <cls_Source_file.Source_file object at 0x1081163c8>
# getter of source_file called: self._source_file =  <cls_Source_file.Source_file object at 0x1081163c8>
# getter of file_name called: self._file_name =  short.rst
# myBook.source_file.file_name = short.rst
# getter of source_file called: self._source_file =  <cls_Source_file.Source_file object at 0x1081163c8>
# getter of file_path called: self._title =  short.xlsx
# myBook.source_file.output_xl = short.xlsx
# getter of source_file called: self._source_file =  <cls_Source_file.Source_file object at 0x1081163c8>
# getter of file_path called: self._title =  short.xlsx
# myBook.source_file.output_xl =  short.xlsx
# getter of file_path called: self._file_path =  /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/data/

#  2018-12-04 10:45:22.931138
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/aqua/class/darmstadtium.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
