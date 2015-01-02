f = open("rosalind_rna.txt", "r")
s = f.readline().strip()

d = s.replace('T', 'U')
print d