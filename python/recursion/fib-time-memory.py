from timeit import Timer
from fibonacci import fib

t1 = Timer( "fibi( 10 )", "from fibonacci import fib" )

for i in range( 1,30 ):
	s = "fibm(" + str(i) + ")"
	t1 = Timer( s, "from fibonacci import fibm" )
	time1 = t1.timeit( 3 )
	s = "fibr(" + str(i) + ")"
	t2 = Timer( s, "from fibonacci import fibi" )
	time2 = t2.timeit( 3 )
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))
