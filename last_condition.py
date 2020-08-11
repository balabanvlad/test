import csv

valute_currency = {
    'EUR': 1.18,
    'GBP': 0.9,
    'USA':1
}


def add_car(name):
    '''add car in file'''
    price = input(f"| Car not found,\n please input price in format 'price currency' for {name} (example:100 EUR):").split()
    price[0] = float(price[0])
    # convert to usd
    if price[1] in valute_currency:
            price[0] = float(price[0]) * valute_currency[price[1]]
    else:
        print('Wrong currency.')

    with open('data_base.csv', 'a') as file:
        fieldnames = ['car', 'price_in_usd']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'car': name, 'price_in_usd': price[0]})
    print('Car is added.')


if __name__ == '__main__':
    print("| Please, input car's name:")
    name = input()
    with open('data_base.csv', 'r') as file:
        reader = csv.DictReader(file)
        for read in reader:
            if name == read['car']:
                print(f"Price of {name} is {read['price']} {read['currency']}")
                break
        else:
            add_car(name)

    print('\n' * 2 + '_' * 30 + "\n| Program executed.")
