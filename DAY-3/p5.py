import sys
print("one")
print("two")
print("three")
try:
    v=[1,2,3]
    print(v[5])
except Exception:
    print(sys.exc_info())
else:
    print("There is no error")

for v in [1,2,3]:
    print(v)

print("End of the line")
