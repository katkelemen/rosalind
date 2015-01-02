# -*- coding: utf8 -*-
lesson = """ett barn [et ba:rn]	child
en flicka [en *flika]	girl
en pojke [*pojke]	boy
ett fönster ['fönster]	window
ett bord [bo:d]	table
en man [man]	man
en kvinna [*kvina]	woman
en bok [bo:k]	book
en telefon [tele'få:n]	telephone
en stol [sto:l]	chair
en dörr [dör]	door
ett vykort [*vy:kot]	postcard
en penna [*pena]	pen(cil)
ett rum [rum]	room
ett badrum [*ba:drum]	bathroom
ett hotell [ho'tel]	hotel
ett frimärke [*fri:märke]	stamp"""
#1 lessondict { "en man": "man" }

pool = lesson.split('\n')
swengdict = {}
for i in range(len(pool)): 
	import re
	line = re.sub(r'\[.*\]', '', pool[i]).split("\t")
	swengdict[line[0].strip()] = line[1]


#2 get_test() ->  <random swedish word> [4 random english, one of them is the answer]

def get_test(k=3):
	vs = swengdict.values()
	import random
	q = random.choice(swengdict.keys())
	rightanswer = swengdict[q]
	answers = [rightanswer]
	vs.remove(rightanswer)
	for i in range(k):
		answer = random.choice(vs)
		answers.append(answer)
		vs.remove(answer)
	random.shuffle(answers)
	return str(q), answers


print get_test()