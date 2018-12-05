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
    # mySource.file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
    mySource.file_path = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"    # setter called
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

# dantopa@Lax-Millgram:class $ mypy europium.py
# setter of _input_rst called: self._input_rst =  short.rst
# b
# getter of file_name called: self._input_rst =  short.rst
# setter of _path_rst called: self._full_rst =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# getter of file_path called: self._full_rst =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# mySource.path_name =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# getter of file_name called: self._input_rst =  short.rst
# c
# setter of _file_name called: self._source_object =  <cls_Source_file.Source_file object at 0x10feb94a8>
# getter of file_path called: self._output_xl =  short.xlsx
# getter of file_path called: self._output_xl =  short.xlsx
# created  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.xlsx
# getter of file_path called: self._full_rst =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# mySource.path_name =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# getter of file_path called: self._full_rst =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# # # # mySource.path_name =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# getter of file_path called: self._full_rst =  /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# reading file /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/data/short.rst
# 231 lines found
#
#  2018-12-04 20:29:35.635061
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/class/europium.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
