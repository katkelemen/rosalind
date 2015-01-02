li = [1,2,3,4,5,5,6]



print map(lambda x: x, li)
print map(lambda x: x * 2, li)
print map(int, li)
print map(str, li)


#this is the same as 
def doubleme(n): return n * 2
print map(doubleme, li)
#this
print map(lambda x: x*2, li)




print int(34.4)