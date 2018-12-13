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
    ( l_reqd, l_optl ) = mySource.search_elements_crude( )
    elements = mySource.search_elements_refine( l_optl, "optional" )
    with e in elements:
        book.col_elements


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
# elements = ['comment', 'author', 'created', 'modified', 'model_id', 'description', 'purpose', 'units']
# line 60 = length_unit, time_unit, mass_unit, conc_unit
# elements = ['length_unit', 'time_unit', 'mass_unit', 'conc_unit']
# line 105 = constants, macros
# elements = ['constants', 'macros']
# line 117 = constant, time_constant, numerical_constant, area_mass_flux_constant
# elements = ['constant', 'time_constant', 'numerical_constant', 'area_mass_flux_constant']
# line 153 = time_macro, cycle_macro, variable_macro
# elements = ['time_macro', 'cycle_macro', 'variable_macro']

#  2018-12-12 18:05:50.840657
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/darboux/domatophobia.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]

# Domatophobia	Fear of houses
