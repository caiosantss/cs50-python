import datetime
import inflect
import sys

p = inflect.engine()


def main():

    agora_hora_zerada = get_date_now()

    # Lê a data de entrada
    date_input = input("Date of Birth: ")

    # Converte a data de entrada
    try:
        data_convertida = convert_input_date(date_input)
    except ValueError:
        sys.exit("Invalid date")

    # Calcula a diferença em minutos
    minutos = diference_in_minutes(data_convertida, agora_hora_zerada)

    # Converte o número de minutos para palavras
    minutos_por_extenso = number_to_words(minutos)

    # Exibe o resultado
    print(f"{minutos_por_extenso} minutes")


def convert_input_date(data):
    # converte para datetime object - Data + Hora(00:00:00)
    return datetime.datetime.strptime(data, "%Y-%m-%d").date()


def diference_in_minutes(date, date_now):
    # Calcula a diferença em minutos entre duas datas
    return (date_now - date).total_seconds() / 60


def number_to_words(number):
    return p.number_to_words(int(number), andword=" ").capitalize()


def get_date_now():
    return datetime.date.today()


if __name__ == "__main__":
    main()
