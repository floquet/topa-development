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
# in parse_alpha
# locations = [1, 3, 9, 18, 34, 97]
# header found in line 7: Overview
# header found in line 16: Amanzi Input
# header found in line 32: Model Description
# header found in line 95: Definitions
# ( loc, txt ) = [7, 16, 32, 95]['Overview', 'Amanzi Input', 'Model Description', 'Definitions']
# ( loc, txt ) = ([7, 16, 32, 95], ['Overview', 'Amanzi Input', 'Model Description', 'Definitions'])
# ( myLoc, myTxt ) = 7, Overview
# ( myLoc, myTxt ) = 16, Amanzi Input
# ( myLoc, myTxt ) = 32, Model Description
# ( myLoc, myTxt ) = 95, Definitions

#  2018-12-08 10:54:59.515954
# source: /Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/agatho.py
# python version 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]


# Pope Agatho (died January 681) served as the Pope from 27 June 678 until his death in 681.
# He heard the appeal of Wilfrid of York, who had been displaced from his See by the division
# of the Archdiocese ordered by Theodore of Canterbury. During Agatho's tenure, the
# Sixth Ecumenical Council was convened which dealt with the monothelitism controversy. He is
# venerated as a saint by both the Catholic and Eastern Orthodox Churches.
