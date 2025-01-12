import sys

nums = []

for line in sys.stdin:
    nums.append(line.rstrip())


for i in range(len(nums)):
    int_a = int(nums[i].split(" ")[0])
    int_b = int(nums[i].split(" ")[1])
    
    print(len(str(int_a+int_b)))