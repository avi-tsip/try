from functools import wraps

def mapper(fnc):

    @wraps(fnc)
    def inner(list_of_names):
        """This is the inner func"""
        return [fnc(value) for value in list_of_names]
    return inner

@mapper
def camelCase(name):
    """Turn regular names into camelcase names"""
    return ''.join([word.capitalize() for word in name.split('_')])

names = [
    'avi_tsip',
    'vardit_harel',
    'met_allica'
]

print(camelCase(names))
print(camelCase.__doc__)