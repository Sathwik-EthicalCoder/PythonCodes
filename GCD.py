a,b=12,33
for x in range(1,((lambda a,b: (a>b) and a or (b))(a,b))):
	if a%x==0 and b%x==0:
		gcd=x
print(gcd)
