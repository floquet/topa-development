#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator - https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5
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

    def __init__( self, level, title, index, requirements, subsection ):
        self.level = 1  # 1, 2, 3, ... indent level
        self.title = title  # 8
        self.index = index
        self.requirements = requirements
        self.subsection = subsection
        # generated
        self.sec_key = "S" * level + "-" + str( index ).zfill( 2 ) # SSS-03

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
        self.chap_ego      = str( chap_num ).zfill( 2 ) + "-" + chap_title
        self.chap_key      = str( chap_num ).zfill( 2 ) + "-" + chap_initials

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Book:
    """A collection of chapters"""

    def __init__( self, book_title, chap_sections, num_sections, book_census_requirements, book_census_optionals ):
        self.book_title               = book_title  # 8
        self.chap_sections            = chap_sections   # Boundary conditions
        self.num_sections             = num_sections
        self.book_census_requirements = book_census_requirements
        self.book_census_optionals    = book_census_optionals

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

class Census:
    """Census of requirements"""

    def __init__( self, num_total, num_PASS, num_FAIL, num_NULL ):
        self.num_PASS  = num_PASS # number of PASSes
        self.num_FAIL  = num_FAIL # number of FAILs
        self.num_NULL  = num_NULL # number of NULL tests
        self.num_total = num_total # sum of the above
        self.flavor    = flavor  # required or optional

# #    # #    # #    # #    # #    # #
