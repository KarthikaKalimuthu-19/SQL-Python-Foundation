#--String Functions
a=10
s=str(a)
print('String value : ',s)

s1="cse "
s2="IT "
print('concated string ',(s1+s2))

#---join
s3="computer "
s4="  , ".join(s3)
print("join result  : ",s4)

s6="ABC             "
print('strip : ',s6.strip())
print('lower   :  ',s6.lower())
print('upper : ',s1.upper())
print('replace : ',s1.replace('s','a'))

str1="cse it ece eee"
print(str1.split(' '))
print(str1.find('t'))
