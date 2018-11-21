#! /Volumes/Tlaltecuhtli/local/anaconda/anaconda3/bin/python

# # Read Amanzi *.rst files, extract header hierarchy

# # Daniel Topa
# # dantopa@lanl.gov
# # 505 667 0817

# # imports
import os           # probe, change directories
import sys          # python version
import datetime     # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

# # program blocks
def rst_file_harvest( ):
    pass

def rst_file_process( ):
    pass

def publish( ):
    pass

def emulate_process( ):
    pass

def session_tag( ):
    # forensic data
    print( "\npython version")
    print( sys.version )

    print( "\nfile:     ", os.path.basename( __file__ ) )
    print(   "directory:", os.getcwd( ) )
    
    print( datetime.datetime.now( ) )


# #    # #    # #    # #    # #    # #

if __name__ == "__main__":


    rst_file_harvest( )
    rst_file_process( )
    publish( )
    session_tag( )
