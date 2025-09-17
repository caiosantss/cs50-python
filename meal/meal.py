def main():

    time = input("What time is it:").strip()
    total_hours =  convert(time)


    ##Cafe da manha 7.0 - 8.0
    if 7 <= total_hours <= 8:
        print("breakfast time")
    elif 12 <= total_hours <= 13:
        print("lunch time")
    elif 18 <= total_hours <= 19:
        print("dinner time")


def convert(time):
    ## 7:30 / 12:30
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    ## Dividing minutes for 60 - turn it to a float number based on how many it is missing to achieve an hour
    return hours + minutes / 60

if __name__ == "__main__":
    main()
