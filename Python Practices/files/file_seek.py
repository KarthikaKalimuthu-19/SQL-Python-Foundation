#--read

fp=open('one.txt','r')
fp.seek(5)    #--from which position we want to show
print(fp.tell()) #--it will tell from which position it will give the result
print(fp.read())
fp.close()

