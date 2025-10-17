#function keyword

def employee(eid,ename):
    print('E_ID :',eid)
    print('E_Name :',ename)

employee(eid='e1',ename='karthika')


#function keyword with *args(keyword)-we can pass multiple values with single parameter

def marks(*args):
    print(args)

marks(10,20,30,40)

#function keyword with **args(keyword)-we can pass multiple values with multiple parameterss

def marks_args(**args):
    print(args)

marks_args(id=1,name='vino',age=90)
