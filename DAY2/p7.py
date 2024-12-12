import time

wobj = open("pin_history.log","a")

pin = 1234
count = 0
while(count < 3):
    p = input('Enter a pin Number:')
    count = count + 1
    if(int(p) == pin):
        wobj.write(f'Success - pin is matched - {count} ')
        wobj.write(f'Pin Entry Time is:{time.ctime()}\n')
        print(f'Success - pin is matched -{count}')
        break # exit from loop
    else:
        wobj.write(f'Failed - user input pin:{p}')
        wobj.write(f'Pin Entry Time is:{time.ctime()}\n')

if(int(p) != pin):
    wobj.write('Blocked-Your max input limit crossed\n')
    print('Sorry your pin is blocked')


wobj.close()
