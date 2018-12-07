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
import cls_Chapter          # Book (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
#import tools_parse          # file parsing tools
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    mySource = cls_Source_file.Source_file( ) # instantiate
    print( "mySource.uuid = %s" % mySource.uuid )
    mySource.input_rst = "short.rst"    # setter called
    #mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    mySource.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
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
    myLines = mySource.parse_master( )
    # worksheets for debugging
    tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    tools_debug.xl_numbered_lines( myWorkbook, myLines )

    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:cauchy $ python agatho.py
# mySource.uuid = c873eacd-62a0-4c5a-9e35-f1e17111ced3
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# 231 lines found
# 16 xml blocks found; locations [28, 38, 56, 81, 101, 113, 122, 128, 134, 140, 149, 162, 170, 185, 198, 207]
# 2 header0 '===' candidates found; locations [34, 97]
# 3 header1 '---' candidates found; locations [48, 109, 145]
# 3 header2 '___' candidates found; locations [158, 180, 194]
# header found in line 32: Model Description
# header found in line 95: Definitions
# header found in line 46: Units
# header found in line 107: Constants
# header found in line 143: Macros
# header found in line 156: Time_macro
# header found in line 178: Cycle_macro
# header found in line 192: Variable_macro
#
#  2018-12-06 17:13:07.349708
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/cauchy/agatho.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]


# Pope Agatho (died January 681) served as the Pope from 27 June 678 until his death in 681.
# He heard the appeal of Wilfrid of York, who had been displaced from his See by the division
# of the Archdiocese ordered by Theodore of Canterbury. During Agatho's tenure, the
# Sixth Ecumenical Council was convened which dealt with the monothelitism controversy. He is
# venerated as a saint by both the Catholic and Eastern Orthodox Churches.
