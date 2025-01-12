import itertools

for ( i, j ) in itertools.product ( range ( 1, 10 ), range ( 1, 10 ) ):
  print ( "%sx%s=%s" % ( i, j, i * j ) )