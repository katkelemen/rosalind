#def evenlines(a):
f = open('rosalind_ini5.txt', 'r')

l = f.readlines()



#for i in range (1,len(l),2):
#	print l[i]

for i in range (len(l)):
	if i % 2: print l[i]

#i = 0
#for line in f:
#	if i % 2: print line
#	i = i + 1
