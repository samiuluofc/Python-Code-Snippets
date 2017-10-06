def power(x,y):
	
	res = 1;
	for ex in range(1,y+1,1):
		res = res * x

	return res,1/res



calcu, inv = power(2,2)
print(calcu,inv)	