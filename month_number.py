#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program tells the months
# with user input


def main():
    # This function tells the months

    # input
    your_number = int(input("Enter any number of your choice (1-12): "))

    # process
    if your_number == 1:
        # output
        print("")
        print("January")

    elif your_number == 2:
        # output
        print("")
        print("February")
    elif your_number == 12:
        # output
        print("")
        print("December")
    else:
        print("")
        print("Error")


if __name__ == "__main__":
    main()
