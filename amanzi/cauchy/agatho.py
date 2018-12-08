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
    print( "mySource.uuid = %s" % mySource.uuid )
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
    # mySource.parse_master( )
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
# mySource.uuid = b61d3c57-5c6c-49eb-9383-ecd9255c0f89
# self.source_object.parse_alpha
# in parse_alpha
# self.myLines = None
# Traceback (most recent call last):
#   File "agatho.py", line 48, in <module>
#     myBook.mark_chapters( )
#   File "/Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/cls_Book.py", line 67, in mark_chapters
#     locations = self.source_object.parse_alpha( "===" )
#   File "/Users/dantopa/Documents/repos/GitHub/topa-development/amanzi/cauchy/cls_Source_file.py", line 254, in parse_alpha
#     for line in self.myLines:
# TypeError: 'NoneType' object is not iterable


# Pope Agatho (died January 681) served as the Pope from 27 June 678 until his death in 681.
# He heard the appeal of Wilfrid of York, who had been displaced from his See by the division
# of the Archdiocese ordered by Theodore of Canterbury. During Agatho's tenure, the
# Sixth Ecumenical Council was convened which dealt with the monothelitism controversy. He is
# venerated as a saint by both the Catholic and Eastern Orthodox Churches.
