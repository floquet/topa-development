#! /usr/bin/python
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817


# # Write chapters

# # imports
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python


#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Requirement:
    """Optional or required"""

    def __init__( self, flavor, title, index, status ):
        self.flavor = flavor  # required or optional
        self.title  = title  # liquid_component
        self.idex   = index
        self.status = status # PASS, FAIL, NULL
        # generated
        self.key    = flavor + "-" + str( index ).zfill( 2 )

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Section:
    """Sections, subsections, subsubsections, ..."""

    def __init__( self, level, title ):
        self.level = 1  # 1, 2, 3, ... indent level
        self.title = title  # 8

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Chapter:
    """A collection of sections"""

    def __init__( self, chap_num, chap_title, chap_initials, chap_sections ):
        self.chap_num      = chap_num  # 8
        self.chap_title    = chap_title   # Boundary conditions
        self.chap_initials = chap_initials   # Boundary conditions
        self.chap_sections = chap_sections
        # generated
        # https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
        self.chap_key      = str( chap_num ).zfill( 2 ) + "-" + chap_initials

# #    # #    # #    # #    # #    # #

if __name__ == "__main__":

    # create sections
    sec_bc_assigned_region = Section( 1, "assigned_region" )
    sec_bc_liquid_phase    = Section( 1, "liquid_phase" )
    sec_bc_solid_phase     = Section( 1, "solid_phase" )
    # create chapter
    chap_bc = Chapter( 8, "Boundary Conditions", "BC",
                [ sec_bc_assigned_region, sec_bc_liquid_phase, sec_bc_solid_phase] )

    print( "chap_bc.chap_num: ",        chap_bc.chap_num )
    print( "chap_bc.chap_title: ",      chap_bc.chap_title )
    print( "chap_bc.chap_key: ",        chap_bc.chap_key )
    print( "chap_bc.chap_sections: ",   chap_bc.chap_sections )

    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    for sec in chap_bc.chap_sections:
        print( "section = ", sec )

    print( datetime.datetime.now( ) )

# dantopa@Lax-Millgram:class $ python class_chapter.py
# ('chap_bc.chap_num: ', 8)
# ('chap_bc.chap_title: ', 'Boundary Conditions')
# ('chap_bc.chap_key: ', '08-BC')
# ('chap_bc.chap_sections: ', [<__main__.Section instance at 0x10564a290>, <__main__.Section instance at 0x10564a2d8>, <__main__.Section instance at 0x10564a320>])
# ('section = ', <__main__.Section instance at 0x10564a290>)
# ('section = ', <__main__.Section instance at 0x10564a2d8>)
# ('section = ', <__main__.Section instance at 0x10564a320>)
# 2018-11-30 19:19:51.110405
