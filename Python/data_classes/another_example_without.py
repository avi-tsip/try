import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return(f"{self.name}, {self.address}")
    
def main() -> None:
    person = Person(name='john', address='123 main street')
    print(person)

if __name__ == '__main__':
    main()