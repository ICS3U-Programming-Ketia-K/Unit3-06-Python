#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Dec 14, 2021
# This program uses the try statement


import random


def main():
    # This function schecks if guessed number is equal or not equal
    # to the random number generated or if it is just not an integer.
    random_number = random.randint(0, 9)
    number_as_string = input("Guess a number between 0 and 9: ")
    print("")
    # The function below casts the string to an integer and checks
    # if it is a integer or not an integer using try statement.
    try:
        number_as_integer = int(number_as_string)
        if number_as_integer == random_number:
            print("Your guess is correct!")
            print("")
        else:
            print("Your guess is wrong. The correct number is {}"
                  .format(random_number))
            print("")
    except Exception:
        print("What you entered is not an integer")
        print("")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
