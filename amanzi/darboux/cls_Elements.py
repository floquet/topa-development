#!/usr/bin/python

# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton DGL LANL/T-5 moulton@lanl.gov 505 665 4712
# # Daniel Topa LANL/CCS-2 dantopa@lanl.gov 505 667 0817

# Source class
#  source:  Amanzi manual to be parsed
#  sink:    Excel file with test matrix

import uuid                 # Universal Unique IDentifier

class Element( object ):
    def __init__( self ):

        self._name         = None    # time_macro
        self._flavor       = None    # Optional or Required
        self._result       = None    # PASS, FAIL, NULL
        self._uuid         = uuid.uuid4( ) # de facto time stamp
        self._k_line       = None    # line number
        self._k_count      = None    # line number
        self._k_chapter    = None
        self._k_section    = None
        self._k_subsection = None
