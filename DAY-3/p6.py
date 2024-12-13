import sys
print("one")
print("two")
print("three")
try:
    fobj = open('invalid_File','r')
except Exception:
    print(sys.exc_info())
else:
    s=fobj.read()
    print(s)
    fobj.close()

for v in [1,2,3]:
    print(v)

print("End of the line")
