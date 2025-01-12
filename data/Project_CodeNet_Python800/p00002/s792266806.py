answers=[]
while True:
    try:
        nums=input().split()
        answers.append(len(str(int(nums[0])+int(nums[1]))))
    except :
        break
for i in range(len(answers)):
    print(answers[i])