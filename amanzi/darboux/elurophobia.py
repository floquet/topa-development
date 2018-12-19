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
    mySource.path_rst = "/Volumes/Tethys/repos/GitHub/topa-development/data/"
    # mySource.path_rst  = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called

    # read source file
    mySource.setup_io( )
    mySource.read_file( )
    print( "length col_lines = %s" % len( mySource.col_lines ) )
    
    book.mark_chapters( )
    
    # mark candidate elements
    ( l_reqd, l_optl ) = mySource.search_elements_crude( )
    # harvest optional elements
    all_elements = mySource.search_elements_refine( l_optl, "optional", book )
    all_elements = mySource.search_elements_refine( l_reqd, "required", book )
    for e in book.col_elements:
        e.print_element( )


    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:darboux $ python elurophobia.py
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# length col_lines = 231
# looking for optional elements
# line 42 = comment, author, created, modified, model_id, description, purpose, units
# line 60 = length_unit, time_unit, mass_unit, conc_unit
# line 105 = constants, macros
# line 117 = constant, time_constant, numerical_constant, area_mass_flux_constant
# line 153 = time_macro, cycle_macro, variable_macro

# Element attributes:
# name = comment
# flavor = OPTL
# status = NULL
# k_index = 1
# uuid = 77fd213f-bccc-424b-99a3-54d92fdb2a5f
# k_line = 42
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
# uuid = 46851554-0b1f-459e-81f9-4541113314d3
# k_line = 42
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
# uuid = bbf177c2-7881-427d-a9c0-a40b9cdffec8
# k_line = 42
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
# uuid = 346bcad7-33f4-46b0-a20d-928f4c79b6c0
# k_line = 42
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
# uuid = 098b3cbd-c9a5-4a1f-932e-7fbb29d218c4
# k_line = 42
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
# uuid = c2fd4a76-641a-4ca3-93c5-b78196190659
# k_line = 42
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
# uuid = 49da8446-b262-41c6-8a2d-6198eb157d89
# k_line = 42
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
# uuid = b3ed511a-b945-4c1a-af9e-f0bc5abebd47
# k_line = 42
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
# uuid = 0db4ae1d-6f31-4714-8e39-c379fe0f40fb
# k_line = 60
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
# uuid = 20b7dc21-2392-4087-944a-14aedff865b5
# k_line = 60
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
# uuid = 9bb41610-d492-4439-93af-ccc6d9943bca
# k_line = 60
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
# uuid = 2a458e48-39ad-479e-be2d-0f50384fa1f6
# k_line = 60
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
# uuid = 77f3c157-1f91-41a9-a906-857fd9a3351f
# k_line = 105
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
# uuid = b8b5f41e-4924-452b-a1f8-7ab9f5581a6b
# k_line = 105
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
# uuid = ecbf2b15-5a8d-43be-950a-998080f3a46e
# k_line = 117
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
# uuid = f5da6e87-c1b0-4f03-b85a-6381e21a8835
# k_line = 117
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
# uuid = 3e76f870-1e09-4a3e-8cb0-3419757e302c
# k_line = 117
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
# uuid = 51b2774c-e454-4c01-8eaf-625cd11c56e0
# k_line = 117
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
# uuid = 76d64c58-fc03-4bd8-836f-f8ec8a710f7d
# k_line = 153
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
# uuid = a309717d-aa5e-4c03-af84-a769b4be4f57
# k_line = 153
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
# uuid = 1d3fd771-b5cc-4c56-85a3-81c0e1f87ded
# k_line = 153
# key_head = None
# key_tail = None
# k_chapter = None
# k_section = None
# k_subsection = None
# xl_row = None
# xl_col = None
#
#  2018-12-18 12:24:52.928932
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/darboux/elurophobia.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Elurophobia	Fear of cats
