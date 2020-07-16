import math

# https://realpython.com/instance-class-and-static-methods-demystified/
class Pizza:
    def __init__( self, radius, ingredients ):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__( self ):
        return f'Pizza( {self.ingredients!r} )'

    def area( self ):
        return self.circle_area( self.radius )

    @staticmethod
    def circle_area( r ):
        return r ** 2 * math.pi


print( "Pizza( 1, ['cheese', 'tomatoes'] ) = %s" % Pizza( 1, ['cheese', 'tomatoes'] ) )
print( "Pizza( 1, ['mozzarella', 'tomatoes'] ) = %s" % Pizza( 1, ['mozzarella', 'tomatoes'] ) )
print( "Pizza( 1, ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] = %s" % Pizza( 1, ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] ) )
print( "Pizza( 1, ['mozzarella'] * 4 = %s" % Pizza( 1, ['mozzarella'] * 4 ) )

p = Pizza( 1, ['mozzarella', 'tomatoes'] )
print( "p.area( ) = %s" % p.area( ) )

# l127914@pn1249300.lanl.gov:class II $ python pizza_II.py
# Pizza( 1, ['cheese', 'tomatoes'] ) = Pizza( ['cheese', 'tomatoes'] )
# Pizza( 1, ['mozzarella', 'tomatoes'] ) = Pizza( ['mozzarella', 'tomatoes'] )
# Pizza( 1, ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] = Pizza( ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] )
# Pizza( 1, ['mozzarella'] * 4 = Pizza( ['mozzarella', 'mozzarella', 'mozzarella', 'mozzarella'] )
# p.area( ) = 3.141592653589793

# l127914@pn1249300.lanl.gov:class II $ date
# Thu Dec  6 13:20:40 MST 2018

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II
