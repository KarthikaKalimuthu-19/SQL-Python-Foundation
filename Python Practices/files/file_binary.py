#--binary file

str=b'\x21'
with open('one.txt','wb') as fp:
    fp.write(str)
