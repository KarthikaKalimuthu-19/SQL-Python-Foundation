#--Tuple
names=('raj',90,78.45,(10,20))
for i in names:
    print(i)

print('names[3]   : ',names[3])
print('names[3][0]   : ',names[3][0])
print('names[3][1]   : ',names[3][1])

#--concat +
marks=(20,60,90)
new_tuple=names+marks
print('New Tuple : ',new_tuple)

#--multiply *
print('multiply  ',marks*3)

#--check
if  60 in marks:
    print('60 present')
marks[2]=100
