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
#import cls_Element          # elements (required, optional)
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
    for e in book.col_chapters:
        # mark candidate elements
        ( l_reqd, l_optl ) = mySource.search_elements_crude( e.k_start, e.k_stop )
        e.print_element( )
    
    # harvest optional elements
    all_elements = mySource.search_elements_refine( l_optl, "optional", book )
    all_elements = mySource.search_elements_refine( l_reqd, "required", book )
    # for e in book.col_elements:
    #     e.print_element( )


    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

#dantopa@Mittag-Leffler.local:darboux $ python elurophobia.py 
#reading source file /Volumes/Tethys/repos/GitHub/topa-development/data/short.rst
#length col_lines = 231
#line 0: ====================================================
#line 2: ====================================================
#line 8: ========
#line 17: ============
#line 33: =================
#line 96: ===========
#in: locations, text = [], []
#lineNum = 0
#A = ====================================================
#B =   </definitions>
#lineNum = 2
#A = ====================================================
#B = Amanzi XML Input Specification (Version 2.3-draft)
#lineNum = 8
#A = ========
#B = Overview
#lineNum = 17
#A = ============
#B = Amanzi Input
#lineNum = 33
#A = =================
#B = Model Description
#lineNum = 96
#A = ===========
#B = Definitions
#out: locations, text = [9, 18, 34, 97], ['Overview', 'Amanzi Input', 'Model Description', 'Definitions']
#myChapter = <cls_Chapter.Chapter object at 0x101b4aa20>
#myChapter = <cls_Chapter.Chapter object at 0x101b4a9b0>
#myChapter = <cls_Chapter.Chapter object at 0x101597048>
#myChapter = <cls_Chapter.Chapter object at 0x1015970b8>
#number of chapters = 4
#1. start_locations = [18, 34, 97]
#2. start_locations = [15, 31, 94]
#chapter 1: Overview
#first, last: 9, 15
#chapter 2: Amanzi Input
#first, last: 18, 31
#chapter 3: Model Description
#first, last: 34, 94
#chapter 4: Definitions
#first, last: 97, 231
#looking for optional elements
#line 42 = comment, author, created, modified, model_id, description, purpose, units
#line 60 = length_unit, time_unit, mass_unit, conc_unit
#line 105 = constants, macros
#line 117 = constant, time_constant, numerical_constant, area_mass_flux_constant
#line 153 = time_macro, cycle_macro, variable_macro 
#looking for required elements
#
#Element attributes:
#name = comment
#flavor = OPTL
#status = NULL
#k_index = 1
#uuid = 1ebd1b22-9ad9-4bb6-9595-5206fba528aa
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  author
#flavor = OPTL
#status = NULL
#k_index = 2
#uuid = c2baa677-2cb3-449f-a62c-e0421e80b93d
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  created
#flavor = OPTL
#status = NULL
#k_index = 3
#uuid = d2f1344e-b935-43ed-874e-c7063f75976c
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  modified
#flavor = OPTL
#status = NULL
#k_index = 4
#uuid = 6c91611c-2a97-4e96-be80-73b9a9970717
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  model_id
#flavor = OPTL
#status = NULL
#k_index = 5
#uuid = 84fc5e58-3093-4517-97cb-61f9b9560633
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  description
#flavor = OPTL
#status = NULL
#k_index = 6
#uuid = c4bae123-31b2-4c33-9a0f-18978b901491
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  purpose
#flavor = OPTL
#status = NULL
#k_index = 7
#uuid = 01a72576-a36d-4b97-ba75-718a6d42338e
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  units
#flavor = OPTL
#status = NULL
#k_index = 8
#uuid = 908256f2-ad8b-4d97-80bd-0a3dfe90ff27
#k_line = 42
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name = length_unit
#flavor = OPTL
#status = NULL
#k_index = 9
#uuid = d9381f22-e53c-4f38-b39d-4e4e92688a38
#k_line = 60
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  time_unit
#flavor = OPTL
#status = NULL
#k_index = 10
#uuid = cf72132c-9cdc-4370-b4fe-dfe4c4453338
#k_line = 60
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  mass_unit
#flavor = OPTL
#status = NULL
#k_index = 11
#uuid = be81a551-b067-4907-86ac-1a9cfdd315ce
#k_line = 60
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  conc_unit
#flavor = OPTL
#status = NULL
#k_index = 12
#uuid = 966a8d0d-d141-4f3d-b980-a66de766acb8
#k_line = 60
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name = constants
#flavor = OPTL
#status = NULL
#k_index = 13
#uuid = f350a4ba-65af-48c0-80a2-a07c7ee6beac
#k_line = 105
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  macros
#flavor = OPTL
#status = NULL
#k_index = 14
#uuid = 6777a7e4-ce5e-411c-ba9b-95de33be822b
#k_line = 105
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name = constant
#flavor = OPTL
#status = NULL
#k_index = 15
#uuid = 4cc4fc8a-4611-49c6-9a8e-ea17391dcf80
#k_line = 117
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  time_constant
#flavor = OPTL
#status = NULL
#k_index = 16
#uuid = b27725a0-8522-454b-99ac-abe8c605dee1
#k_line = 117
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  numerical_constant
#flavor = OPTL
#status = NULL
#k_index = 17
#uuid = 21587f9f-dbf4-4363-a2b1-d969b64ed2f1
#k_line = 117
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  area_mass_flux_constant
#flavor = OPTL
#status = NULL
#k_index = 18
#uuid = f4550d05-64c3-4ef3-b8bf-c47bb42bcbe5
#k_line = 117
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name = time_macro
#flavor = OPTL
#status = NULL
#k_index = 19
#uuid = d481c98c-32c5-4042-a135-e274873f9095
#k_line = 153
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  cycle_macro
#flavor = OPTL
#status = NULL
#k_index = 20
#uuid = c9708125-91d9-4169-9fa5-9fe5769d9487
#k_line = 153
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
#Element attributes:
#name =  variable_macro 
#flavor = OPTL
#status = NULL
#k_index = 21
#uuid = be484b5f-549c-42dd-a724-8257cc98b305
#k_line = 153
#key_head = None
#key_tail = None
#k_chapter = None
#k_section = None
#k_subsection = None
#xl_row = None
#xl_col = None
#
# 2018-12-18 19:23:46.676378
#source: /Volumes/Tethys/repos/GitHub/topa-development/amanzi/darboux/elurophobia.py
#python version 3.6.7 (default, Oct 21 2018, 08:02:39) 
#[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]


# Elurophobia	Fear of cats
