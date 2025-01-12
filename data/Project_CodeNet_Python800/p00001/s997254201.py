one  = 0
two = 0
three  = 0
while 1:
	try :
		i = int(raw_input())
		if one<i:
			three=two
			two=one
			one=i
		elif two<i:
			three=two
			two=i
		elif three<i:
			three=i
    	except:
	    	print"%d" % (one)
	    	print"%d" % (two)
	    	print"%d" % (three)
	    	break