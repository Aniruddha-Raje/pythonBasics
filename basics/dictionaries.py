'''
Dictionary - 
A dictionary is a collection which is unordered, changeable and indexed.
'''

dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Modify a dictionary
dict["year"] = 2018

#updates or inserts the items to the dictionary
dict.update({"color": "Red", "type":"racing"})

#Copy one dict into another
dict2 =	dict.copy()

#Print values of key "brand"
print(dict.get('brand'))

#Print items as array
print(dict.items())

#Print only Keys
print(dict.keys())

#Print only Values
print(dict.values())

#removes the last item
dict.popitem()

#Delete model from the dictionary
del dict["model"]

#Delete element with "year" key
dict.pop("year")

#Removes all the elements from the dictionary
dict.clear()