for n in range(1,10):
  for i in range(1, 10):
    print('{}x{}={}'.format(n, i, eval('{}*{}'.format(n, i))))