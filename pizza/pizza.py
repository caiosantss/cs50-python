import csv
import tabulate
import sys


def main():

    try:
        with open(get_argv()) as csvFile:
            reader = csv.DictReader(csvFile)
            print(tabulate.tabulate(reader, headers="keys" ,tablefmt="grid"))
    except FileNotFoundError:
        raise (sys.exit("File does not exist"))


def get_argv():

    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return str(sys.argv[1])
        else:
            sys.exit("Not a CSV file")
    elif(len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

main()


## Input - sys argv -  one command-line argument, the name (or path) of a CSV file in Pinocchio’s format
##  outputs a table formatted as ASCII art using tabulate // Format the table using the library’s grid format.

## error at input:
# ok if the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .csv, or
# ok - if the specified file does not exist, the program should instead exit via sys.exit.
