'''
Set - 
Collection of unique elements
Order is not guranteed
'''

#Set creation
set = {"aaa", "bbb", "ccc", "aaa"}
print('set => ', set)


#Add element in the set
set.add("ddd")
print('added ddd => ', set)


#Create a new set from existing
set2 = set.copy()
print('copied into set2 ', set2)


#Add multiple elements in a set
set.update(["eee", "fff"])
print('set.update => ', set)


#Return True if all items set are present in set2
set2.issubset(set) 


#Removes value - returns error if value if not found
set.remove("banana")


#Removes value - gracefully handles if value is not found
set.discard("banana")

#Remove element
set.pop()

#Removes all the elements from the set
set.clear()

#Deletes set
del set

#################
#Creates a union of the two sets
set3 = set.union(set2)

#Returns a set, that are the intersection of to other sets
set3 = set.intersection(set2)

#Removes the items in this set that is not present in other, specified set(s)
set.intersection_update(set2)

#Returns elements from set, which are not present in set2
set.difference(set2)

#Removes elements from set, which occured in set2 
set.difference_update(set2)