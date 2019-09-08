#Iterator -

tuple = ("apple", "banana", "cherry")
str = "Hello"

itr1 = iter(tuple)
itr2 = iter(str)

print('itr1 next => ', next(itr1))
print('itr2 next => ', next(itr2))