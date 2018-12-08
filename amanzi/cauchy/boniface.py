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

# dantopa@Lax-Millgram:cauchy $ py boniface.py
# reading source file /Users/dantopa/Documents/repos/GitHub/topa-development/data/short.rst
# myChapter = <cls_Chapter.Chapter object at 0x106ade3c8>
# myChapter = <cls_Chapter.Chapter object at 0x106ade2e8>
# myChapter = <cls_Chapter.Chapter object at 0x106b58c88>
# myChapter = <cls_Chapter.Chapter object at 0x106b58e48>
# number of chapters = 4
# 1. start_locations = [16, 32, 95]
# 2. start_locations = [15, 31, 94]
# chapter 1: Overview
# first, last: 7, 15
# chapter 2: Amanzi Input
# first, last: 16, 31
# chapter 3: Model Description
# first, last: 32, 94
# chapter 4: Definitions
# first, last: 95, 231

#  2018-12-08 11:52:11.316267
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/boniface.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]


# Pope Boniface I (Latin: Bonifatius I; died 4 September 422) was Pope from
# 28 December 418 to his death in 422. His election was disputed by the supporters
# of Eulalius, until the dispute was settled by the Emperor. Boniface was active
# maintaining church discipline and he restored certain privileges to the
# metropolitical sees of Narbonne and Vienne, exempting them from any subjection
# to the primacy of Arles.
