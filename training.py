import csv
import sys


def normalize_value(data):
    max_data = max(data)
    min_data = min(data)
    scaled_data = []
    for elem in data:
        try:
            scaled_data.append((elem - min_data) / (max_data - min_data))
        except ZeroDivisionError:
            print("The csv file contains only one entry,\
                 which is not good for this exercise.")
            sys.exit(1)
    return scaled_data


def denormalize_value(data, origin_min, origin_max):
    origin_data = [(x * (origin_max - origin_min)) + origin_min for x in data]
    return origin_data


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
    if len(mileages) == 0 or len(prices) == 0:
        raise ValueError()
    return mileages, prices


def estimatePrice(theta_0, theta_1, mileage):
    return theta_0 + (theta_1 * mileage)


def process_t0(mileages, prices, theta_0, theta_1, learning_rate):
    tmp_theta = learning_rate * (1 / len(mileages))
    sum = 0
    for mileage, price in zip(mileages, prices):
        sum += estimatePrice(theta_0, theta_1, mileage) - price
    return tmp_theta * sum


def process_t1(mileages, prices, theta_0, theta_1, learning_rate):
    tmp_theta = learning_rate * (1 / len(mileages))
    sum = 0
    for mileage, price in zip(mileages, prices):
        sum += (estimatePrice(theta_0, theta_1, mileage) - price) * mileage
    return tmp_theta * sum


def descent_gradient(mileages, prices):
    generation = 300
    learning_rate = 0.5
    theta_0 = 0.0
    theta_1 = 0.0
    for i in range(generation):
        tmp_t0 = process_t0(mileages, prices, theta_0, theta_1, learning_rate)
        tmp_t1 = process_t1(mileages, prices, theta_0, theta_1, learning_rate)
        theta_0 -= tmp_t0
        theta_1 -= tmp_t1
    return theta_0, theta_1


def save_in_file(theta_0, theta_1):
    with open("theta.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Theta 0", "Theta 1"])
        writer.writerow([theta_0, theta_1])


def main():
    mileages, prices = get_data_from_csv()
    norm_mileages = normalize_value(mileages)
    norm_prices = normalize_value(prices)
    theta_0, theta_1 = descent_gradient(norm_mileages, norm_prices)
    save_in_file(theta_0, theta_1)


if __name__ == "__main__":
    main()
