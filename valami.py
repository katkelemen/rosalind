#import random

#l = [random.randint(0,10) for i in range(20)]

l = range(60,80)
m = map(chr , l)
#print dict(zip(l,m))

s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def tr(c): 
	if c == "G":return "C"
	elif c == "C":return "G"
	else:return c

print "".join(map(tr,s))