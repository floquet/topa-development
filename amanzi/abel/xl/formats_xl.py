#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # Excel formats

    # method 1
    # setting the property as a dictionary of key/value pairs in the constructor
    fmt_title = this_workbook.add_format( )
    fmt_title.set_bold( )
    fmt_title.set_font_color( "blue" )

    fmt_bold  = workbook.add_format( {'bold': True} )
    fmt_red   = workbook.add_format( {'bg_color': "#FFC7CE"} ) # https://xlsxwriter.readthedocs.io/example_conditional_format.html
    fmt_green = workbook.add_format( {'bg_color': "#C6EFCE"} )
    fmt_gray  = workbook.add_format( {'bg_color': "#808080"} ) # https://xlsxwriter.readthedocs.io/working_with_colors.html

    # method 2
    # passing a dictionary of properties to the add_format() constructor
    fmt_time = this_workbook.add_format( {'num_format': 'yy/mm/dd hh:mm'} ) # https://xlsxwriter.readthedocs.io/working_with_dates_and_time.html
