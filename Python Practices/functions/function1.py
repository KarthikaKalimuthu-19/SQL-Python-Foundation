#1.function with parameter with return value

def fun_return_add(a,b):
    c=a+b
    return c

res=fun_return_add(2,3)
print('Result :',res)

#2.function without parameter with return value

def fun_sub():
    a=10
    b=5
    c=a-b
    return c

res1=fun_sub()
print('Subtrction result :',res1)

#3. func with para without return

def fun_mul(a,b):
    c=a*b
    print('Multiplication result :',c)

fun_mul(2,4)

#4. func without para without return

def fun_div():
    a=10
    b=2
    c=a/b
    print('Division result :',c)

fun_div()
