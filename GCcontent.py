f = open("rosalind_gc.txt", "r")
lines = f.readlines()
ids = []
cgs = []


def szazalek(s):
	cgdb = 0
	for i in range (len(s)):
		if s[i] == "C" or s[i] =="G":
			cgdb = cgdb + 1
	l = len(s)
	return float(cgdb) / float(l) * 100

for line in lines:
	if line[0] == '>':
		ids.append(line[1:-1])
	else:
		i = len(ids)
		g = len(cgs)
		if i == g:
			cgs[-1] = cgs[-1]+line.strip()
		else:
			cgs.append(line[:-1])
maxi = 0
v = 0
for elem in range(len(cgs)):
	p = szazalek(cgs[elem])
	if p > v:
		v = p
		maxi = elem
print ids[maxi] 
print v
