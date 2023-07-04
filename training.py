import csv
import matplotlib.pyplot as plt
import sys


def get_data_from_csv():
    mileages = []
    prices = []
    try:
        with open(r"data.csv") as file:
            my_reader = csv.reader(file, delimiter=",")
            for row in my_reader:
                if len(row) == 2 and row[0].isdigit() and row[1].isdigit():
                    mileages.append(float(row[0]))
                    prices.append(float(row[1]))
    except IOError:
        print("Error on the csv file.")
        sys.exit(1)
    return mileages, prices


def estimatePrice(theta_0, theta_1, mileage):
    return theta_0 + (theta_1 * mileage)


def process_theta_0(mileages, prices, theta_0, theta_1, learning_rate):
    tmp_theta = learning_rate * (1 / len(mileages))
    tmp_theta_sum = 0
    for mileage, price in zip(mileages, prices):
        tmp_theta_sum += estimatePrice(theta_0, theta_1, mileage) - price
    return tmp_theta * tmp_theta_sum


def process_theta_1(mileages, prices, theta_0, theta_1, learning_rate):
    tmp_theta = learning_rate * (1 / len(mileages))
    tmp_theta_sum = 0
    for mileage, price in zip(mileages, prices):
        tmp_theta_sum += (estimatePrice(theta_0, theta_1, mileage) - price) * mileage
    return tmp_theta * tmp_theta_sum


def descent_gradient(mileages, prices):
    generation = 50
    learning_rate = 0.05
    theta_0 = 0.0
    theta_1 = 0.0
    for i in range(generation):
        tmp_theta_0 = process_theta_0(mileages, prices, theta_0, theta_1, learning_rate)
        tmp_theta_1 = process_theta_1(mileages, prices, theta_0, theta_1, learning_rate)
        theta_0 = tmp_theta_0
        theta_1 = tmp_theta_1
    return theta_0, theta_1


def save_in_file(theta_0, theta_1):
    with open("theta.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Theta 0", "Theta 1"])
        writer.writerow([theta_0, theta_1])


def training():
    mileages, prices = get_data_from_csv()
    theta_0, theta_1 = descent_gradient(mileages, prices)
    save_in_file(theta_0, theta_1)
