import sys
def main():

    conta_linha = 0

    try:
        with open(get_argv(), "r") as f:
            for line in f:
                if not line.lstrip().startswith("#") and not line.strip() == "":
                    conta_linha+=1
                    #print(line.strip())

            print(conta_linha)

    except (FileNotFoundError):
        sys.exit("File does not exist")


def get_argv() -> str:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            return str(sys.argv[1])
        else:
            return sys.exit("Not a Python file")
    elif(len(sys.argv) < 2):
        sys.exit("Too few command-line arguments ")
    else:
        sys.exit("Too many command-line arguments")


main()

