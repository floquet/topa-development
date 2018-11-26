#! /Volumes/Tlaltecuhtli/local/anaconda/anaconda3/bin/python

# # Write to Excel worksheet

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

# # # References
# Example: Adding Headers and Footers to Worksheets
# # https://xlsxwriter.readthedocs.io/example_headers_footers.html
# The Worksheet Class (Page Setup)
# # https://xlsxwriter.readthedocs.io/page_setup.html

# # imports
# import os           # probe, change directories
# import sys          # python version
# import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import xlsxwriter   # API for Excel

workbook_title = "workseet-tester.xlsx"
workbook_object = xlsxwriter.Workbook( workbook_title )
print( "\nopened workbook ", workbook_title )

worksheet_title = "my worksheet"
worksheet_object = workbook_object.add_worksheet( worksheet_title )
print( "\nopened worksheet ", worksheet_title )

myheader = "&C&12&A" # fontsize 12
myfooter = "&L&8&T\n&8&D" + "&C &P / &N" + "&R&8&Z\n&8&F" # fontsize 8
worksheet_object.set_header( myheader )
worksheet_object.set_footer( myfooter )

workbook_object.close( )
