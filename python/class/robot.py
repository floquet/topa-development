# https://python.swaroopch.com/oop.html

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    # constructor
    def __init__( self, name ):
        """Initializes the data."""
        self.name = name
        print( "(Initializing {})".format( self.name ) )

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die( self ):
        """I am dying."""
        print( "{} is being destroyed!".format( self.name ) )

        Robot.population -= 1

        if Robot.population == 0:
            print( "{} was the last one.".format( self.name ) )
        else:
            print( "There are still {:d} robots working.".format( Robot.population ) )

    def say_hi( self ):
        """Greeting by the robot.

        Yeah, they can do that."""
        print( "Greetings, my masters call me {}.".format( self.name ) )

    @classmethod
    def how_many( cls ):
        """Prints the current population."""
        print( "We have {:d} robots.".format( cls.population ) )

# instantiate droids
droid1 = Robot( "R2-D2" )
droid1.say_hi( )
Robot.how_many( )

droid2 = Robot( "C-3PO" )
droid2.say_hi( )
Robot.how_many( )

# work period
print( "\nRobots can do some work here.\n" )

# clean up
print( "Robots have finished their work. So let's destroy them." )
droid1.die( )
droid2.die( )

# verify they're all gone
Robot.how_many()

# dantopa@Lax-Millgram:class $ date
# Tue Nov 20 21:08:00 MST 2018

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/class

# dantopa@Lax-Millgram:class $ py robot.py
# (Initializing R2-D2)
# Greetings, my masters call me R2-D2.
# We have 1 robots.
# (Initializing C-3PO)
# Greetings, my masters call me C-3PO.
# We have 2 robots.
#
# Robots can do some work here.
#
# Robots have finished their work. So let's destroy them.
# R2-D2 is being destroyed!
# There are still 1 robots working.
# C-3PO is being destroyed!
# C-3PO was the last one.
# We have 0 robots.
