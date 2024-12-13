print("one")
print("two")
print("three")
try:
    print(var)
except NameError:
    print("Undefined variable")
else:
    print("There is no error")

for v in [1,2,3]:
    print(v)

print("End of the line")
