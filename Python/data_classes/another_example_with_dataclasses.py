import random
import string
from dataclasses import dataclass, field
from typing import List

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

# since python 3.10 we can add a kw_only=True to the dataclass decorator and this will make the user pass the values as key word arguments
# since python 3.10 we can also add to the decorator slots=Ture, this will increase performnace by 20% instead of __dict__ but it won't work when using
# multiple inheritance

@dataclass # data classes is generating both __init__ and __str__ method automatically for us
class Person: 
    name: str
    address: str
    active: bool = True
    email_address: List[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False) # this field won't be initialized so we can use a post init method to still get it initialized
    # we do not allow to initialize when we don't want the possibility to allow this field to be initialized

    def __post_init__(self):
        self._search_string = f'{self.name} {self.address}'

def main() -> None:
    person = Person(name='john', address='123 main street', email_address = ['avi@rapyd.net', 'dora@rapyd.net']) # if you provided a value to the field, the default value is ignored
    print(person)
    print(person.__dict__)

if __name__ == '__main__':
    main()