#! /usr/bin/python
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # imports
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import class_book   # class definitions
import tools_xl     # xl routines

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    workbook_title = "test.xlsx"
    myWorkbook = tools_xl.xl_new_workbook( workbook_title )
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

    # #    # #    # #    # #    # #    # #  Create worksheet
    mySheet = tools_xl.xl_sheet_generate( myWorkbook, chap_bc.chap_key ) # 08-BC
    mySheet.set_column( "A:A", 18.5 ) # column width
    # cell indices
    row = 0 # make relative jumps in rows
    col = 0
    col_key = 0 # column for posting keys
    mySheet.write( row, col, chap_bc.chap_ego ) # # 08-Boundary Conditions

    row += 2
    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops

    for sec in chap_bc.chap_sections:
        print( "section = ", sec )
        print( "section title = ", sec.title )
        myKey = chap_bc.chap_key + "." + sec.sec_key
        mySheet.write( row, col_key, myKey  ) # # 08-BC.S01-01

    myWorkbook.close( )

    print( datetime.datetime.now( ) )
