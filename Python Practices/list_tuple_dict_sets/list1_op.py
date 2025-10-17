#--list
list1=['a',123,'vijay',89.3434]

print(list1)
for i in list1:
    print(i)

print('index : ',list1[2])

#---Functions in list
marks=[90,60,50]
print('mark list : ',marks)
marks.append(100)
print('Appended list :   ',marks)

#extend
marks.extend([80,70])
print('Extended New list :   ',marks)

#sort
marks.sort()
print('Sorted new list ',marks)

#-min.max
print('min value in marks list : ',min(marks))
print('max value in marks list : ',max(marks))

#len
print('len ',len(marks))
#count
print('count ',marks.count(60))

#--reverse
marks.reverse()
print(marks)

#edit
marks[1]=20
print('modified list :  ',marks)

#pop
marks.pop()
print('After removal of item ',marks)
marks.pop(1)
print('After removal of item in Position 1 :   ',marks)












