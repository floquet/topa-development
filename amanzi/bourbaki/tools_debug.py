#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# # Debug tools
# reader( file_source )

# # imports
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_numbered_lines( thisWorkbook, thisBook ):

    sheet_numbered_lines = tools_xl.xl_sheet_generate( thisWorkbook, "numbered lines" )

    # address worksheet in row, col form
    row = 0;
    col = 0;

    # https://stackabuse.com/read-a-file-line-by-line-in-python/
    with open( thisBook.source_object.full_rst ) as f:
       for cnt, line in enumerate( f ):
           # line number
           sheet_numbered_lines.write( row, col,     "{}".format( cnt ) )
           # text
           sheet_numbered_lines.write( row, col + 1, "{}".format( line ) ); row += 1

    return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_dramatis_personae( thisWorkbook, thisBook ):

    sheet_dramatis_personae = tools_xl.xl_sheet_generate( thisWorkbook, "dramatis personae" )
    # widen first column
    sheet_dramatis_personae.set_column( "A:A", 10 )

    # restablish (?) formats
    format_title = thisWorkbook.add_format( )
    format_title.set_bold( )
    format_title.set_font_color( "blue" )

    # address worksheet in row, col form
    row = 0;
    col = 0;

    # source
    sheet_dramatis_personae.write( row, col, "Source file", format_title ); row += 1

    sheet_dramatis_personae.write( row, col, "Title" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.title ); row += 1

    sheet_dramatis_personae.write( row, col, "Data file" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.input_rst ); row += 1

    sheet_dramatis_personae.write( row, col, "Data path" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.path_rst ); row += 1

    sheet_dramatis_personae.write( row, col, "Lines read" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.numLines ); row += 1

    # sink
    row += 1
    sheet_dramatis_personae.write( row, col, "Output file", format_title ); row += 1

    sheet_dramatis_personae.write( row, col, "Output file" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.output_xl ); row += 1

    sheet_dramatis_personae.write( row, col, "Output path" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source_object.path_xl ); row += 1

    return;

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #
