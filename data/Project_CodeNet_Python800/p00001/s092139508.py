lis = [ ]
for i in range ( 10 ):
  lis.append ( int ( input ( ) ) )
lis.sort ( )
for i in range ( 3 ):
  print ( lis.pop ( ) )