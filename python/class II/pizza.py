# https://realpython.com/instance-class-and-static-methods-demystified/
class Pizza:
    def __init__( self, ingredients ):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza( {self.ingredients!r} )'

    @classmethod
    def margherita(cls):
        return cls( ['mozzarella', 'tomatoes'] )

    @classmethod
    def prosciutto(cls):
        return cls( ['mozzarella', 'tomatoes', 'ham'] )

#  ==   ==   == ==   ==   == ==   ==   == ==   ==   ==  #

if __name__ == "__main__":

    print( "Pizza( ['cheese', 'tomatoes'] ) = %s" % Pizza( ['cheese', 'tomatoes'] ) )
    print( "Pizza( ['mozzarella', 'tomatoes'] ) = %s" % Pizza( ['mozzarella', 'tomatoes'] ) )
    print( "Pizza( ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] = %s" % Pizza( ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] ) )
    print( "Pizza( ['mozzarella'] * 4 = %s" % Pizza( ['mozzarella'] * 4 ) )
    print( "Pizza.margherita( ) = %s" % Pizza.margherita( ) )
    print( "Pizza.prosciutto( ) = %s" % Pizza.prosciutto( ))

# l127914@pn1249300.lanl.gov:class II $ python pizza.py
# Pizza( ['cheese', 'tomatoes'] ) = Pizza( ['cheese', 'tomatoes'] )
# Pizza( ['mozzarella', 'tomatoes'] ) = Pizza( ['mozzarella', 'tomatoes'] )
# Pizza( ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] = Pizza( ['mozzarella', 'tomatoes', 'ham', 'mushrooms'] )
# Pizza( ['mozzarella'] * 4 = Pizza( ['mozzarella', 'mozzarella', 'mozzarella', 'mozzarella'] )
# Pizza.margherita( ) = Pizza( ['mozzarella', 'tomatoes'] )
# Pizza.prosciutto( ) = Pizza( ['mozzarella', 'tomatoes', 'ham'] )

# l127914@pn1249300.lanl.gov:class II $ date
# Thu Dec  6 13:15:21 MST 2018

# l127914@pn1249300.lanl.gov:class II $ pwd
# /Volumes/Tlaltecuhtli/repos/GitHub/topa-development/python/class II
