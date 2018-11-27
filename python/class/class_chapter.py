# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python


class Section:
    def __init__( self, level, title ):
        self.level = 1  # 1, 2, 3, ... indent level
        self.title = title  # 8

class Chapter:
    def __init__( self, chap_num, chap_title, chap_sections ):
        self.chap_num   = chap_num  # 8
        self.chap_title = chap_title   # Boundary conditions
        self.chap_sections = chap_sections

# #    # #    # #    # #    # #    # #

if __name__ == "__main__":

    # create sections
    sec_bc_assigned_region = Section( 1, "assigned_region" )
    sec_bc_liquid_phase    = Section( 1, "liquid_phase" )
    sec_bc_solid_phase     = Section( 1, "solid_phase" )
    # create chapter
    chap_bc = Chapter( 8, "Boundary Conditions",
                [ sec_bc_assigned_region, sec_bc_liquid_phase, sec_bc_solid_phase] )

    print( "chap_bc.chap_num: ",   chap_bc.chap_num )
    print( "chap_bc.chap_title: ",   chap_bc.chap_title )

    print( datetime.datetime.now( ) )

# dantopa@Lax-Millgram:class $ py employee.py
# python version:
# 3.6.7 (default, Oct 21 2018, 09:26:25)
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)]
# <__main__.Employee object at 0x10aed7550>
# <__main__.Employee object at 0x10aed75c0>
# who am I?:  Daniel Topa

# dantopa@Lax-Millgram:class $ date
# Tue Nov 20 22:05:40 MST 2018

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/class

# dantopa@Lax-Millgram:class $ python --version
# Python 3.6.7
