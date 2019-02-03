# https://python.swaroopch.com/oop.html

class Person:
    def __init__( self, name ):
        self.name = name

    def say_hi( self ):
        print( 'Hello, my name is', self.name )

p = Person( 'Swaroop' )
p.say_hi( )

# dantopa@Lax-Millgram:class $ date
# Tue Nov 20 21:07:26 MST 2018

# dantopa@Lax-Millgram:class $ pwd
# /Users/dantopa/Documents/GitHub/topa-development/python/class

# dantopa@Lax-Millgram:class $ py oop_init.py
# Hello, my name is Swaroop
