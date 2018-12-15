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
    mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    # mySource.path_rst = "/Volumes/Tethys/repos/GitHub/topa-development/data/"
    # mySource.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called

    # read source file
    mySource.setup_io( )
    mySource.read_file( )
    print( "length col_lines = %s" % len( mySource.col_lines ) )
    # mark candidate elements
    ( l_reqd, l_optl ) = mySource.search_elements_crude( )
    # harvest optional elements
    myflavor = "optional";
    Qreqd = "OPTL"
    all_elements = mySource.search_elements_refine( l_optl, myflavor )
    #print( "elements = {}".format( elements ) )
    count = 0
    for elist in all_elements:
        for t in elist:
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
#
# Element attributes:
# name = comment
# flavor = OPTL
# status = NULL
# k_index = 1
# uuid = b3eedc01-b2c2-427a-bfee-edf6db9cfdc5
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = author
# flavor = OPTL
# status = NULL
# k_index = 2
# uuid = 99efae96-eb55-4399-8b9c-9d4ae8a84159
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = created
# flavor = OPTL
# status = NULL
# k_index = 3
# uuid = 4588b7dc-6e01-4556-887f-60ad829b7060
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = modified
# flavor = OPTL
# status = NULL
# k_index = 4
# uuid = c5f65d3b-2583-4b85-b6bf-82f71eeb1397
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = model_id
# flavor = OPTL
# status = NULL
# k_index = 5
# uuid = b425e017-cad1-473e-a99b-f38f85b5d3fd
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = description
# flavor = OPTL
# status = NULL
# k_index = 6
# uuid = fd78533e-7350-4bbe-9d84-e612f8e40673
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = purpose
# flavor = OPTL
# status = NULL
# k_index = 7
# uuid = aca89323-ff30-45af-afc7-06fc5829926d
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = units
# flavor = OPTL
# status = NULL
# k_index = 8
# uuid = b2046214-4a45-41d2-81c7-425a90a3f629
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = length_unit
# flavor = OPTL
# status = NULL
# k_index = 9
# uuid = 805f5dc0-7c82-4939-a76d-f9e3613c5268
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = time_unit
# flavor = OPTL
# status = NULL
# k_index = 10
# uuid = 4ecd25d4-5826-44fa-81d3-1deb6eaf989a
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = mass_unit
# flavor = OPTL
# status = NULL
# k_index = 11
# uuid = 9ea668db-0420-498e-8c6c-2bbad81156a1
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = conc_unit
# flavor = OPTL
# status = NULL
# k_index = 12
# uuid = 7cdad8c9-1c2d-4432-80db-893028be54cb
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = constants
# flavor = OPTL
# status = NULL
# k_index = 13
# uuid = 4aa75565-4086-45b2-8ea6-f401a2286f8b
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = macros
# flavor = OPTL
# status = NULL
# k_index = 14
# uuid = 597cd734-da20-4cd9-ae81-f54c2929d567
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = constant
# flavor = OPTL
# status = NULL
# k_index = 15
# uuid = 4cf054f4-2f1c-43c1-822d-9cd7bcae5e2d
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = time_constant
# flavor = OPTL
# status = NULL
# k_index = 16
# uuid = 3f54219d-6936-477d-a317-383c0718c561
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = numerical_constant
# flavor = OPTL
# status = NULL
# k_index = 17
# uuid = 65eed8ac-4c3f-491e-a595-8b9567103bf6
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = area_mass_flux_constant
# flavor = OPTL
# status = NULL
# k_index = 18
# uuid = c439e663-6b95-404d-b970-e2d2e5e6cbb6
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = time_macro
# flavor = OPTL
# status = NULL
# k_index = 19
# uuid = b511ceab-b22f-473f-a7de-82b278527b33
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = cycle_macro
# flavor = OPTL
# status = NULL
# k_index = 20
# uuid = bf7955c2-b393-42fb-87be-33aad0322c6a
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
# Element attributes:
# name = variable_macro
# flavor = OPTL
# status = NULL
# k_index = 21
# uuid = da8f878c-f2d2-4bd3-bd6c-223e5e7a9c95
# k_line = None
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
#  2018-12-12 19:58:47.541296
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/darboux/domatophobia.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Domatophobia	Fear of houses
