from pprint import pprint as pp

stocks = {1: "Sumanesh", 2: "Saveetha", 3: "Aadhavan", 4: "Aghilan"}

print(stocks)

# we can update an existing value or add a new value using dict.stocks
stocks.update({1: "Suman", 5: "Nila"})
print("After the dict.update")
print(stocks)
pp(stocks)

print(type(stocks))

molecule = {'A': [1, 2],
            'B': [3, 4],
            'C': [5, 6]
            }
molecule['A'] += [10, 11]

pp(molecule)