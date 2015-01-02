f = open("rosalind_ini6.txt", "r")
s = f.readline().strip()

#s = "We tried list and we tried dicts also we tried Zen"
spl = s.split(" ")
d = {}
for i in range (len(spl)):
	if spl[i] in d:
		d[spl[i]] = d[spl[i]] + 1
	else:
		d[spl[i]] = 1 

for i,j in d.iteritems():
	print i, j
