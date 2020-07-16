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

workbook = xlsxwriter.Workbook( "Amanzi Requirements.xlsx" )

# # formats
bold = workbook.add_format({'bold': True})

chapter_number  = 8
chapter_subject = "Initial conditions"
chapter_title = str( chapter_number ) + " - " + chapter_subject

##   ##   ##  Data
worksheet = workbook.add_worksheet( chapter_title )
worksheet.set_column( "A:B", 14 )


row = 0
worksheet.write( row, 0, chapter_title, bold ); row += 2

# column locations
col_section = 0
col_key = col_section + 1
col_require = col_key + 1

## loop over sections
section_name = "assigned_regions"
worksheet.write( row, col_section, section_name ); row += 1
worksheet.write( row, col_require, "no requirements" ); row += 1

section_name = "liquid_phase"
worksheet.write( row, col_section, section_name ); row += 1
worksheet.write( row, col_key,     "08-IC.S-02.req-01" )
worksheet.write( row, col_require, "liquid_component" ); row += 1
worksheet.write( row, col_key,     "08-IC.S-02.opt-01" )
worksheet.write( row, col_require, "geochemistry_component" ); row += 1

section_name = "solid_phase"
worksheet.write( row, col_section, section_name ); row += 1
worksheet.write( row, col_key,     "08-IC.S-03.req-01" )
worksheet.write( row, col_require, "geochemisty" ); row += 1
worksheet.write( row, col_key,     "08-IC.S-03.opt-01" )
worksheet.write( row, col_require, "mineral" ); row += 1
worksheet.write( row, col_key,     "08-IC.S-03.opt-02" )
worksheet.write( row, col_require, "geochemistry" ); row += 1

##   ##   ##  provenance
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

workbook.close()
