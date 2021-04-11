'''
Tuple -
It is immutable(cannot be changed) unlike list
Index starts from 1 instead of 0
'''

tup = 1, 2, 3
# unpacking
a, b, c = tup
print(a * b * c)

# Tuple creation
tuple = (1, 2, 3)
print(tuple)

# Get index of a value
print('find by index => ', tuple.index(1))

# Get occurances of a value
print('find occurances => ', tuple.count(1))

# Tuple deletion
del tuple
