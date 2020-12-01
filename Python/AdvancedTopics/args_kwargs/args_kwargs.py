def foo(x, *args, **kwargs):
    print(x)
    if (args):
        print(args)
    if (kwargs):
        print(kwargs)

foo('this is a required argument')

foo('this is a required argument', 'and an arg')

foo('this is a required argument', 'and an arg', key='and a kwarg')