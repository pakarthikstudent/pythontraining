n = input('Enter n value:')

if(n.isdigit()):
	n=int(n)+100
	print(f'Incremented n value is:{n}')
else:
	print(f'Sorry input n value {n} is not a digit format')
