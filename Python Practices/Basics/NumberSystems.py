#----Number Systems----------

no=10

bin_Res=bin(no)
oct_Res=oct(no)
hex_Res=hex(no)

print('Decimal value   :',no)
print('Binary value   :   ',bin_Res)
print('Octal value   :   ',oct_Res)
print('Hexa value   :   ',hex_Res)

print('----------------------')
#---number type conversions
print('Binary value   :   ',bin_Res)
print('DEcimal  value   :   ',  int(bin_Res,2))  #---base of 2

print('----------------------')
#---number type conversions
print('Octal value   :   ',oct_Res)
print('DEcimal  value   :   ',  int(oct_Res,8))  #---base of 8


print('----------------------')
#---number type conversions
print('Hexa value   :   ',hex_Res)
print('DEcimal  value   :   ',  int(hex_Res,16))  #---base of 16


