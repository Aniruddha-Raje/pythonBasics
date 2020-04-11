from random import randint
from random import shuffle

# In operator
in_data = "x" in ['x', 'y', 'z']
print(in_data)

in_data2 = "a" in ['x', 'y', 'z']
print(in_data2)

# MIN and MAX operator
lis = [10, 5, 12, 2, 1, 100]
print("Maximum value from the List:", max(lis))
print("Minimum value from the List:", min(lis))

# Random Opeator
random_list = [10, 5, 12, 2, 1, 100]
shuffle(random_list)
print("Random Number from shuffle:", random_list)

# Random Integer
x = randint(0, 20)
print(x)

# Range Operator -
x = range(0, 10)
print(x)