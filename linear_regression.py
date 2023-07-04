import csv
import matplotlib.pyplot as plt


def normalize_value(mileages, prices):
    new_mileages = []
    new_prices = []
    max_mileage = max(mileages)
    min_mileage = min(mileages)
    max_price = max(prices)
    min_price = min(prices)
    for mileage in mileages:
        new_mileage = (float(mileage)-min_mileage)/(max_mileage-min_mileage)
        new_mileages.append(new_mileage)
    for price in prices:
        new_price = (float(price) - min_price) / (max_price - min_price)
        new_prices.append(new_price)
    return new_mileages, new_prices


if __name__ == "__main__":
    file = open(r"data.csv")
    my_reader = csv.reader(file)
    mileages = []
    prices = []

    for index, row in enumerate(my_reader):
        if index != 0:
            mileages.append(float(row[0]))
            prices.append(float(row[1]))
    # mileages, prices = normalize_value(mileages, prices)
    plt.scatter(mileages, prices, s=10)
    plt.ylabel("Price")
    plt.xlabel("Mileage")
    plt.show()
