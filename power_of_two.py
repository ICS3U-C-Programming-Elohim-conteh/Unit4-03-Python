#!/usr/bin/env python3

# Created by: elohim
# Created on: Nov 11 2026
# This program calculates the square of each number from 0 to the user input


def main():
    # input
    user_input = input("Enter a whole number: ")
    print("")

    # process & output
    try:
        user_number_as_int = int(user_input)

        if user_number_as_int < 0:
            print("Please enter a positive whole number.")
        else:
            for counter in range(user_number_as_int + 1):
                power_of_two = counter ** 2
                print("{}^2 = {}".format(counter, power_of_two))

    except ValueError:
        print("Invalid entry! Please enter a valid integer.")


if __name__ == "__main__":
    main()
