import csv
import random


class LocatesDistributer:

    def __init__(self):
        self.demanded_locates = {}
        self.symbol_list = ['QQQ', 'GOOG', 'YOO', 'ABC', 'TTT']
        self.supply_locates = {}

    def generate_demand_csv(self, num_of_clients: int):
        with open('results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for client in range(1, num_of_clients):
                writer.writerow([f"Client{client}", f"{random.choice(self.symbol_list)}", f"{random.randint(1, 6)*100}"])

    def requested_locates(self):
        with open('results.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                try:
                    self.demanded_locates[row[1]] = int(row[2]) + int(self.demanded_locates[row[1]])
                    print(f'Incremented {row[1]} by {row[2]}')
                except KeyError:
                    self.demanded_locates[row[1]] = int(row[2])
                    print("New entry was created")
        print(f'demanded locates: {self.demanded_locates}')

    def approved_locates(self):
        is_pop_itme = random.choices([True, False])
        if is_pop_itme:
            self.symbol_list.pop(random.randrange(len(self.symbol_list)))
        for symbol in self.symbol_list:
            self.supply_locates[symbol] = random.choice([random.randint(100, 600), random.randint(1, 6) * 100])
        print(f'approved locates: {self.supply_locates}')

    def request_locates(self):
        for symbol in self.symbol_list:
            result = self.compare_demand_and_supply(symbol)
            # Number approved locates are the same as demanded
            if result == "equal":
                with open('results.csv', 'r') as file:
                    reader = csv.reader(file, delimiter=',')
                    for row in reader:
                        if row[1] == symbol:
                            print(f'{row[0]} was supplied with {row[2]} locates for symbol {row[1]}')

        # Number approved locates are less then demanded
            elif result == "over_demand":
                proportion_amounts = self.calc_proportional_amounts(symbol)
                if len(proportion_amounts) == 1:
                    with open('results.csv', 'r') as file:
                        reader = csv.reader(file, delimiter=',')
                        for row in reader:
                            if row[1] == symbol:
                                print(f'{row[0]} was supplied with {self.supply_locates[symbol]} locates for symbol {row[1]}')
                # The logic is to round the amount half way up or down and sum the left overs and add them to the last client
                elif len(proportion_amounts) > 1:
                    filtered_csv = []
                    with open('results.csv', 'r') as file:
                        reader = csv.reader(file, delimiter=',')
                        for row in reader:
                            if row[1] == symbol:
                                filtered_csv.append(row[0])
                        for client, amount in zip(filtered_csv, proportion_amounts):
                            print(f'{client} was supplied with {amount} locates for symbol {symbol}')
        # Number approved locates are bigger then demanded
            elif result == "over_supply":
                print(f'{symbol} is over supplied!')
                with open('results.csv', 'r') as file:
                    reader = csv.reader(file, delimiter=',')
                    for row in reader:
                        if row[1] == symbol:
                            print(f'{row[0]} was supplied with {row[2]} locates for symbol {row[1]}')
                    print(f'after supplying all demands, the left over in the amount of {self.supply_locates[symbol] - self.demanded_locates[symbol]}'
                          f' is redirected to other clients')
        # No locates are approved for the requested symbol
            elif result == 'no_supply':
                print(f'There was no supply for {symbol} locates')

            else:
                print('internal error')

    def compare_demand_and_supply(self, symbol: str) -> str:

        try:
            if self.demanded_locates[symbol] == self.supply_locates[symbol]:
                result = "equal"
            elif self.demanded_locates[symbol] < self.supply_locates[symbol]:
                result = "over_supply"
            elif self.demanded_locates[symbol] > self.supply_locates[symbol]:
                result = "over_demand"
            else:
                result = 'internal_error'
        except KeyError:
            result = 'no_supply'
        return result

    def calc_proportional_amounts(self, symbol: str) -> list:
        proportions = []
        proportional_amounts = []
        left_over = 0
        with open('results.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[1] == symbol:
                    proportions.append(int(int(row[2]) / 100))
            print(proportions)
            proportional_unit = self.supply_locates[symbol] / sum(proportions)
            print(proportional_unit)
            for item in proportions:
                amount = item * proportional_unit
                rounded_amount = round(amount, -2)
                left_over += amount - rounded_amount
                proportional_amounts.append(rounded_amount)
            while left_over > 0:
                for item in proportions:
                    if left_over <= 100:
                        proportional_amounts[random.randint(0, len(proportions) - 1)] += left_over
                        left_over = 0
                    elif left_over > 100:
                        proportional_amounts[proportions.index(item)] += 100
                        left_over -= 100
            print(proportional_amounts)
            return proportional_amounts


def main():
    locates_distributer = LocatesDistributer()
    locates_distributer.generate_demand_csv(9)
    locates_distributer.requested_locates()
    locates_distributer.approved_locates()
    locates_distributer.request_locates()


if __name__ == '__main__':
    main()
