app = input('Enter an app name:')
if( app == 'flask' or app == 'fastapi'):
	port = input(f'Enter a {app} port number:')
	print(f'App name is:{app} running port number is:{port}')
else:
	print(f'Sorry inputApp {app} is not matched')
	exit() # exit from python execution
