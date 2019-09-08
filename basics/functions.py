# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Aniruddha'):
    print(f'Hello {name}')

sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print('get Sum =>',getSum(1,2))

############################################################
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum2 = lambda num1, num2: num1 + num2

print('getSum2 => ',getSum2(10, 3))

############################################################

def my_function(name, lang = "Python"):
	print("Hello! " + name + ", You are learning " + lang)
	return "Function finished!"

print(my_function("Aniruddha"))