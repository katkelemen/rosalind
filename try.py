c = 50
# 1. numbers
print range(c)

# 2. even numbers 
print filter (lambda x: not x%2 , range(c))

	 

# 3. numbers divisible by 3
print filter (lambda x: not x%3 , range(c))
	

# 4. numbers as string
#print map(lambda x: str(x), range(c))
print map(str, range(c))

# 5. square of numbers 
print map(lambda x: x**2 , range(c))

# 6. double of numbers divisible by 7
d = filter(lambda x: not x%7, range(c))
print map(lambda x: x*2, d)

l = []
for b in range(0,c,7):
	b = b*2
	l.append(b)
print l
