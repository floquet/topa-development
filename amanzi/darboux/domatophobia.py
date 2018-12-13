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
import cls_Chapter          # chapter (constains sections)
import cls_Element          # elements (required, optional)
import cls_Source           # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # fundamental object: a book
    book = cls_Book.Book( ) # instantiate book
    book.source = cls_Source.Source( ) # instantiate source
    mySource = book.source

    # # source data
    mySource.input_rst = "short.rst"    # setter called
    # mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    # mySource.path_rst = "/Volumes/Tethys/repos/GitHub/topa-development/data/"
    mySource.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called

    # read source file
    mySource.setup_io( )
    mySource.read_file( )
    print( "length col_lines = %s" % len( mySource.col_lines ) )
    # mark candidate elements
    ( l_reqd, l_optl ) = mySource.search_elements_crude( )
    # harvest optional elements
    myflavor = "optional";
    Qreqd = "OPTL"
    elements = mySource.search_elements_refine( l_optl, myflavor )
    print( "elements = {}".format( elements ) )
    count = 0
    for t in elements: # titles
        e = cls_Element.Element( )
        count += 1
        e.name = t
        e.flavor = Qreqd
        e.status = "NULL"
        e.k_index = count
        book.col_elements.append( e )
    for k in range( 0, count ):
        book.col_elements[ k ].print_element( )


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

# l127914@pn1249300.lanl.gov:darboux $ python domatophobia.py
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# length col_lines = 231
# looking for optional elements
# line 42 = comment, author, created, modified, model_id, description, purpose, units
# line 60 = length_unit, time_unit, mass_unit, conc_unit
# line 105 = constants, macros
# line 117 = constant, time_constant, numerical_constant, area_mass_flux_constant
# line 153 = time_macro, cycle_macro, variable_macro
# elements = ['time_macro', 'cycle_macro', 'variable_macro']

# Element attributes:
# name = time_macro
# flavor = OPTL
# status = NULL
# k_index = 1
# uuid = 837c9d47-321c-457b-9afa-2f5cf5c0dc44
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None

# Element attributes:
# name = cycle_macro
# flavor = OPTL
# status = NULL
# k_index = 2
# uuid = a4cbb4e0-9aaf-4c88-83f9-8b9583cf0853
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None

# Element attributes:
# name = variable_macro
# flavor = OPTL
# status = NULL
# k_index = 3
# uuid = 4af71765-2c14-4a7e-b6f3-035303bf39dc
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None

#  2018-12-12 19:45:01.022169
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/darboux/domatophobia.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Domatophobia	Fear of houses
