#--generators

def simpleGenerator():
    yield 'hexaware'
    yield 2
    yield 'a'

for i in simpleGenerator():
    print(i)

