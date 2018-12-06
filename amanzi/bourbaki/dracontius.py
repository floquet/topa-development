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
    print( "mySource.uuid = %s" % mySource.uuid )
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

    # first read rst
    myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )
    ( numLines, myLines ) = tools_parse.reader( mySource.path_name ) # read file as split lines
    myBook.source_object.title = myLines[ 1 ] # harvest title line
    myBook.source_object.numLines = numLines
    # worksheets for debugging
    tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    tools_debug.xl_numbered_lines( myWorkbook, myLines )

    # continue parsing - compile lists of target locations
    # ( loc_xml, loc_candidate_header0, loc_candidate_header1, loc_candidate_header2 ) = mySource.parse_candidates( myLines )  # first parse: candidate headers
    # mySource.parse_match_lengths( myLines, loc_candidate_header0 )
    # mySource.parse_match_lengths( myLines, loc_candidate_header1 )
    # mySource.parse_match_lengths( myLines, loc_candidate_header2 )
    mySource.parse_master( myLines )

    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:bourbaki $ python catullus.py
# mySource.uuid = 0a4eeab3-44ce-4332-93a6-592c0e243dd3
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

#  2018-12-06 15:08:15.943395
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki/catullus.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Blossius Aemilius Dracontius (c. 455 – c. 505) of Carthage was a Christian poet who flourished in the
# latter part of the 5th century. He belonged to a family of land proprietors, and practiced as an
# advocate in his native place. After the conquest of the country by the Vandals, Dracontius was at
# first allowed to retain possession of his estates, but was subsequently deprived of his property
# and thrown into prison by the Vandal king, whose triumphs he had omitted to celebrate, while he had
# written a panegyric on a foreign and hostile ruler. He subsequently addressed an elegiac poem to the
# king, asking pardon, and pleading for release.
