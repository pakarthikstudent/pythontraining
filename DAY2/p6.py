import pprint

d={}

d['K1']=[{'url':'abc.com','port':80,'IP':'1.2.3.4'},{'url':'xyz.com','port':90,'IP':'10.20.30.40'}]

d['K2']=[{'K1':[1,2,3,{'K1':[15,25]}]}]

#print(d)

pprint.pprint(d)
print(d['K1'][1]['port'])
