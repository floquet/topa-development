#! /usr/bin/python
# # Daniel Topa  LANL/CCS-2  dantopa@lanl.gov  505 667 0817

# # imports

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Requirement:
    """Optional or required"""

    def __init__( self, flavor, title, index, status ):
        self.flavor = flavor  # required or optional
        self.title  = title  # liquid_component
        self.index  = index
        self.status = status # PASS, FAIL, NULL
        # generated
        self.key    = flavor + "-" + str( index ).zfill( 2 )

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Section:
    """Sections, subsections, subsubsections, ..."""

    def __init__( self, level, title, index ):
        self.level = 1  # 1, 2, 3, ... indent level
        self.title = title  # 8
        self.index = index
        # generated
        self.sec_key = "S" * level + str( level ).zfill( 2 )

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
