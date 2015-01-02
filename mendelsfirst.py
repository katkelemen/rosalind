k = 30.0               #homozygous dominant
m = 27.0              #heterozygous
n = 18.0              #homozygous recessive

s = k + m + n

pr = k/s + m/s*k/(s-1) + m/s*(m-1)/(s-1)*0.75 + m/s*n/(s-1)*0.5 + n/s*k/(s-1) + n/s*m/(s-1)*0.5

print pr