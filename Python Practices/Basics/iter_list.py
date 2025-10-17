a=[1,2,3,4]

for iterator in a:
    print(iterator)


iterator=iter(a)
print('--------------')

print(next(iterator))
print(next(iterator))
print(next(iterator))

