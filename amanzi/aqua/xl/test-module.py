#! /usr/bin/python
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # imports
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import class_book   # class definitions
import tools_xl     # xl routines

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# #    # #    # #    # #    # #    # #

if __name__ == "__main__":

    workbook_title = "test.xlsx"
    myWorkbook = echo.xl_new_workbook( workbook_title )
    # xl_sheet_new_chapter( myWorkbook, chapter_details )

    # #    # #    # #    # #    # #    # #  Fake a chapter
    # create sections
    count_section = 1
    sec_bc_assigned_region = class_book.Section( 1, "assigned_region", count_section ); count_section +=1
    sec_bc_liquid_phase    = class_book.Section( 1, "liquid_phase",    count_section ); count_section +=1
    sec_bc_solid_phase     = class_book.Section( 1, "solid_phase",     count_section ); count_section +=1
    # create chapter
    chap_bc = class_book.Chapter( 8, "Boundary Conditions", "BC",
                [ sec_bc_assigned_region, sec_bc_liquid_phase, sec_bc_solid_phase] )

    print( "chap_bc.chap_num: ",        chap_bc.chap_num )
    print( "chap_bc.chap_title: ",      chap_bc.chap_title )
    print( "chap_bc.chap_key: ",        chap_bc.chap_key )
    print( "chap_bc.chap_sections: ",   chap_bc.chap_sections )

    # #    # #    # #    # #    # #    # #  Create worksheet
    mySheet = echo.xl_sheet_generate( chap_bc.key )

    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    for sec in chap_bc.chap_sections:
        print( "section = ", sec )

    myWorkbook.close( )


    print( datetime.datetime.now( ) )
