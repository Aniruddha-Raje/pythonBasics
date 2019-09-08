#List -

#creation
list = ["abc", "pqr"]
list = ["abc", 10, 5.5]
list = ["abc", 1, 2,3, 4, 5]

#Prints entire list
print(list)

#['abc', 1, 2]
print('list[0:3] => ', list[0:3])

#[2, 3, 4, 5]
print('list[2:] => ',list[2:])

#['abc', 1, 2]
print('list[:3] => ',list[:3])

#5
print('list[-1] => ',list[-1])

############################################################
############################################################
############################################################

list1 = [1,2]
list2 = ["abc","pqr"]
list3 = [list1,list2]
print('\nlist3 => ', list3)

#Prints 0th index element
print('\nsearch by index => ', list[0])

#Fetch index of element "abc"
print('find index of an element => ', list.index("abc"))

#Insert value at a specific index
print('list.insert => ',list.insert(0,"ccc"))

#Remove element "ccc"
print('list.remove => ',list.remove("ccc"))

#Add at the end
print('list.append => ',list.append("xyz"))

#Remove first inserted element
print('list.pop => ',list.pop(0))

#Remove last inserted element
print('list.pop => ',list.pop())

#find size of the list
print('length => ', len(list))

#Delete element at index 0
del list[0]
print('\ndel by index => ', list)

#Delete element from 2nd index
del list[2:]
print('del by index => ', list)

#Sort enitre list
list.sort()
print('\nlist.sort => ', list.sort)

#Add multiple values at the end
print('list.extend => ', list.extend(["aaa","bbb"]))

#Copy list contents into list2
list2 = list.copy()
print('list.copy => ', list2)

#Reverse the list
print('list.reverse => ', list.reverse())

#Get occurance count of element "abc"
print('occurance in a list => ',list.count("abc"))

list4 = [1,3,5,8,99,-1]

#Won't work is list is not homogeneous
print('max => ', max(list4))
print('min => ', min(list4))
print('sum => ', sum(list4))