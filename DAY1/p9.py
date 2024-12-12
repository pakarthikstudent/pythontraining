hosts = [] # empty list

print(f'Total no.of hosts:{len(hosts)}')

c=0
while(c < 5):
    h = input('Enter a hostname:')
    hosts.append(h)
    c=c+1

print('\nList of host:')

for var in hosts:
    print(var)
else:
    print(f'Total no.of hosts:{len(hosts)}')
