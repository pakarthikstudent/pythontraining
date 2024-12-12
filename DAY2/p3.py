prod_list = ['p101,prodA,1000','p102,prodB,2000',
             'p103,prodC,3000']

# create a new prod.csv file
# write prod_list details to prod.csv file (same format)
# <prodid>  <prodName> <pcost>

wobj = open('prod.csv','w') # create a new prod.csv file

for var in prod_list:
    wobj.write(var+"\n") # write data to file(prod.csv)

wobj.close()
