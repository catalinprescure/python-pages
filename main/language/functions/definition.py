# A function is a named sequence of statements.
#
# A function definition specifies the name and the statements.
# Expression in parantheses is called the argument
#
# To end the function, you have to enter an empty line.
# Statements inside a function don't run until the function is called

def myfunc(a): 
    return a%2

print (myfunc(3))


# In Python, there is value called None
# which represents the absence of a value

def myprint(x):
    print(x)
    return

assert myprint("2") == None # pass