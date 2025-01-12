numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    for num2 in numbers:
        print('{0}x{1}={2}'.format(num, num2, num * num2))
