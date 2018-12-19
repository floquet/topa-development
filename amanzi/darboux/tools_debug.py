#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# # Debug tools
# xl_numbered_lines( thisWorkbook, theseLines )
# xl_dramatis_personae( thisWorkbook, thisBook )

# # imports
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_chapter_attributes( thisWorkbook, col_chapters ):
    print( "=  =  = xl_chapter_attributes: %s" % len( col_chapters ) )
    # create sheet
    sheet = tools_xl.xl_sheet_generate( thisWorkbook, "chapters" )

    # address worksheet in row, col form
    row = 1;
    col = 1;

    for c in col_chapters:
        print( "chapter number %s" % c.k_index )
        sheet.write( row, col, c.k_index )
        sheet.write( row, col + 1, c.title ); row += 1

        sheet.write( row, col, "range of lines:" )
        sheet.write( row, col + 1, c.k_start )
        sheet.write( row, col + 2, c.k_stop ); row += 1

        sheet.write( row, col, "key:" )
        sheet.write( row, col + 1, c.key ); row += 1

    print( "return" )
    return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_numbered_lines( thisWorkbook, theseLines ):
    print( "=  =  = xl_numbered_lines:" )
    sheet_numbered_lines = tools_xl.xl_sheet_generate( thisWorkbook, "text lines" )

    # address worksheet in row, col form
    row = 0;
    col = 0;
    counter = 0;
    # Excel treats === and --- as operations, not text
    # To circumvent, use the TEXT function
    # which chokes on strings containing double quotes
    myText = thisWorkbook.add_format({'num_format': '@'})
    # restablish (?) formats
    format_title = thisWorkbook.add_format( )
    format_title.set_bold( )
    format_title.set_font_color( "blue" )

    sheet_numbered_lines.write( row, col,     "index",  format_title )
    sheet_numbered_lines.write( row, col + 1, "length", format_title )
    sheet_numbered_lines.write( row, col + 2, "text",   format_title ); row += 1

    for line in theseLines:
        sheet_numbered_lines.write( row, col, counter )
        myString = '= TEXT( "' + line + '", "=" )'
        #sheet_numbered_lines.write_formula( row, col + 1, myString )
        sheet_numbered_lines.write( row, col + 1, len( line ) )
        sheet_numbered_lines.write( row, col + 2, "boo:", myText )
        sheet_numbered_lines.write( row, col + 2, line, myText ); row += 1
        #sheet_numbered_lines.write( row, col + 2, myString, myText ); row += 1
        counter += 1;
    # https://stackabuse.com/read-a-file-line-by-line-in-python/
    # with open( thisBook.source.full_rst ) as f:
    #     for cnt, line in enumerate( f ):
    #         # line number
    #         sheet_numbered_lines.write( row, col,     cnt )
    #         # text
    #         sheet_numbered_lines.write( row, col + 1, "{}".format( line ) ); row += 1
    # https://stackabuse.com/read-a-file-line-by-line-in-python/
    # with open( thisBook.source.full_rst ) as f:
    #     for cnt, line in enumerate( f ):
    #         # line number
    #         sheet_numbered_lines.write( row, col, cnt )
    #         # text
    #         myString = '= TEXT( "' + line + '", "=" )'
    #         print( "myString = %s" % myString )
    #         sheet_numbered_lines.write_formula( row, col + 1, myString ); row += 1
    return

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

def xl_dramatis_personae( thisWorkbook, thisBook ):
    # print( "=  =  = xl_dramatis_personae:" )

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
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.title ); row += 1

    sheet_dramatis_personae.write( row, col, "Data file" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.input_rst ); row += 1

    sheet_dramatis_personae.write( row, col, "Data path" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.path_rst ); row += 1

    sheet_dramatis_personae.write( row, col, "Lines read" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.numLines ); row += 1

    # sink
    row += 1
    sheet_dramatis_personae.write( row, col, "Output file", format_title ); row += 1

    sheet_dramatis_personae.write( row, col, "Output file" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.output_xl ); row += 1

    sheet_dramatis_personae.write( row, col, "Output path" )
    sheet_dramatis_personae.write( row, col + 1, thisBook.source.path_xl ); row += 1

    return;

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #
