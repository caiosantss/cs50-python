months = ["January","February","March","April","May","June","July","August","September","October",
"November","December"]

def main():
    while True:

        date = input("Date: ").strip()

        try:
            ## se input for month/day/year
            if "/" in date:
                parts = date.split("/")

                if len(parts) != 3:
                    continue

                month, day, year = parts

            ## se o input for Month Day, Year
            else:
                if "," not in date:
                    continue
                month_str, day, year = date.replace(",", "").split()
                ## atribui a variavel month
                month = validate_month(month_str)

            ## fora do if, valida os valores
            month = validate_month(month)
            day = validate_day(day)
            year = validate_year(year)

            ## se algum der falso, retorna ao começo do loop

            if not(month and day and year):
                continue

            ## output: the same date as YYYY-MM-DD
            print(f"{year:04}-{month:02}-{day:02}")
            break

        except ValueError:
            pass
        except EOFError:
            break


def validate_month(month):
    ##se o mes for numerico - converte inteiro - retorna mes
    if month.isdecimal():
        month = int(month)
        if 1 <= month <= 12:
            return month
        else:
            return False
    else:
        ##caso o mes nao seja numerico
        ##try, pois pode dar erro de valor de lista
        try:
            return months.index(month.capitalize()) + 1
        except ValueError:
            return False


def validate_day(day):
    if day.isdecimal():
        day = int(day)
        if 1 <= day <= 31:
            return day
    return False


def validate_year(year):
    if year.isdecimal():
        year = int(year)
        if year > 0:
            return year
    return False


main()














