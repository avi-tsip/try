# This file shows what is the result when not using data classes

class Person:
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

person1 = Person("avi", "dev-ops", 32)
person2 = Person("moshe", "qa", 46)
person3 = Person("moshe", "qa", 46)

print(id(person2))
print(id(person3))
print(person1)

print (person3 == person2)