lista = ((open("rosalind_subs.txt", "r")).read()).split('\n')

s = lista[0]
t = lista[1]

startindex = 0
tindex = 0
while tindex != -1:
	tindex = s.find(t, startindex)
	startindex = tindex + 1
	if tindex != -1:
		print  tindex + 1
