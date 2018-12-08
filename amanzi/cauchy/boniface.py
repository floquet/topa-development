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
import cls_Book             # Book (constains chapters, contains requirements)
import cls_Chapter          # chapter (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    mySource = cls_Source_file.Source_file( ) # instantiate
    mySource.input_rst = "short.rst"    # setter called
    mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    #mySource.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
    mySource.full_rst  = mySource.path_rst + mySource.input_rst

    # # output file
    mySource.output_xl = Path( mySource.input_rst ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    mySource.path_xl   = mySource.path_rst
    mySource.full_xl   = mySource.path_xl + mySource.output_xl

    # # start the book
    myBook = cls_Book.Book( ) # instantiate
    myBook.source_object = mySource

    # open Excel file for results and intermediate data
    myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )

    # compile lists of target locations
    myBook.source_object.read_file( )
    myBook.mark_chapters( )
    # worksheets for debugging
    tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    tools_debug.xl_numbered_lines( myWorkbook, mySource.myLines )

    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# dantopa@Lax-Millgram:cauchy $ py agatho.py
# reading source file /Users/dantopa/Documents/repos/GitHub/topa-development/data/short.rst
# myChapter = <cls_Chapter.Chapter object at 0x101a26198>
# myChapter = <cls_Chapter.Chapter object at 0x101a261d0>
# myChapter = <cls_Chapter.Chapter object at 0x101a4ca20>
# myChapter = <cls_Chapter.Chapter object at 0x101a4cba8>
# number of chapters = 4

#  2018-12-08 11:29:40.616303
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/agatho.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]

#  2018-12-08 10:54:59.515954
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/agatho.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]


# Pope Boniface I (Latin: Bonifatius I; died 4 September 422) was Pope from
# 28 December 418 to his death in 422. His election was disputed by the supporters
# of Eulalius, until the dispute was settled by the Emperor. Boniface was active
# maintaining church discipline and he restored certain privileges to the
# metropolitical sees of Narbonne and Vienne, exempting them from any subjection
# to the primacy of Arles.
