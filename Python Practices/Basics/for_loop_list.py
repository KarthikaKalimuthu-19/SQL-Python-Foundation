
num=int(input('Enter the number :'))
sum=0
for i in range(1,num+1):
    sum=sum+i
print('Sum of natural numbers :',sum)

print('-----------------------------------------------')


a=[]
print('Enter ten numbers')
sum=0
for i in range(1,11):
    num=int(input('Enter num '+str(i)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print('Sum :',sum)
print('Avg :',sum/10)

print('-----------------------------------------------')


num=int(input('enter the number :'))

for i in range(1,num+1):
    print('Number is :',i ,'and Cube of the',i,'is',i*i*i)
    
    


