first=0
second=0
third=0

for i in range(10):
    mountain=int(input())
    if mountain>first:
        third=second
        second=first
        first=mountain
    elif mountain>second:
        third=second
        second=mountain
    elif mountain>third:
        third=mountain

print(first)
print(second)
print(third)