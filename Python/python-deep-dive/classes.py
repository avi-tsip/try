class MyClass:
    # class attributes
    language = 'python'
    version = '3.6'

# two ways to get class attributes
print(getattr(MyClass, 'language', 'python')) # the thirs var is a default value in case the attribute does not exist
print(MyClass.language)

# two ways to set an attribute
setattr(MyClass, 'language', 'java') # if the attibute exist, the value will be update. If it doesn't exist, a new attribute will be created
MyClass.language = 'java' 

print(MyClass.__dict__) # all attributes are stored in a dict 

# two ways to remove an attribute:
delattr(MyClass, 'language')
del MyClass.version