# class is the collection methods,attributes and properties
# object - object is an istance of a class

# all classes have function __init__(), which is always executed when the class is being Initiated
# use of __init__() function to assign a value to object properties.

#Class -
class Person:
	def __init__(self, name, age):
    		self.name = name
    		self.age = age

    def display(self):
		print("Name => " + self.name +"\n Age => " + self.age)


p = Person("Aniruddha", 26)
p.age = 27
p.display()
del p