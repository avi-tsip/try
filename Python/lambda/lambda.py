# regular way

def f(x):
    return 3*x + 1

# the lambda way
g = lambda x: 3*x + 1

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

no_name_example = some_list.sort(key=lambda name: name.split(" ")[-1].lower())

# lambdas inside a function

def quadratic_function(a,b,c):
    return lambda x: a*x**2 + b*x + c

# this is how you call a function with a labmda inside it with vars 
quadratic_function(1,2,3)(0)