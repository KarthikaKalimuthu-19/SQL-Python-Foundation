from functools import reduce

Tickets=[]
price=100

def get_input():
    n=int(input('Enter the no of tickets :'))
    for i in range (n):
        name=input('Enter your name :')
        age=int(input('Enter your age :'))
        gender=input('Enter your gender :')
        
                
        Tickets.append([name,age,gender])

def calculate():
    total=0
    for i in range(len(Tickets)):
        age=Tickets[i][1]
        if age>60 and age<5:
            Price=price*0.5
        else:
            Price=price
    Tickets[i].append(price)
    total=total+price
    print('Total amount after concession :',total)

def display1():
    print('\n-----------Ticket info-----------')
    for i in Tickets:
        print('Name :', i[0], 'Age :',i[1], 'Gender :',i[2], 'price :',i[3])

def display2():
    max_age=reduce(lambda x,y: x if x>y else y,(map(lambda x:x[1],Tickets)))
    inc_age=list(map(lambda t:t[1]+2,Tickets))

get_input()
calculate()
display1()
display2()
