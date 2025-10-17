try:
    raise NameError('My error: python')
except NameError:
    print('exception my error called')
    raise
