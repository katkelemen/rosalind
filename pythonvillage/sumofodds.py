def sumofodds(a,b):
	oddsum = 0
	for i in range(a,b+1):
		if not i % 2 == 0:
			oddsum = oddsum + i
	print oddsum

sumofodds(4616,8965)

