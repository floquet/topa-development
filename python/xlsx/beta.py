#! /Volumes/Tlaltecuhtli/local/anaconda/anaconda3/bin/python

# # Write to Excel worksheet

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

# # imports
import os           # probe, change directories
import sys          # python version
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
import xlsxwriter   # API for Excel

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook( "Amanzi Requirements.xlsx" )
worksheet = workbook.add_worksheet( "provenance" )

# Write some simple text.
worksheet.set_column( "A:A", 15 )

worksheet.write( "A1", "python source" )
worksheet.write( "B1", os.path.basename( __file__ ) )

worksheet.write( "A2", "directory" )
worksheet.write( "B2", os.getcwd( ) )

worksheet.write( "A3", "python version" )
worksheet.write( "B3", sys.version )

row = 4
worksheet.write( row, 0, "Environment variables" )
row += 1
worksheet.write( row, 0, "$USER" )
worksheet.write( row, 1, os.environ[ "USER" ] )
row += 1
worksheet.write( row, 0, "$HOSTNAME" )
worksheet.write( row, 1, os.environ[ "HOSTNAME" ] )
row += 1
worksheet.write( row, 0, "$HOME" )
worksheet.write( row, 1, os.environ[ "HOME" ] )
row += 2
worksheet.write( row, 0, "timestamp" )
worksheet.write( row, 1, datetime.datetime.now( ) )
# cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
# worksheet.add_format( row, 1, cell_format )

workbook.close()
