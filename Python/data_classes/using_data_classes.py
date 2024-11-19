from  dataclasses import dataclass, field

@dataclass(order=True, frozen=True) # when using the dataclass decorator, we don't need to use the init function to initialize our data
                                    # frozen means that the attributes are read only and cannot be changed after initialization
class Person:
    sort_index: int = field(init=False, repr=False) # do not initialize this attribute and do not print it when printing hte values of the object
    name: str
    job: str
    age: int
    strength: int = 100 # add a default value for this attribute

    def __post_init__(self):
        # self.sort_index = self.age - can't be used when frozen = True
        object.__setattr__(self, 'sort_index', self.age) # allows to circumvent the frozen = true

    def __str__(self):
        return f'(Person object - {self.name} is an {self.job} and is {self.age} years old)'

person1 = Person("avi", "dev-ops", 32, 99)
person2 = Person("moshe", "qa", 46)
person3 = Person("moshe", "qa", 46)

print(id(person2))
print(id(person3))
print(person1)

print(person1 > person2)
print (person3 == person2)