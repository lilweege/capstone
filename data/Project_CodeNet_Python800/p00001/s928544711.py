firstMountainHeight  = 0
secondMountainHeight = 0
thirdMountainHeight  = 0

while 1:

	try :

		i = int(raw_input())

		if firstMountainHeight    < i :
			thirdMountainHeight  = secondMountainHeight
			secondMountainHeight = firstMountainHeight
			firstMountainHeight  = i

		elif secondMountainHeight < i :
			thirdMountainHeight  = secondMountainHeight
			secondMountainHeight = i
			
		elif thirdMountainHeight  < i :
			thirdMountainHeight   = i
			
    	except:
	    	print"%d" % (firstMountainHeight)
	    	print"%d" % (secondMountainHeight)
	    	print"%d" % (thirdMountainHeight)

	    	break