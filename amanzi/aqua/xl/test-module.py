#! /usr/bin/python
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # imports
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import echo     # xl routines

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

# #    # #    # #    # #    # #    # #

if __name__ == "__main__":

    workbook_title = "test.xlsx"
    myWorkbook = echo.xl_new_workbook( workbook_title )
    # xl_sheet_new_chapter( myWorkbook, chapter_details )
    myWorkbook.close( )

    print( datetime.datetime.now( ) )
