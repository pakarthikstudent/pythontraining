products={} # empty dict

while(True):
	pid = input('Enter a productid:')
	if pid in products:
		print(f'Usage:Input productID:{pid} is already exists')
	else:
		pname = input('Enter a productName:')
		products[pid] = pname # adding new data to an existing dict
	
	choice = input('Wish to exit type Yes or press Y:')
	if(choice == 'Yes' or choice == 'Y'):
		break # exit from loop

print("List of product details:-")
print("-"*30)

for var in products:
	print(f'{var}\t{products[var]}')
