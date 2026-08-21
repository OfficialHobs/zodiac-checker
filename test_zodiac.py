from datetime import datetime
birth_date = datetime.strptime("15/08/2001", "%d/%m/%Y")

print(birth_date)
print(birth_date.month)
print(birth_date.day)


def get_zodiac(month, day):

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"

    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"

    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"

    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"

    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"

    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"

    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"

    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"

    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"

    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"

    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

    return "Invalid date"
print(get_zodiac(3, 21))