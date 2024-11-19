from dataclasses import dataclass
from typing import Iterable

def main() -> None:
    # Create an itterable
    countries = ("avi", "tali", "aba", "edit", "shai", "vardit")
    # Create an itterator
    country_iterator = iter(countries)
    # Loop through the itterator
    while True:
        try:
            country = next(country_iterator)        
        except StopIteration:
            break
        else:
            print(country)
    # But when writing code, we will do it like this
    for country in countries:
        print(country)

    # Another usage for iter is that you can iter over the object returned by a function
    with open("countries.txt") as file:
        for line in iter(file.readline, ""):
            print(line, end="")

    line_items = {
        LineItem(1, 2),
        LineItem(1, 3),
        LineItem(1, 4),
    }

    print_totals(line_items)

# Itterables offer a layer of abstruction
@dataclass(frozen=True)
class LineItem:
    price: int
    quantity: int

    def total_price(self) -> int:
        return self.price * self.quantity
    
def print_totals(items: Iterable[LineItem]) -> None:
    for item in items:
        print(item.total_price())
    

if __name__ == "__main__":
    main()