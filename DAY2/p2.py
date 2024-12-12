'''
Emp=['101,raj,sales,pune,1000','102,anu,hr,hyd,2000',
     '103,vijay,sales,bglore,3000']
'''
fobj = open('emp.csv','r') 
Emp = fobj.readlines()
fobj.close()

print("Emp_Name Dept")
print("-"*30)
total=0
for var in Emp:
    L=var.split(',') # split str ->list based on , sep
    print(f'{L[1].title()}\t | {L[2].title()}')
    total = total + int(L[-1])
else:
    print('-'*30)
    print(f"Sum of Emp's Cost:{total}")
    print('-'*30)
