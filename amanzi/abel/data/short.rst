====================================================
Amanzi XML Input Specification (Version 2.3-draft)
====================================================

.. contents:: **Table of Contents**


Overview
========

The Amanzi simulator evolves a system of conservation equations for reacting flows in porous media, as detailed in the ASCEM report entitled `"Mathematical Formulation Requirements and Specifications for the Process Models`" (hereafter referred to as the 'Model Requirements Document (MRD)'). The purpose of the present document is to specify the data required to execute Amanzi.  This specification should be regarded as a companion to the MRD, and parameterizations of the individual submodels are consistent between Amanzi, the MRD and this document. Where applicable, the relevant sections of the MRD are indicated.

All data required to execute Amanzi is specified within an XML formated file laid out according to the Amanzi input schema.  The current version of the Amanzi schema is located with the Amanzi source code repository.  The following discusses each section of the schema, its purpose and provides examples.  Further details can be found in the schema document amanzi.xsd.

Please note, many attributes within the XML list a limited set of specified values.  During validation of the input file or initialization of Amanzi the values in the user provided input file will be compared against the limited set provided in the XML Schema document.  Errors will occur is the values do not match exactly.  These values are CASE SENSITIVE.  The Amanzi schema has been designed will all LOWER CASE values.  Please note this when writing input file.  In particular, `"Exodus II`" will be evaluated as `"exodus ii`".

Amanzi Input
============

Here, the user specifies which version of the input the input file adheres to. The user also specifies the overall type of simulation being run.  Amanzi supports both structured and unstructured numerical solution approaches.  This flexibility has a direct impact on the selection and design of the underlying numerical algorithms, the style of the software implementations, and, ultimately, the complexity of the user-interface. The attribute *type* is used to selected between the following:

* ``Structured``: This instructs Amanzi to use BoxLib data structures and an associated paradigm to numerically represent the flow equations.  Data containers in the BoxLib software library, developed by CCSE at LBNL, are based on a hierarchical set of uniform Cartesian grid patches.  ``Structured`` requires that the simulation domain be a single coordinate-aligned rectangle, and that the "base mesh" consists of a logically rectangular set of uniform hexahedral cells.  This option supports a block-structured approach to dynamic mesh refinement, wherein successively refined subregions of the solution are constructed dynamically to track "interesting" features of the evolving solution.  The numerical solution approach implemented under the ``Structured`` framework is highly optimized to exploit regular data and access patterns on massively parallel computing architectures.

* ``Unstructured``: This instructs Amanzi to use data structures provided in the Trilinos software framework.  To the extent possible, the discretization algorithms implemented under this option are largely independent of the shape and connectivity of the underlying cells.  As a result, this option supports an arbitrarily complex computational mesh structure that enables users to work with numerical meshes that can be aligned with geometrically complex man-made or geostatigraphical features.  Under this option, the user typically provides a mesh file that was generated with an external software package.  The following mesh file formats are currently supported: `"Exodus II`".  Amanzi also provides a rudimentary capability to generate regular meshes within the unstructured framework internally.

An example root tag of an input file would look like the following.

.. code-block:: xml

  <amanzi_input version="2.2.1" type="unstructured"/>


Model Description
=================

This allows the users to provide a name and general description of model being developed.  This is also the section in which the units for the problem are stored. This entire section is optional but encouraged as documentation.

.. code-block:: xml

  <model_description name="Name of Model" >
      Required Elements: NONE
      Optional Elements: comment, author, created, modified, model_id, description, purpose, units
  </model_description>

All elements expect string content, except ``units`` which is described below.

Units
-----

The ``units`` element defines the default units to be assumed for the entire input file.  Amanzi's internal default units are SI units.  Conversion from the listed units to Amanzi's internal default units is not yet implemented.  Akuna does allow users to specify units when entering individual values during model setup and tool set definition.  Akuna then translates all user specified units to the Amanzi default units before writing out the Amanzi input file.

``units`` has the optional elements of length, time, mass, and concentration.  Each of those in turn have their own structure.  The structures are as follows.

REMINDER - UNITS ARE NOT IMPLEMENTED YET

.. code-block:: xml

  <units>
      Required Elements: NONE
      Optional Elements: length_unit, time_unit, mass_unit, conc_unit
  </units>

Acceptable values for each unit are as follows:

+----------------+----------------+
| Units Elements | Value Options  |
+================+================+
| length_unit    | m or cm        |
+----------------+----------------+
| time_unit      | y, d, h, or s  |
+----------------+----------------+
| mass_unit      | kg             |
+----------------+----------------+
| conc_unit      | molar, SI      |
+----------------+----------------+

Note, currently mol/m^3 concentration unit is only available for unstructured.  The input converter for unstructured will convert the concentration internally as needed.

Here is an overall example for the model description element.

.. code-block:: xml

  <model_description name="DVZ 3layer 2D">
    <comments>This is a simplified 3-layer DVZ problem in 2D with two cribs (Flow+Transport)</comments>
    <model_name>DVZ 3layer</model_name>
    <author>d3k870</author>
    <units>
      <length_unit>m</length_unit>
      <time_unit>s</time_unit>
      <mass_unit>kg</mass_unit>
      <conc_unit>molar</conc_unit>
    </units>
  </model_description>


Definitions
===========

Definitions allows the user the define and name constants, times, and macros to be used in later sections of the input file.  This is to streamline the look and readability of the input file.  The user should take care not to reuse names within this section or other sections.  This may have unindented consequences.

.. code-block:: xml

  <definitions>
      Required Elements: NONE
      Optional Elements: constants, macros
  </definitions>

Constants
---------

Here the user can define and name constants to be used in other sections of the input file.  Note that if a name is repeated the last read value will be retained and all others will be overwritten.  See `Constants`_ for specifying time units other than seconds.

.. code-block:: xml

  <constants>
      Required Elements: NONE
      Optional Elements: constant, time_constant, numerical_constant, area_mass_flux_constant
  </constants>

A ``constant`` has three attributes ``name``, ``type``, and ``value``.  The user can provide any name, but note it should not be repeated anywhere within the input to avoid confusion.  The available types include: `"none`", `"time`", `"numerical`", and `"area_mass_flux`".  Values assigned to constants of type `"time`" can include known units, otherwise seconds will be assumed as the default. See `Constants`_ for specifying time units other than seconds.

.. code-block:: xml

    <constant name="String" type="none | time | numerical | area_mass_flux" value="constant_value"/>

A ``time_constant`` is a specific form of a constant assuming the constant type is a time.  It takes the attributes ``name`` and ``value`` where the value is a time (time unit optional).

.. code-block:: xml

    <time_constant  name="Name of Time"  value="time,y|d|h|s"/>

A ``numerical_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value``.

.. code-block:: xml

    <numerical_constant name="Name of Numerical Constant" value="value_constant"/>

A ``area_mass_flux_constant`` is a specific form of a constant.  It takes the attributes ``name`` and ``value`` where the value is an area mass flux.

.. code-block:: xml

    <area_mass_flux_constant name="Name of Flux Constant" value="value_of_flux"/>

Macros
------

The ``macros`` section defines time, cycle, and variable macros.  These specify a list or interval for triggering an action, particularly, writing out visualization, checkpoint, walkabout, or observation files.

.. code-block:: xml

  <constants>
      Required Elements: NONE
      Optional Elements: time_macro, cycle_macro, variable_macro [S]
  </constants>


Time_macro
__________

The ``time_macro`` requires an attribute ``name``.  The macro can then either take the form of one or more labeled time subelements or the subelements ``start``, ``timestep_interval``, and ``stop`` again containing labeled times.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.  The labeled times can be time values assuming the default time unit of seconds or including a known time unit.

.. code-block:: xml

  <time_macro name="Name of Macro">
    <time>Value</time>
  </time_macro>

or

.. code-block:: xml

  <time_macro name="Name of Macro">
    <start> TimeValue </start>
    <timestep_interval> TimeIntervalValue </timestep_interval>
    <stop> TimeValue | -1 </stop>
  </time_macro>


Cycle_macro
___________


The ``cycle_macro`` requires an attribute ``name`` and the subelements ``start``, ``timestep_interval``, and ``stop`` with integer values.  A ``stop`` value of -1 will continue the cycle macro until the end of the simulation.

.. code-block:: xml

  <cycle_macro name="Name of Macro">
    <start>Value</start>
    <timestep_interval>Value</timestep_interval>
    <stop>Value|-1</stop>
  </cycle_macro>

Variable_macro
______________

The ``variable_macro`` requires an attribute ``name``  and one or more subelements ``variable`` containing strings.

.. code-block:: xml

  <variable_macro name="Name of Macro">
    <variable> VariableString </variable>
  </variable_macro>


An example ``definition`` section would look as the following:

.. code-block:: xml

  <definitions>
    <constants>
      <constant name="zero"              type="none"           value="0.000"/>
      <constant name ="start"            type="time"           value="1956.0,y"/>
      <constant name ="B-18_release_end" type="time"           value ="1956.3288,y"/>
      <constant name="future_recharge"   type="area_mass_flux" value="1.48666e-6"/>
      <numerical_constant name="zero" value="0.000"/>
    </constants>
    <macros>
      <time_macro name="Macro 1">
        <time>6.17266656E10</time>
        <time>6.172982136E10</time>
        <time>6.173297712E10</time>
        <time>6.3372710016E10</time>
        <time>6.33834396E10</time>
      </time_macro>
      <cycle_macro name = "Every_1000_timesteps">
        <start>0</start>
        <timestep_interval>1000</timestep_interval>
        <stop>-1 </stop>
      </cycle_macro>
    </macros>
  </definitions>
