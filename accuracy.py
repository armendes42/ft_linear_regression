import sys
from training import get_data_from_csv
from plot import get_theta_from_csv
from linear_regression import estimate_price


def calculate_accuracy(mileages, prices, t0, t1):
    if t0 and t1:
        length = len(prices)
        mean = sum(prices) / length
        total_sum = 0
        est_sum = 0
        for i in range(length):
            total_sum += pow(prices[i] - mean, 2)
            est = estimate_price(mileages[i], mileages, prices, t0, t1)
            est += pow(prices[i] - est, 2)
        try:
            coeff = 1 - (est_sum / total_sum)
        except ZeroDivisionError:
            print("Error: The csv file with data seems to be empty.")
            sys.exit(1)
        return coeff
    return 0.0


def display_accuracy(accuracy):
    print(f"The accuracy is {accuracy:.2f} and {round(accuracy * 100)}%.")


def main():
    mileages, prices = get_data_from_csv()
    theta_0, theta_1 = get_theta_from_csv()
    accuracy = calculate_accuracy(mileages, prices, theta_0, theta_1)
    display_accuracy(accuracy)


if __name__ == "__main__":
    main()
