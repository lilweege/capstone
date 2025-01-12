while True:
   try :
      a, b=[int(x) for x in input().split()]
      ans = a+b
      ans = str(ans)
      size = len(ans)
      print(size)
   except EOFError:
      break
