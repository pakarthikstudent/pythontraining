import sys

try:
    n = input('Enter n value:')
    if(int(n) <100):
        raise ValueError('Sorry n value is not above 100')
except Exception:
    print(sys.exc_info())
else:
    print(f'Given n value:{n} - {int(n)+100}')

for v in [1,2,3,4]:
    print('test message:'+str(v))

print('End of the line')
