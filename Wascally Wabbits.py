#n(month)<=40 and k(pairs)<=5

def fibok(n,k):
    if n == 1 or n == 0:
        return 1
    else:
        return fibok(n-1,k) + fibok(n-2,k) * k
n = 28 
k = 4
print fibok(n-1,k)


