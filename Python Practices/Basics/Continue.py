
sum=0
i=1

while i<=5:
    no=int(input('Enter the number :'))
    if no<0:
        print('Negative value')
        continue
    else:
        sum=sum+no
    i=i+1


print('sum : ',sum)
        
