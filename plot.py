import csv
import matplotlib.pyplot as plt
from training import get_data_from_csv


def get_theta_from_csv():
    theta_0 = 0.0
    theta_1 = 0.0
    try:
        with open(r"theta.csv") as file:
            my_reader = csv.reader(file, delimiter=",")
            for index, row in enumerate(my_reader):
                if index != 0:
                    theta_0 = float(row[0])
                    theta_1 = float(row[1])
    except IOError:
        print("Error on the csv file.")
    except ValueError:
        print("Error: the csv file seems to contain invalid values.")
    return theta_0, theta_1


def main():
    mileages, prices = get_data_from_csv()
    theta_0, theta_1 = get_theta_from_csv()
    plt.scatter(mileages, prices, s=10)
    if theta_0 and theta_1:
        min_mile = min(mileages)
        max_mile = max(mileages)
        min_price = min(prices)
        max_price = max(prices)
        line_mileages = [min_mile, max_mile]
        line_prices = []
        for mile in line_mileages:
            normalize_mile = (mile - min_mile) / (max_mile - min_mile)
            mile = theta_1 * normalize_mile + theta_0
            if mile:
                denormalize_mile = mile * (max_price - min_price) + min_price
            else:
                denormalize_mile = 0
            line_prices.append(denormalize_mile)
        plt.plot(line_mileages, line_prices, color="red", label="Estimated Prices")
    plt.ylabel("Price")
    plt.xlabel("Mileage")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
