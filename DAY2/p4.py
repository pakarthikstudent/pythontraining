wobj = open("sales.csv","w") # create a new sales.csv file

fobj = open("emp.csv","r") # open an existing emp.csv file

L = fobj.readlines() # read a emp.csv contents to list

for var in L: # iterate list of items one by one (line by line)
   if('sales' in var):  # test/filter sales dept list
       wobj.write(var)  # write data(sales details) to FILE

fobj.close()
wobj.close()
