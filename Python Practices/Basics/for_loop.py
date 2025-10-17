#---for loop


num=int(input('Enter the number :'))
print('Multiplications of your number:', num)
for i in range(1,11):
    mul=num*i
    print('{}*{}={}'.format(i,num,mul))

print('-----------------------------------------------')


num1=int(input('enter the num 1 :'))
num2=int(input('enter the num 2 :'))

for i in range(num1+1,num2):
  print (i)

print('-----------------------------------------------')

#---count---

count1=0
count2=0
for i in range(1,11):
    if i%2==0:
        print(i)
        count1=count1+1
    else:
        print(i)
        count2=count2+1
print('Count of even :',count1)
print('Count of odd :',count2)

print('-----------------------------------------------')
    
count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
        count=count+1
print('Count of div_3 and 5:',count)









        






