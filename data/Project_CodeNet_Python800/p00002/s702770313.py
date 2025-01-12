import itertools
import operator

dataset = []
while True:
    try:
        dataset.append(input())
    except EOFError:
        break

for item in (sum(int(y) for y in x.split()) for x in dataset):
    print(len(str(item)))