#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # Debug tools
# reader( file_source )

# # imports
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_dramatis_personae( thisWorkbook, thisBook ):

    sheet_dramatis_personae = tools_xl.xl_sheet_generate( thisWorkbook, "dramatis personae" )

    # restablish (?) formats
    format_title = thisWorkbook.add_format( )
    format_title.set_bold( )
    format_title.set_font_color( "blue" )

    # address worksheet in row, col form
    row = 0;
    col = 0;
    sheet_dramatis_personae.write( row, col, "Source file", format_title ); row += 1

    sheet_dramatis_personae.write( row, col, "File name" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.input_rst ); row += 1

    sheet_dramatis_personae.write( row, col, "Path" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.path_rst ); row += 1


    return;

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #
