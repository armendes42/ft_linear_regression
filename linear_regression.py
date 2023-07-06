import sys
from training import get_data_from_csv
from plot import get_theta_from_csv


def get_mileage():
    try:
        user_input = input("Please enter a mileage:\n")
        mileage = float(user_input)
        if mileage < 0:
            print("The value can't be negative.")
            mileage = get_mileage()
        elif mileage > 1000000:
            print("The value is too high.")
            mileage = get_mileage()
    except ValueError:
        print("The value entered is not a float or an int.")
        mileage = get_mileage()
    except Exception as e:
        print(f"The program crashed unexpectedly : {e}")
        sys.exit(1)
    return mileage


def estimate_price(mileage, mileages, prices, theta_0, theta_1):
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    min_price = min(prices)
    max_price = max(prices)
    normalize_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
    mileage = theta_1 * normalize_mileage + theta_0
    if mileage:
        denormalize_mileage = mileage * (max_price - min_price) + min_price
    else:
        denormalize_mileage = 0
    return denormalize_mileage


def main():
    mileages, prices = get_data_from_csv()
    theta_0, theta_1 = get_theta_from_csv()
    mileage = get_mileage()
    value = estimate_price(mileage, mileages, prices, theta_0, theta_1)
    if value < 0:
        print(f"The mileage is too high, we can't sell it. ({round(value)}$)")
    else:
        print(f"The estimated price of the car is : {round(value)}$.")


if __name__ == "__main__":
    main()
