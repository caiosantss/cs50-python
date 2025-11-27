import re
import sys


def main():
    print(count(input("Text: ")))


def count(s)-> int:
    pattern = r"\bum\b"
    matchfindall = re.findall(pattern, s, re.IGNORECASE)
    return len(matchfindall)

if __name__ == "__main__":
    main()
