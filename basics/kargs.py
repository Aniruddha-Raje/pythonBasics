def funct(**kwargs):
    for key, values in kwargs.items():
        print(key, values)

funct(first="Amit", second="hemant")

# *args and **kwargs both use in one function


def functs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ('Amit', 'Arvind', 'Patil')
functs(*args)

kwargs = {"arg1": "Amit", "arg2": "Arvind", "arg3": "patil"}
functs(**kwargs)