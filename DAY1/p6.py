sh_name = input('Enter a shell name:')
if(sh_name == 'bash'):
	fname = 'bashrc'
elif(sh_name == 'ksh'):
	fname = 'kshrc'
elif(sh_name == 'csh'):
	fname = 'cshrc'
else:
	sh_name = 'nologin'
	fname = '/etc/profile'

print(f'shell name is:{sh_name} and profile file name is:{fname}')
