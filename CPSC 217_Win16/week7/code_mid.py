n = int(input('Enter an integer:'))

if n <= 0:
	print("Wrong input. Program Terminated......")
else:
	for i in range(1,n+1,1):
		
		prev_value = 0
		
		for j in range(1,i+1,1):
			prev_value = prev_value + j 
			print(prev_value," ", end= '')
		
		print()




