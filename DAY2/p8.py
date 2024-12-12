import pprint

prod_info={}

prod_info['prodID']=[]
prod_info['prodName']=[]
prod_info['salesCount']=[]

prod_info['prodID'].append('p101')
prod_info['prodID'].append('p102')
prod_info['prodID'].append('p103')

prod_info['prodName'].append('prodA')
prod_info['prodName'].append('prodB')
prod_info['prodName'].append('prodC')

prod_info['salesCount'].append(100)
prod_info['salesCount'].append(200)
prod_info['salesCount'].append(300)

pprint.pprint(prod_info)

wobj = open('products.log','w')

for var in prod_info:
    wobj.write(f'{var}\n')
    for var1 in prod_info[var]:
        wobj.write(f'{var1}\n')
    wobj.write("\n")
wobj.close()

