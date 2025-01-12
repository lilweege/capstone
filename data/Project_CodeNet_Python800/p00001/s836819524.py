# coding: utf-8
mountain = [int(input()) for i in range(10)]
for i in range(3):
    print(max(mountain))
    mountain.remove(max(mountain))