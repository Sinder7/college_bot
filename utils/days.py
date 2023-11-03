
weekday_mapping = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота"
}

def get_name_weekday(day_number):

    day_of_week = weekday_mapping.get(day_number)

    return day_of_week