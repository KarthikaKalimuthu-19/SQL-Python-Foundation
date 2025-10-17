#--dictionary
employee={'e1':'Anish','e2':'vinoth','e3':'mano'}

print(employee)
print(employee.items())
print(employee.keys())
print(employee.values())

#get
print(employee.get('e2'))

#check key
if 'e3' in employee:
    print('e3 is present')

#update
employee.update({'e2':'hariharan'})
print('After modification of dictionary : ',employee)

#--remove pop
employee.pop('e2')
print('After POP of dictionary : ',employee)

#--popitem
employee.popitem()
print('After POPItem of dictionary : ',employee)

#--Add element
employee['e5']='vijay'
print('After adding value  :',employee)










