mark1={88,22,33}
mark2={11,22,44}

print('mark 1',mark1)
print('mark 2',mark2)

#1.union

union_set=mark1 | mark2
print('Union result :',union_set)

#2.intersection

intersect_res=mark1 & mark2
print('Intersect result :',intersect_res)

#3.difference

diff_res=mark1 - mark2
print('Difference result :',diff_res)

#4.symmetric difference

symm_diff=mark1 ^ mark2
print('Symmetric Difference result :',symm_diff)
