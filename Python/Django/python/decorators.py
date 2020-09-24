s = "I am a global variable"

def func(s):
    #local variable perceeds global vars
    # global s # will set the value of the local var to the global
    # s = 'I am a local variable'
    print(locals()) # prints a dict with all local variables
    print(globals()) # prints a dict with all global variables
    
    return(s)
print(func(s))

# Decorator example


def new_decorator(func):

    def wrap_func():
        print('code here before executation')
        func()
        print('code here after execution')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('this func is in need of a decorator')

# the @new_decorator replaces the commented line below
# func_needs_decorator = new_decorator(func_needs_decorator)
