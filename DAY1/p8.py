pin = 1234
count = 0
while(count < 3):
    p = input('Enter a pin Number:')
    count = count + 1
    if(int(p) == pin):
        print(f'Success - pin is matched -{count}')
        break # exit from loop

if(int(p) != pin):
    print('Sorry your pin is blocked')
