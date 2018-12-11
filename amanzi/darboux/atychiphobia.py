#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# # imports
import datetime             # timestamps
import os                   # opeating system
import sys                  # python version
from pathlib import Path    # rename file
import xlsxwriter           # API for Excel
# home brew
# classes
#import cls_Book             # Book (constains chapters, contains requirements)
#import cls_Chapter          # chapter (constains sections, contains requirements)
import cls_Source            # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    source = cls_Source.Source( ) # instantiate
    source.input_rst = "short.rst"    # setter called
    #mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    source.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called

    source.setup_io( )
    source.read_file( )

    # # # start the book
    # myBook = cls_Book.Book( ) # instantiate
    # myBook.source_object = mySource
    #
    # # open Excel file for results and intermediate data
    # myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )
    #
    # # compile lists of target locations
    # myBook.source_object.read_file( )
    # myBook.mark_chapters( )
    # # worksheets for debugging
    # tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    # tools_debug.xl_numbered_lines( myWorkbook, mySource.myLines )
    #
    # # write workbook
    # myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:darboux $ python atychiphobia.py
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst

#  2018-12-10 18:35:19.791441
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/darboux/atychiphobia.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Atychiphobia	Fear of failure
