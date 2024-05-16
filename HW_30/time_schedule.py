from datetime import datetime, timedelta

start_date = datetime(2024, 4, 11, 19, 15)
class_days = [0, 3]


def next_class_date(current_date):
    while current_date.weekday() not in class_days:
        current_date += timedelta(days=1)
    return current_date


current_date = start_date
lecture_number = 1
while lecture_number <= 32:
    print(f"Lecture {lecture_number}: {current_date.strftime('%d %b %Y %H:%M')}")
    current_date = next_class_date(current_date + timedelta(days=1))
    lecture_number += 1
