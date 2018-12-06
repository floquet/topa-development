#! /usr/bin/python
# # Amanzi: The Multi-Process HPC Simulator
# #   https://github.com/amanzi/amanzi
# # David Moulton   DGL LANL/T-5  moulton@lanl.gov  505 665 4712
# # Daniel Topa     LANL/CCS-2    dantopa@lanl.gov  505 667 0817

# # imports
import datetime             # timestamps
import os                   # opeating system
import sys                  # python version
from pathlib import Path    # rename file
import xlsxwriter           # API for Excel
# home brew
# classes
import cls_Book             # Book (constains sections, contains requirements)
import cls_Source_file      # e.q. Amanzi XML Input Specification (Version 2.3-draft)
# tools
import tools_debug
import tools_parse          # file parsing tools
import tools_xl             # spreadsheet authoring tools

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    # # source data
    mySource = cls_Source_file.Source_file( ) # instantiate
    print( "mySource.uuid = %s" % mySource.uuid )
    mySource.input_rst = "short.rst"    # setter called
    #mySource.path_rst  = "/Users/dantopa/Documents/repos/GitHub/topa-development/data/"
    mySource.path_rst = "/Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/"    # setter called
    mySource.full_rst  = mySource.path_rst + mySource.input_rst

    # # output file
    mySource.output_xl = Path( mySource.input_rst ).stem + ".xlsx" # https://stackoverflow.com/questions/2900035/changing-file-extension-in-python
    mySource.path_xl   = mySource.path_rst
    mySource.full_xl   = mySource.path_xl + mySource.output_xl

    # # start the book
    myBook = cls_Book.Book( ) # instantiate
    myBook.source_object = mySource

    # first read rst
    myWorkbook = tools_xl.xl_new_workbook( mySource.full_xl )
    ( numLines, myLines ) = tools_parse.reader( mySource.path_name ) # read file as split lines
    myBook.source_object.title = myLines[ 1 ] # harvest title line
    myBook.source_object.numLines = numLines
    # worksheets for debugging
    tools_debug.xl_dramatis_personae( myWorkbook, myBook )
    tools_debug.xl_numbered_lines( myWorkbook, myLines )

    # continue parsing - compile lists of target locations
    ( loc_xml, loc_candidate_header0, loc_candidate_header1, loc_candidate_header2 ) = mySource.parse_candidates( myLines )  # first parse: candidate headers
    mySource.parse_match_lengths( myLines, loc_candidate_header0 )
    mySource.parse_match_lengths( myLines, loc_candidate_header1 )
    mySource.parse_match_lengths( myLines, loc_candidate_header2 )

    # write workbook
    myWorkbook.close( )

    print( "\n", datetime.datetime.now( ) )
    print( "source: %s/%s" % ( os.getcwd( ), os.path.basename( __file__ ) ) )
    print( "python version %s" % sys.version )

# l127914@pn1249300.lanl.gov:bourbaki $ python catullus.py
# mySource.uuid = 54e586ec-8315-49d2-8b80-802a41a9f5d0
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# 231 lines found
# Line 1: ====================================================
# possible header 0 in line 1
# Line 2: Amanzi XML Input Specification (Version 2.3-draft)
# Line 3: ====================================================
# possible header 0 in line 3
# Line 4:
# Line 5: .. contents:: **Table of Contents**
# Line 6:
# Line 7:
# Line 8: Overview
# Line 9: ========
# possible header 0 in line 9
# Line 10:
# Line 11: The Amanzi simulator evolves a system of conservation equations for reacting flows in porous media, as detailed in the ASCEM report entitled `"Mathematical Formulation Requirements and Specifications for the Process Models`" (hereafter referred to as the 'Model Requirements Document (MRD)'). The purpose of the present document is to specify the data required to execute Amanzi.  This specification should be regarded as a companion to the MRD, and parameterizations of the individual submodels are consistent between Amanzi, the MRD and this document. Where applicable, the relevant sections of the MRD are indicated.
# Line 12:
# Line 13: All data required to execute Amanzi is specified within an XML formated file laid out according to the Amanzi input schema.  The current version of the Amanzi schema is located with the Amanzi source code repository.  The following discusses each section of the schema, its purpose and provides examples.  Further details can be found in the schema document amanzi.xsd.
# Line 14:
# Line 15: Please note, many attributes within the XML list a limited set of specified values.  During validation of the input file or initialization of Amanzi the values in the user provided input file will be compared against the limited set provided in the XML Schema document.  Errors will occur is the values do not match exactly.  These values are CASE SENSITIVE.  The Amanzi schema has been designed will all LOWER CASE values.  Please note this when writing input file.  In particular, `"Exodus II`" will be evaluated as `"exodus ii`".
# Line 16:
# Line 17: Amanzi Input
# Line 18: ============
# possible header 0 in line 18
# Line 19:
# Line 20: Here, the user specifies which version of the input the input file adheres to. The user also specifies the overall type of simulation being run.  Amanzi supports both structured and unstructured numerical solution approaches.  This flexibility has a direct impact on the selection and design of the underlying numerical algorithms, the style of the software implementations, and, ultimately, the complexity of the user-interface. The attribute *type* is used to selected between the following:
# Line 21:
# Line 22: * ``Structured``: This instructs Amanzi to use BoxLib data structures and an associated paradigm to numerically represent the flow equations.  Data containers in the BoxLib software library, developed by CCSE at LBNL, are based on a hierarchical set of uniform Cartesian grid patches.  ``Structured`` requires that the simulation domain be a single coordinate-aligned rectangle, and that the "base mesh" consists of a logically rectangular set of uniform hexahedral cells.  This option supports a block-structured approach to dynamic mesh refinement, wherein successively refined subregions of the solution are constructed dynamically to track "interesting" features of the evolving solution.  The numerical solution approach implemented under the ``Structured`` framework is highly optimized to exploit regular data and access patterns on massively parallel computing architectures.
# Line 23:
# Line 24: * ``Unstructured``: This instructs Amanzi to use data structures provided in the Trilinos software framework.  To the extent possible, the discretization algorithms implemented under this option are largely independent of the shape and connectivity of the underlying cells.  As a result, this option supports an arbitrarily complex computational mesh structure that enables users to work with numerical meshes that can be aligned with geometrically complex man-made or geostatigraphical features.  Under this option, the user typically provides a mesh file that was generated with an external software package.  The following mesh file formats are currently supported: `"Exodus II`".  Amanzi also provides a rudimentary capability to generate regular meshes within the unstructured framework internally.
# Line 25:
# Line 26: An example root tag of an input file would look like the following.
# Line 27:
# Line 28: .. code-block:: xml
# xml found in line 28
# Line 29:
# Line 30:   <amanzi_input version="2.2.1" type="unstructured"/>
# Line 31:
# Line 32:
# Line 33: Model Description
# Line 34: =================
# possible header 0 in line 34
# Line 35:
# Line 36: This allows the users to provide a name and general description of model being developed.  This is also the section in which the units for the problem are stored. This entire section is optional but encouraged as documentation.
# Line 37:
# Line 38: .. code-block:: xml
# xml found in line 38
# Line 39:
# Line 40:   <model_description name="Name of Model" >
# Line 41:       Required Elements: NONE
# Line 42:       Optional Elements: comment, author, created, modified, model_id, description, purpose, units
# Line 43:   </model_description>
# Line 44:
# Line 45: All elements expect string content, except ``units`` which is described below.
# Line 46:
# Line 47: Units
# Line 48: -----
# possible header 1 in line 48
# Line 49:
# Line 50: The ``units`` element defines the default units to be assumed for the entire input file.  Amanzi's internal default units are SI units.  Conversion from the listed units to Amanzi's internal default units is not yet implemented.  Akuna does allow users to specify units when entering individual values during model setup and tool set definition.  Akuna then translates all user specified units to the Amanzi default units before writing out the Amanzi input file.
# Line 51:
# Line 52: ``units`` has the optional elements of length, time, mass, and concentration.  Each of those in turn have their own structure.  The structures are as follows.
# Line 53:
# Line 54: REMINDER - UNITS ARE NOT IMPLEMENTED YET
# Line 55:
# Line 56: .. code-block:: xml
# xml found in line 56
# Line 57:
# Line 58:   <units>
# Line 59:       Required Elements: NONE
# Line 60:       Optional Elements: length_unit, time_unit, mass_unit, conc_unit
# Line 61:   </units>
# Line 62:
# Line 63: Acceptable values for each unit are as follows:
# Line 64:
# Line 65: +----------------+----------------+
# possible header 1 in line 65
# Line 66: | Units Elements | Value Options  |
# Line 67: +================+================+
# Line 68: | length_unit    | m or cm        |
# Line 69: +----------------+----------------+
# possible header 1 in line 69
# Line 70: | time_unit      | y, d, h, or s  |
# Line 71: +----------------+----------------+
# possible header 1 in line 71
# Line 72: | mass_unit      | kg             |
# Line 73: +----------------+----------------+
# possible header 1 in line 73
# Line 74: | conc_unit      | molar, SI      |
# Line 75: +----------------+----------------+
# possible header 1 in line 75
# Line 76:
# Line 77: Note, currently mol/m^3 concentration unit is only available for unstructured.  The input converter for unstructured will convert the concentration internally as needed.
# Line 78:
# Line 79: Here is an overall example for the model description element.
# Line 80:
# Line 81: .. code-block:: xml
# xml found in line 81
# Line 82:
# Line 83:   <model_description name="DVZ 3layer 2D">
# Line 84:     <comments>This is a simplified 3-layer DVZ problem in 2D with two cribs (Flow+Transport)</comments>
# Line 85:     <model_name>DVZ 3layer</model_name>
# Line 86:     <author>d3k870</author>
# Line 87:     <units>
# Line 88:       <length_unit>m</length_unit>
# Line 89:       <time_unit>s</time_unit>
# Line 90:       <mass_unit>kg</mass_unit>
# Line 91:       <conc_unit>molar</conc_unit>
# Line 92:     </units>
# Line 93:   </model_description>
# Line 94:
# Line 95:
# Line 96: Definitions
# Line 97: ===========
# possible header 0 in line 97
# Line 98:
# Line 99: Definitions allows the user the define and name constants, times, and macros to be used in later sections of the input file.  This is to streamline the look and readability of the input file.  The user should take care not to reuse names within this section or other sections.  This may have unindented consequences.
# Line 100:
# Line 101: .. code-block:: xml
# xml found in line 101
# Line 102:
# Line 103:   <definitions>
# Line 104:       Required Elements: NONE
# Line 105:       Optional Elements: constants, macros
# Line 106:   </definitions>
# Line 107:
# Line 108: Constants
# Line 109: ---------
# possible header 1 in line 109
# Line 110:
# Line 111: Here the user can define and name constants to be used in other sections of the input file.  Note that if a name is repeated the last read value will be retained and all others will be overwritten.  See `Constants`_ for specifying time units other than seconds.
# Line 112:
# Line 113: .. code-block:: xml
# xml found in line 113
# Line 114:
# Line 115:   <constants>
# Line 116:       Required Elements: NONE
# Line 117:       Optional Elements: constant, time_constant, numerical_constant, area_mass_flux_constant
# Line 118:   </constants>
# Line 119:
# Line 120: A ``constant`` has three attributes ``name``, ``type``, and ``value``.  The user can provide any name, but note it should not be repeated anywhere within the input to avoid confusion.  The available types include: `"none`", `"time`", `"numerical`", and `"area_mass_flux`".  Values assigned to constants of type `"time`" can include known units, otherwise seconds will be assumed as the default. See `Constants`_ for specifying time units other than seconds.
# Line 121:
# Line 122: .. code-block:: xml
# xml found in line 122
# Line 123:
# Line 124:     <constant name="String" type="none | time | numerical | area_mass_flux" value="constant_value"/>
# Line 125:
# Line 126: A ``time_constant`` is a specific form of a constant assuming the constant type is a time.  It takes the attributes ``name`` and ``value`` where the value is a time (time unit optional).
# Line 127:
# Line 128: .. code-block:: xml
# xml found in line 128
# Line 129:
# Line 130:     <time_constant  name="Name of Time"  value="time,y|d|h|s"/>
# Line 131:
# Line 132: A ``numerical_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value``.
# Line 133:
# Line 134: .. code-block:: xml
# xml found in line 134
# Line 135:
# Line 136:     <numerical_constant name="Name of Numerical Constant" value="value_constant"/>
# Line 137:
# Line 138: A ``area_mass_flux_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value`` where the value is an area mass flux.
# Line 139:
# Line 140: .. code-block:: xml
# xml found in line 140
# Line 141:
# Line 142:     <area_mass_flux_constant name="Name of Flux Constant" value="value_of_flux"/>
# Line 143:
# Line 144: Macros
# Line 145: ------
# possible header 1 in line 145
# Line 146:
# Line 147: The ``macros`` section defines time, cycle, and variable macros.  These specify a list or interval for triggering an action, particularly, writing out visualization, checkpoint, walkabout, or observation files.
# Line 148:
# Line 149: .. code-block:: xml
# xml found in line 149
# Line 150:
# Line 151:   <constants>
# Line 152:       Required Elements: NONE
# Line 153:       Optional Elements: time_macro, cycle_macro, variable_macro [S]
# Line 154:   </constants>
# Line 155:
# Line 156:
# Line 157: Time_macro
# Line 158: __________
# possible header 2 in line 158
# Line 159:
# Line 160: The ``time_macro`` requires an attribute ``name``.  The macro can then either take the form of one or more labeled time subelements or the subelements ``start``, ``timestep_interval``, and ``stop`` again containing labeled times.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.  The labeled times can be time values assuming the default time unit of seconds or including a known time unit.
# Line 161:
# Line 162: .. code-block:: xml
# xml found in line 162
# Line 163:
# Line 164:   <time_macro name="Name of Macro">
# Line 165:     <time>Value</time>
# Line 166:   </time_macro>
# Line 167:
# Line 168: or
# Line 169:
# Line 170: .. code-block:: xml
# xml found in line 170
# Line 171:
# Line 172:   <time_macro name="Name of Macro">
# Line 173:     <start> TimeValue </start>
# Line 174:     <timestep_interval> TimeIntervalValue </timestep_interval>
# Line 175:     <stop> TimeValue | -1 </stop>
# Line 176:   </time_macro>
# Line 177:
# Line 178:
# Line 179: Cycle_macro
# Line 180: ___________
# possible header 2 in line 180
# Line 181:
# Line 182:
# Line 183: The ``cycle_macro`` requires an attribute ``name`` and the subelements ``start``, ``timestep_interval``, and ``stop`` with integer values.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.
# Line 184:
# Line 185: .. code-block:: xml
# xml found in line 185
# Line 186:
# Line 187:   <cycle_macro name="Name of Macro">
# Line 188:     <start>Value</start>
# Line 189:     <timestep_interval>Value</timestep_interval>
# Line 190:     <stop>Value|-1</stop>
# Line 191:   </cycle_macro>
# Line 192:
# Line 193: Variable_macro
# Line 194: ______________
# possible header 2 in line 194
# Line 195:
# Line 196: The ``variable_macro`` requires an attribute ``name``  and one or more subelements ``variable`` containing strings.
# Line 197:
# Line 198: .. code-block:: xml
# xml found in line 198
# Line 199:
# Line 200:   <variable_macro name="Name of Macro">
# Line 201:     <variable> VariableString </variable>
# Line 202:   </variable_macro>
# Line 203:
# Line 204:
# Line 205: An example ``definition`` section would look as the following:
# Line 206:
# Line 207: .. code-block:: xml
# xml found in line 207
# Line 208:
# Line 209:   <definitions>
# Line 210:     <constants>
# Line 211:       <constant name="zero"              type="none"           value="0.000"/>
# Line 212:       <constant name ="start"            type="time"           value="1956.0,y"/>
# Line 213:       <constant name ="B-18_release_end" type="time"           value ="1956.3288,y"/>
# Line 214:       <constant name="future_recharge"   type="area_mass_flux" value="1.48666e-6"/>
# Line 215:       <numerical_constant name="zero" value="0.000"/>
# Line 216:     </constants>
# Line 217:     <macros>
# Line 218:       <time_macro name="Macro 1">
# Line 219:         <time>6.17266656E10</time>
# Line 220:         <time>6.172982136E10</time>
# Line 221:         <time>6.173297712E10</time>
# Line 222:         <time>6.3372710016E10</time>
# Line 223:         <time>6.33834396E10</time>
# Line 224:       </time_macro>
# Line 225:       <cycle_macro name = "Every_1000_timesteps">
# Line 226:         <start>0</start>
# Line 227:         <timestep_interval>1000</timestep_interval>
# Line 228:         <stop>-1 </stop>
# Line 229:       </cycle_macro>
# Line 230:     </macros>
# Line 231:   </definitions>
# 16 xml blocks found; locations [28, 38, 56, 81, 101, 113, 122, 128, 134, 140, 149, 162, 170, 185, 198, 207]
# 6 header0 candidates found; locations [1, 3, 9, 18, 34, 97]
# 8 header1 candidates found; locations [48, 65, 69, 71, 73, 75, 109, 145]
# Traceback (most recent call last):
#   File "catullus.py", line 53, in <module>
#     ( loc_xml, loc_candidate_header0, loc_candidate_header1 ) = mySource.parse1( myLines )  # first parse: candidate headers
# ValueError: too many values to unpack (expected 3)
# l127914@pn1249300.lanl.gov:bourbaki $ python catullus.py
# mySource.uuid = e9f5f894-5234-4954-bc26-a93b493af70b
# reading source file /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/data/short.rst
# 231 lines found
# Line 1: ====================================================
# possible header 0 in line 1
# Line 2: Amanzi XML Input Specification (Version 2.3-draft)
# Line 3: ====================================================
# possible header 0 in line 3
# Line 4:
# Line 5: .. contents:: **Table of Contents**
# Line 6:
# Line 7:
# Line 8: Overview
# Line 9: ========
# possible header 0 in line 9
# Line 10:
# Line 11: The Amanzi simulator evolves a system of conservation equations for reacting flows in porous media, as detailed in the ASCEM report entitled `"Mathematical Formulation Requirements and Specifications for the Process Models`" (hereafter referred to as the 'Model Requirements Document (MRD)'). The purpose of the present document is to specify the data required to execute Amanzi.  This specification should be regarded as a companion to the MRD, and parameterizations of the individual submodels are consistent between Amanzi, the MRD and this document. Where applicable, the relevant sections of the MRD are indicated.
# Line 12:
# Line 13: All data required to execute Amanzi is specified within an XML formated file laid out according to the Amanzi input schema.  The current version of the Amanzi schema is located with the Amanzi source code repository.  The following discusses each section of the schema, its purpose and provides examples.  Further details can be found in the schema document amanzi.xsd.
# Line 14:
# Line 15: Please note, many attributes within the XML list a limited set of specified values.  During validation of the input file or initialization of Amanzi the values in the user provided input file will be compared against the limited set provided in the XML Schema document.  Errors will occur is the values do not match exactly.  These values are CASE SENSITIVE.  The Amanzi schema has been designed will all LOWER CASE values.  Please note this when writing input file.  In particular, `"Exodus II`" will be evaluated as `"exodus ii`".
# Line 16:
# Line 17: Amanzi Input
# Line 18: ============
# possible header 0 in line 18
# Line 19:
# Line 20: Here, the user specifies which version of the input the input file adheres to. The user also specifies the overall type of simulation being run.  Amanzi supports both structured and unstructured numerical solution approaches.  This flexibility has a direct impact on the selection and design of the underlying numerical algorithms, the style of the software implementations, and, ultimately, the complexity of the user-interface. The attribute *type* is used to selected between the following:
# Line 21:
# Line 22: * ``Structured``: This instructs Amanzi to use BoxLib data structures and an associated paradigm to numerically represent the flow equations.  Data containers in the BoxLib software library, developed by CCSE at LBNL, are based on a hierarchical set of uniform Cartesian grid patches.  ``Structured`` requires that the simulation domain be a single coordinate-aligned rectangle, and that the "base mesh" consists of a logically rectangular set of uniform hexahedral cells.  This option supports a block-structured approach to dynamic mesh refinement, wherein successively refined subregions of the solution are constructed dynamically to track "interesting" features of the evolving solution.  The numerical solution approach implemented under the ``Structured`` framework is highly optimized to exploit regular data and access patterns on massively parallel computing architectures.
# Line 23:
# Line 24: * ``Unstructured``: This instructs Amanzi to use data structures provided in the Trilinos software framework.  To the extent possible, the discretization algorithms implemented under this option are largely independent of the shape and connectivity of the underlying cells.  As a result, this option supports an arbitrarily complex computational mesh structure that enables users to work with numerical meshes that can be aligned with geometrically complex man-made or geostatigraphical features.  Under this option, the user typically provides a mesh file that was generated with an external software package.  The following mesh file formats are currently supported: `"Exodus II`".  Amanzi also provides a rudimentary capability to generate regular meshes within the unstructured framework internally.
# Line 25:
# Line 26: An example root tag of an input file would look like the following.
# Line 27:
# Line 28: .. code-block:: xml
# xml found in line 28
# Line 29:
# Line 30:   <amanzi_input version="2.2.1" type="unstructured"/>
# Line 31:
# Line 32:
# Line 33: Model Description
# Line 34: =================
# possible header 0 in line 34
# Line 35:
# Line 36: This allows the users to provide a name and general description of model being developed.  This is also the section in which the units for the problem are stored. This entire section is optional but encouraged as documentation.
# Line 37:
# Line 38: .. code-block:: xml
# xml found in line 38
# Line 39:
# Line 40:   <model_description name="Name of Model" >
# Line 41:       Required Elements: NONE
# Line 42:       Optional Elements: comment, author, created, modified, model_id, description, purpose, units
# Line 43:   </model_description>
# Line 44:
# Line 45: All elements expect string content, except ``units`` which is described below.
# Line 46:
# Line 47: Units
# Line 48: -----
# possible header 1 in line 48
# Line 49:
# Line 50: The ``units`` element defines the default units to be assumed for the entire input file.  Amanzi's internal default units are SI units.  Conversion from the listed units to Amanzi's internal default units is not yet implemented.  Akuna does allow users to specify units when entering individual values during model setup and tool set definition.  Akuna then translates all user specified units to the Amanzi default units before writing out the Amanzi input file.
# Line 51:
# Line 52: ``units`` has the optional elements of length, time, mass, and concentration.  Each of those in turn have their own structure.  The structures are as follows.
# Line 53:
# Line 54: REMINDER - UNITS ARE NOT IMPLEMENTED YET
# Line 55:
# Line 56: .. code-block:: xml
# xml found in line 56
# Line 57:
# Line 58:   <units>
# Line 59:       Required Elements: NONE
# Line 60:       Optional Elements: length_unit, time_unit, mass_unit, conc_unit
# Line 61:   </units>
# Line 62:
# Line 63: Acceptable values for each unit are as follows:
# Line 64:
# Line 65: +----------------+----------------+
# possible header 1 in line 65
# Line 66: | Units Elements | Value Options  |
# Line 67: +================+================+
# Line 68: | length_unit    | m or cm        |
# Line 69: +----------------+----------------+
# possible header 1 in line 69
# Line 70: | time_unit      | y, d, h, or s  |
# Line 71: +----------------+----------------+
# possible header 1 in line 71
# Line 72: | mass_unit      | kg             |
# Line 73: +----------------+----------------+
# possible header 1 in line 73
# Line 74: | conc_unit      | molar, SI      |
# Line 75: +----------------+----------------+
# possible header 1 in line 75
# Line 76:
# Line 77: Note, currently mol/m^3 concentration unit is only available for unstructured.  The input converter for unstructured will convert the concentration internally as needed.
# Line 78:
# Line 79: Here is an overall example for the model description element.
# Line 80:
# Line 81: .. code-block:: xml
# xml found in line 81
# Line 82:
# Line 83:   <model_description name="DVZ 3layer 2D">
# Line 84:     <comments>This is a simplified 3-layer DVZ problem in 2D with two cribs (Flow+Transport)</comments>
# Line 85:     <model_name>DVZ 3layer</model_name>
# Line 86:     <author>d3k870</author>
# Line 87:     <units>
# Line 88:       <length_unit>m</length_unit>
# Line 89:       <time_unit>s</time_unit>
# Line 90:       <mass_unit>kg</mass_unit>
# Line 91:       <conc_unit>molar</conc_unit>
# Line 92:     </units>
# Line 93:   </model_description>
# Line 94:
# Line 95:
# Line 96: Definitions
# Line 97: ===========
# possible header 0 in line 97
# Line 98:
# Line 99: Definitions allows the user the define and name constants, times, and macros to be used in later sections of the input file.  This is to streamline the look and readability of the input file.  The user should take care not to reuse names within this section or other sections.  This may have unindented consequences.
# Line 100:
# Line 101: .. code-block:: xml
# xml found in line 101
# Line 102:
# Line 103:   <definitions>
# Line 104:       Required Elements: NONE
# Line 105:       Optional Elements: constants, macros
# Line 106:   </definitions>
# Line 107:
# Line 108: Constants
# Line 109: ---------
# possible header 1 in line 109
# Line 110:
# Line 111: Here the user can define and name constants to be used in other sections of the input file.  Note that if a name is repeated the last read value will be retained and all others will be overwritten.  See `Constants`_ for specifying time units other than seconds.
# Line 112:
# Line 113: .. code-block:: xml
# xml found in line 113
# Line 114:
# Line 115:   <constants>
# Line 116:       Required Elements: NONE
# Line 117:       Optional Elements: constant, time_constant, numerical_constant, area_mass_flux_constant
# Line 118:   </constants>
# Line 119:
# Line 120: A ``constant`` has three attributes ``name``, ``type``, and ``value``.  The user can provide any name, but note it should not be repeated anywhere within the input to avoid confusion.  The available types include: `"none`", `"time`", `"numerical`", and `"area_mass_flux`".  Values assigned to constants of type `"time`" can include known units, otherwise seconds will be assumed as the default. See `Constants`_ for specifying time units other than seconds.
# Line 121:
# Line 122: .. code-block:: xml
# xml found in line 122
# Line 123:
# Line 124:     <constant name="String" type="none | time | numerical | area_mass_flux" value="constant_value"/>
# Line 125:
# Line 126: A ``time_constant`` is a specific form of a constant assuming the constant type is a time.  It takes the attributes ``name`` and ``value`` where the value is a time (time unit optional).
# Line 127:
# Line 128: .. code-block:: xml
# xml found in line 128
# Line 129:
# Line 130:     <time_constant  name="Name of Time"  value="time,y|d|h|s"/>
# Line 131:
# Line 132: A ``numerical_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value``.
# Line 133:
# Line 134: .. code-block:: xml
# xml found in line 134
# Line 135:
# Line 136:     <numerical_constant name="Name of Numerical Constant" value="value_constant"/>
# Line 137:
# Line 138: A ``area_mass_flux_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value`` where the value is an area mass flux.
# Line 139:
# Line 140: .. code-block:: xml
# xml found in line 140
# Line 141:
# Line 142:     <area_mass_flux_constant name="Name of Flux Constant" value="value_of_flux"/>
# Line 143:
# Line 144: Macros
# Line 145: ------
# possible header 1 in line 145
# Line 146:
# Line 147: The ``macros`` section defines time, cycle, and variable macros.  These specify a list or interval for triggering an action, particularly, writing out visualization, checkpoint, walkabout, or observation files.
# Line 148:
# Line 149: .. code-block:: xml
# xml found in line 149
# Line 150:
# Line 151:   <constants>
# Line 152:       Required Elements: NONE
# Line 153:       Optional Elements: time_macro, cycle_macro, variable_macro [S]
# Line 154:   </constants>
# Line 155:
# Line 156:
# Line 157: Time_macro
# Line 158: __________
# possible header 2 in line 158
# Line 159:
# Line 160: The ``time_macro`` requires an attribute ``name``.  The macro can then either take the form of one or more labeled time subelements or the subelements ``start``, ``timestep_interval``, and ``stop`` again containing labeled times.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.  The labeled times can be time values assuming the default time unit of seconds or including a known time unit.
# Line 161:
# Line 162: .. code-block:: xml
# xml found in line 162
# Line 163:
# Line 164:   <time_macro name="Name of Macro">
# Line 165:     <time>Value</time>
# Line 166:   </time_macro>
# Line 167:
# Line 168: or
# Line 169:
# Line 170: .. code-block:: xml
# xml found in line 170
# Line 171:
# Line 172:   <time_macro name="Name of Macro">
# Line 173:     <start> TimeValue </start>
# Line 174:     <timestep_interval> TimeIntervalValue </timestep_interval>
# Line 175:     <stop> TimeValue | -1 </stop>
# Line 176:   </time_macro>
# Line 177:
# Line 178:
# Line 179: Cycle_macro
# Line 180: ___________
# possible header 2 in line 180
# Line 181:
# Line 182:
# Line 183: The ``cycle_macro`` requires an attribute ``name`` and the subelements ``start``, ``timestep_interval``, and ``stop`` with integer values.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.
# Line 184:
# Line 185: .. code-block:: xml
# xml found in line 185
# Line 186:
# Line 187:   <cycle_macro name="Name of Macro">
# Line 188:     <start>Value</start>
# Line 189:     <timestep_interval>Value</timestep_interval>
# Line 190:     <stop>Value|-1</stop>
# Line 191:   </cycle_macro>
# Line 192:
# Line 193: Variable_macro
# Line 194: ______________
# possible header 2 in line 194
# Line 195:
# Line 196: The ``variable_macro`` requires an attribute ``name``  and one or more subelements ``variable`` containing strings.
# Line 197:
# Line 198: .. code-block:: xml
# xml found in line 198
# Line 199:
# Line 200:   <variable_macro name="Name of Macro">
# Line 201:     <variable> VariableString </variable>
# Line 202:   </variable_macro>
# Line 203:
# Line 204:
# Line 205: An example ``definition`` section would look as the following:
# Line 206:
# Line 207: .. code-block:: xml
# xml found in line 207
# Line 208:
# Line 209:   <definitions>
# Line 210:     <constants>
# Line 211:       <constant name="zero"              type="none"           value="0.000"/>
# Line 212:       <constant name ="start"            type="time"           value="1956.0,y"/>
# Line 213:       <constant name ="B-18_release_end" type="time"           value ="1956.3288,y"/>
# Line 214:       <constant name="future_recharge"   type="area_mass_flux" value="1.48666e-6"/>
# Line 215:       <numerical_constant name="zero" value="0.000"/>
# Line 216:     </constants>
# Line 217:     <macros>
# Line 218:       <time_macro name="Macro 1">
# Line 219:         <time>6.17266656E10</time>
# Line 220:         <time>6.172982136E10</time>
# Line 221:         <time>6.173297712E10</time>
# Line 222:         <time>6.3372710016E10</time>
# Line 223:         <time>6.33834396E10</time>
# Line 224:       </time_macro>
# Line 225:       <cycle_macro name = "Every_1000_timesteps">
# Line 226:         <start>0</start>
# Line 227:         <timestep_interval>1000</timestep_interval>
# Line 228:         <stop>-1 </stop>
# Line 229:       </cycle_macro>
# Line 230:     </macros>
# Line 231:   </definitions>
# 16 xml blocks found; locations [28, 38, 56, 81, 101, 113, 122, 128, 134, 140, 149, 162, 170, 185, 198, 207]
# 6 header0 candidates found; locations [1, 3, 9, 18, 34, 97]
# 8 header1 candidates found; locations [48, 65, 69, 71, 73, 75, 109, 145]
#
#  2018-12-06 13:32:45.490899
# source: /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/amanzi/bourbaki/catullus.py
# python version 3.7.0 (default, Jun 28 2018, 07:39:16)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
