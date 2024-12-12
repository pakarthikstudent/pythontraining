'''
Task:10
version:3.13
Author:Mr.Palani Karthikeyan
'''
DBs=['oracle','sql','mysql','plsql']

v = input('Enter a db name:')

if(v in DBs):
    print(f'Yes input db:{v} is exists - index number is:{DBs.index(v)}')
else:
    print(f'Input db:{v} is not exists - will add to DBs')
    DBs.append(v)

print('List of Dbs:')
for var in DBs:
    print(var)
