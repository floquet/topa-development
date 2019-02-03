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
    mySource.input_rst = "short.rst"    # setter called
    mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    print( "mySource.path_rst = %s" % mySource.path_rst )
    # mySource.file_path = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
    mySource.full_rst  = mySource.path_rst + mySource.input_rst

    # # output file
    mySource.output_xl = Path( mySource.input_rst ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    mySource.path_xl   = mySource.path_rst
    mySource.full_xl   = mySource.path_xl + mySource.output_xl

    myBook = cls_Book.Book( ) # instantiate
    myBook.source_object = mySource
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    # print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )
    # print( "created ", mySource.file_path + mySource.output_xl )
    # print( "mySource.path_name = ", mySource.path_name )
    # print( "# # # mySource.path_name = ", mySource.path_name )
    ( numLines, myLines ) = tools_parse.reader( mySource.path_name ) # read file as split lines
    myBook.source_object.numLines = numLines
    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# dantopa@Lax-Millgram:bourbaki $ mypy ausonius.py
# mySource.path_rst = /Users/dantopa/Documents/repos/GitHub/topa-development/data/
# reading source file /Users/dantopa/Documents/repos/GitHub/topa-development/data/short.rst
# 231 lines found

#  2018-12-04 21:22:59.007407
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/bourbaki/ausonius.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]

#  Decimus or Decimius Magnus Ausonius was a Roman poet and teacher of rhetoric
# from Burdigala in Aquitaine, modern Bordeaux, France. For a time he was tutor
# to the future emperor Gratian, who afterwards bestowed the consulship on him.
# His best-known poems are Mosella, a description of the river Moselle,
# and Ephemeris, an account of a typical day in his life. 
