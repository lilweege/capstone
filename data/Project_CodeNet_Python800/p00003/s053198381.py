for i in range ( int ( input ( ) ) ):
  ( a, b, c ) = sorted ( list ( map ( int, input ( ).split ( ) ) ) )
  if ( a ** 2 ) + ( b ** 2 ) == ( c ** 2 ):
    print ( "YES" )
  else:
    print ( "NO" )