#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
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
# classes
import cls_Book             # Book (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
import tools_parse          # file parsing tools
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    mySource = cls_Source_file.Source_file( ) # instantiate
    mySource.input_rst = "short.rst"    # setter called
    #mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    mySource.path_rst = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
    mySource.full_rst  = mySource.path_rst + mySource.input_rst

    # # output file
    mySource.output_xl = Path( mySource.input_rst ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    mySource.path_xl   = mySource.path_rst
    mySource.full_xl   = mySource.path_xl + mySource.output_xl

    # # start the book
    myBook = cls_Book.Book( ) # instantiate
    myBook.source_object = mySource
    # https://docs.python.org/3/library/uuid.html
    # uuid4: random - more secure
    # print( "uuid = %s" % uuid.uuid4( ) ) # https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

    # first read rst
    myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )
    ( numLines, myLines ) = tools_parse.reader( mySource.path_name ) # read file as split lines
    myBook.source_object.title = myLines[ 1 ] # harvest title line
    print( myLines[ 0 ] )
    myBook.source_object.numLines = numLines
    # worksheets for debugging
    tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    tools_debug.xl_numbered_lines( myWorkbook, myLines )

    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:bourbaki $ python bavius.py
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# 231 lines found
# ====================================================
# 
#  2018-12-06 10:28:50.801701
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki/bavius.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Bavius and Maevius (or Mevius) were two poets in the age of Augustus Caesar,
# whose names became synonymous with bad verse and malicious criticism of superior writers.
