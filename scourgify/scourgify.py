import csv
import sys


def main():

    check_argv()

    # SCOURGIFY
    try:
        with open(str(sys.argv[1]), "r", newline="", encoding="utf-8") as oldFile, \
            open(str(sys.argv[2]), "w", newline="", encoding="utf-8") as newFile:

            readerOldFile = csv.DictReader(oldFile)

            fieldnames = ["first", "last", "house"]
            writerNewFile = csv.DictWriter(newFile, fieldnames=fieldnames)

            #cabeçalho tem que ser escrito antes do loop, pois dictReader que sera percorrido pelo loop não coloca o cabeçalho no loop ele começa a partir da segunda linha

            writerNewFile.writeheader()

            for line in readerOldFile:
                last_name, name = line["name"].strip().split(", ")
                # The keys must have the save value as the fieldnames
                new_line = {"first": name, "last": last_name, "house": line["house"]}
                writerNewFile.writerow(new_line)

    except FileNotFoundError:
       raise sys.exit("File Not Found")



def check_argv():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")


main()




