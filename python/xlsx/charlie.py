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
bold      = workbook.add_format( {'bold': True} )
fmt_red   = workbook.add_format( {'bg_color': "#FFC7CE"} ) # https://xlsxwriter.readthedocs.io/example_conditional_format.html
fmt_green = workbook.add_format( {'bg_color': "#C6EFCE"} )
fmt_gray  = workbook.add_format( {'bg_color': "#808080"} ) # https://xlsxwriter.readthedocs.io/working_with_colors.html

# column locations
col_section = 0
col_key     = col_section + 1
col_status  = col_key + 1
col_require = col_status + 1

##  ##  chapter 8
##  ##  Initial Conditions
chapter_number  = 8
chapter_subject = "Initial conditions"
chapter_title = str( chapter_number ) + " - " + chapter_subject
key_chap = "0" + str( chapter_number ) + "-IC"

##   ##   ##  Data
worksheet = workbook.add_worksheet( chapter_title )
worksheet.set_column( "A:B", 14 )
worksheet.set_column( "C:C", 1 )  # status: green, red, gray

row = 0
worksheet.write( row, 0, chapter_title, bold ); row += 2

## loop over sections
section_number = 1
section_name = "assigned_regions"
section_entry = str( section_number ) + ". " + section_name
worksheet.write( row, col_section, section_entry ); row += 1
worksheet.write( row, col_require, "no requirements" ); row += 1

section_number += 1
section_name = "liquid_phase"
section_entry = str( section_number ) + ". " + section_name
key_sec = ".S-0" + str ( section_number )
worksheet.write( row, col_section, section_entry ); row += 1
worksheet.write( row, col_status,  "", fmt_red )
worksheet.write( row, col_key,     key_chap + key_sec + ".req-01" )
worksheet.write( row, col_status,  "", fmt_gray )
worksheet.write( row, col_require, "liquid_component" ); row += 1
worksheet.write( row, col_status,  "", fmt_green )
worksheet.write( row, col_key,     key_chap + key_sec + ".opt-01" )
worksheet.write( row, col_require, "geochemistry_component" ); row += 1

section_number += 1
section_name = "solid_phase"
section_entry = str( section_number ) + ". " + section_name
key_sec = ".S-0" + str ( section_number )
worksheet.write( row, col_section, section_entry ); row += 1
worksheet.write( row, col_status,  "", fmt_green )
worksheet.write( row, col_key,     key_chap + key_sec + ".req-01" )
worksheet.write( row, col_require, "geochemisty" ); row += 1
worksheet.write( row, col_status,  "", fmt_red )
worksheet.write( row, col_key,     key_chap + key_sec + ".opt-01" )
worksheet.write( row, col_require, "mineral" ); row += 1
worksheet.write( row, col_status,  "", fmt_gray )
worksheet.write( row, col_key,     key_chap + key_sec + ".opt-02" )
worksheet.write( row, col_require, "geochemistry" ); row += 1

##  ##  chapter 9
##  ##  Initial Conditions
chapter_number  += 1
chapter_subject = "Boundary conditions"
chapter_title = str( chapter_number ) + " - " + chapter_subject
key_chap = "0" + str( chapter_number ) + "-BC"

##   ##   ##  Data
worksheet = workbook.add_worksheet( chapter_title )
worksheet.set_column( "A:B", 14 )
worksheet.set_column( "C:C", 1 )  # status: green, red, gray

row = 0
worksheet.write( row, 0, chapter_title, bold ); row += 2

## loop over sections
section_number = 1
section_name = "assigned_regions"
section_entry = str( section_number ) + ". " + section_name
key_sec = ".S-0" + str ( section_number )
worksheet.write( row, col_section, section_entry ); row += 1
worksheet.write( row, col_require, "no requirements" ); row += 1

section_number += 1
section_name = "liquid_phase"
section_entry = str( section_number ) + ". " + section_name
key_sec = ".S-0" + str ( section_number )
worksheet.write( row, col_section, section_entry ); row += 1
worksheet.write( row, col_status,  "", fmt_gray )
worksheet.write( row, col_key,     key_chap + key_sec + ".req-01" )
worksheet.write( row, col_status,  "", fmt_green )
worksheet.write( row, col_require, "liquid_component" ); row += 1
worksheet.write( row, col_status,  "", fmt_red )
worksheet.write( row, col_key,     key_chap + key_sec + ".opt-01" )
worksheet.write( row, col_require, "geochemistry_component" ); row += 1


##  ##  provenance
##  ##
worksheet = workbook.add_worksheet( "provenance" )

# widen first column
worksheet.set_column( "A:A", 15 )

worksheet.write( "A1", "python source" )
worksheet.write( "B1", os.path.basename( __file__ ) )

worksheet.write( "A2", "directory" )
worksheet.write( "B2", os.getcwd( ) )

worksheet.write( "A3", "python version" )
worksheet.write( "B3", sys.version )

row = 4
worksheet.write( row, 0, "Environment variables" ); row += 1

worksheet.write( row, 0, "$USER" )
worksheet.write( row, 1, os.environ[ "USER" ] ); row += 1

worksheet.write( row, 0, "$HOSTNAME" )
worksheet.write( row, 1, os.environ[ "HOSTNAME" ] ); row += 1

worksheet.write( row, 0, "$HOME" )
worksheet.write( row, 1, os.environ[ "HOME" ] ); row += 1

worksheet.write( row, 0, "timestamp" )
worksheet.write( row, 1, datetime.datetime.now( ) ); row += 1

workbook.close()
