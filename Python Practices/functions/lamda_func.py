#--Lambda: Asunchronous function: map,filter,reduce
#using non-block code" db op, file op, queries

result=lambda a:a*10
print(result(5))

mul=lambda a,b,c:a*b*c
print(mul(2,5,6))

#map

salary=[10000,20025,45000,60000]
inc_res=list(map(lambda x:x+1000,salary))
print('Incremented salary :',inc_res)

#filter

fil=list(filter(lambda x:x%2!=0,salary))
print('Filtered salary :',fil)

#reduce
from functools import reduce

red=reduce(lambda x,y:x+y,salary)
print('Total salary :',red)


min_sal=reduce(lambda x,y:x if x<y else y,salary)
print('Minimum salary :',min_sal)
         
