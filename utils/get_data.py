import json
import datetime
import glob


from utils.days import get_name_weekday



json_files = glob.glob('timetable\*.json')


def get_day_data(message, day_number):
    info = []
    with open(json_files[0], 'r') as f: 
        text = json.load(f)
        for faculty in text["faculties"][0]["groups"]:
            if message.lower() == faculty["group_name"].lower():
                for day in faculty["days"]:
                    if day_number == day["weekday"]:
                        info.append('\n'+get_name_weekday(day["weekday"])+'\n')
                        try:    
                            for lesson in day["lessons"]:
                                data = f"\nПара: {lesson['subject']}\n" \
                                    f"Начало: {lesson['time_start']} Конец: {lesson['time_end']}\n"
                                for teacher in lesson['teachers']:
                                    data += f"Преподователь: {teacher['teacher_name']}\n"
                                for auditory in lesson['auditories']:
                                    data += f"Аудитория: {auditory['auditory_name']}\n"
                                info.append(data)
                        except KeyError:
                            data = "\nПар нет🥳"
                            info.append(data)
                    elif datetime.date.today().weekday()+1 == 7:
                        data = "В воскресенье пар нет"
                        info.append(data)
                break
                
    return ' '.join(str(x) for x in info)


def get_week_data(message):
    info = []
    with open(json_files[0], 'r') as f: 
        text = json.load(f)
        for faculty in text["faculties"][0]["groups"]:
            if message.lower() == faculty["group_name"].lower():
                for day in faculty["days"]:
                    info.append('\n'+get_name_weekday(day["weekday"])+'\n')
                    try:    
                        for lesson in day["lessons"]:
                            data = f"\nПара: {lesson['subject']}\n" \
                                f"Начало: {lesson['time_start']} Конец: {lesson['time_end']}\n"
                            for teacher in lesson['teachers']:
                                data += f"Преподователь: {teacher['teacher_name']}\n"
                            for auditory in lesson['auditories']:
                                data += f"Аудитория: {auditory['auditory_name']}\n"
                            info.append(data)
                    except KeyError:
                        data = "Пар нет🥳"
                        info.append(data)
                break
                
    return ' '.join(str(x) for x in info)
