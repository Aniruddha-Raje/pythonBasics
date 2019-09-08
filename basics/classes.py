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