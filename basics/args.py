# The Special syntax *args in function definations
# in used for pass a variable as no of arguments to a function


def myfunct(*argv):
    for args in argv:
        print(args)

myfunct('Hellow', 'Welcome', 'to', 'GreektoGreek')

############################################################

def myfuncts(args, *argss):
    print("First argument is:", args)
    
    for arg in argss:
        print("Next argument is:", arg)

myfuncts('Hellow', 'Welcome', 'to', 'GreektoGreek')