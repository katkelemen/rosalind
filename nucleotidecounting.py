f = open("rosalind_dna.txt", "r")
s = f.readline().strip()

d = {}
for i in range(len(s)):
	if s[i] in d:
		d[s[i]] = d[s[i]] + 1
	else: d[s[i]] = 1

print d['A'], d['C'], d['G'], d['T']