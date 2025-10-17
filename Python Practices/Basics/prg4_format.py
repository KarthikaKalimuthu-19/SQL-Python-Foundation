#--formats--

price=100.56
item='jeans'
qty=5

order=" order the item: {} of quantity :{} with price : {} "

print(order.format(item,qty,price))

#---index with format
order=" order the item: {2} of quantity :{0} with price : {1} "
print(order.format(item,qty,price))


#--named index format

order=" order the item: {a} of quantity :{b} with price : {c} "
print(order.format(a="mobile",b=9,c=20000))
