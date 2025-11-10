import re
import sys

'''
types of valid input:
    I: 9:00 AM to 5:00 | PM O: 09:00 to 17:00
    II: 9 AM to 5 PM | O: 09:00 to 17:00
    III: 9:00 AM to 5 PM | O: 09:00 to 17:00
    IV: 9 AM to 5:00 PM | O: 09:00 to 17:00
'''

def main():
    print(convert(input("Hours: ")))


def convert(s):
    '''
    I: 9:00 AM to 5:00 | PM O: 09:00 to 17:00
    II: 9 AM to 5 PM | O: 09:00 to 17:00
    III: 9:00 AM to 5 PM | O: 09:00 to 17:00
    IV: 9 AM to 5:00 PM | O: 09:00 to 17:00

    '''
    pattern = r"^(?P<hour_first>1[0-2]|[1-9])(?P<minute_first>:[0-5][0-9])? (?P<am_pm_first>AM|PM) to (?P<hour_last>1[0-2]|[1-9])(?P<minute_last>:[0-5][0-9])? (?P<am_pm_last>AM|PM)$"


    if match := re.search(pattern,s, re.IGNORECASE):
        hour_first = int(match.group("hour_first"))
        minute_first = match.group("minute_first") or ":00"
        am_pm_first = match.group("am_pm_first")
        hour_last = int(match.group("hour_last"))
        minute_last = match.group("minute_last") or ":00"
        am_pm_last = match.group("am_pm_last")


        '''
        Caso	                Regra
        Se for AM e hora = 12	Substitui por 00
        Se for AM e hora ≠ 12	Mantém igual
        Se for PM e hora = 12	Mantém igual
        Se for PM e hora ≠ 12	Soma 12	3:00 PM

        '''
        # Se for AM e hora = 12	Substitui por 00
        if am_pm_first == "AM" and hour_first == 12:
            hour_first = 0

        if am_pm_last == "AM" and hour_last == 12:
            hour_last = 0

        # Se for AM e hora ≠ 12	Mantém igual
        ...

        # Se for PM e hora = 12	Mantém igual
        ...

        # Se for PM e hora ≠ 12	Soma 12
        if am_pm_first == "PM" and hour_first != 12:
            hour_first += 12

        if am_pm_last == "PM" and hour_last != 12:
            hour_last += 12

        return f"{hour_first:02}{minute_first} to {hour_last:02}{minute_last}"

    else:
        raise ValueError("Invalid input")


if __name__ == "__main__":
    main()
