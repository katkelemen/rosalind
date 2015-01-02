s = 'adYvA8QEBNpmInevTamiasVjnSTy4fuHmhSzjlAehJDfuPK5z99ieA4ugr1732GWX49SVserpentinaSxjhrTzN64Fu0JinAV2EtlzUEvXNpDTRoXyowzBLNYePKlZMOr1W8R0C2syPkwlGvVgCvmuxmLb9TmMeROk4IwE6Fmos0H8JY5W3PHHr.'

r = s[16:22] + ' ' + s[69:79]

print r

f = open("rosalind_ini3.txt")
s = f.readline()
r = f.readline().split(" ")
a,b,c,d = map(int,r)

print s[a:b+1] + ' ' + s[c:d+1]




