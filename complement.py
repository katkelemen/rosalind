f = open("rosalind_revc.txt", "r")
s = f.readline().strip()

#s = s[::-1]
#s = s.lower()
#s = s.replace('t', 'A')
#s = s.replace('a', 'T')
#s = s.replace('c', 'G')
#s = s.replace('g', 'C')


from string import maketrans
print (s[::-1].translate(maketrans('ACTG', 'TGAC')))
