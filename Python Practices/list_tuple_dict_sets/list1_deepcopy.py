#--deep copy
import copy

list1=[10,20,90,30]
list2=copy.deepcopy(list1)

print('list 1 :',list1)
print('list 2 :',list2)

list1[2]=100

print('After modification ')
print('list 1 :',list1)
print('list 2 :',list2)


