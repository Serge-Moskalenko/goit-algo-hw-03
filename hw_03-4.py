from datetime import datetime,timedelta

users={
    "first":"1995.03.16"
}

birthdays_users = {}
upcoming_birthdays = []

today=datetime.today().date()

def make_birthdays_in_datetime(users):
    for key, value in users.items():
        b_user=datetime.strptime(value, "%Y.%m.%d").date().replace(year=today.year)
        birthdays_users.update({key : b_user})

def get_upcoming_birthdays(birthdays_users):
    end_date = today + timedelta(days=7)

    for name , birthday in birthdays_users.items():
        if birthday < today:
            birthday=birthday.replace(year=birthday.year +1)
        
        if today <= birthday <= end_date:

            if birthday.weekday() in [5,6]:
                next_monday=7-birthday.weekday()
                congratulation_date=birthday + timedelta(next_monday)
            else:
                congratulation_date=birthday

            upcoming_birthdays.append({
                "name":name,\
                "congratulation_date":congratulation_date.strftime("%Y.%m.%d")})


make_birthdays_in_datetime(users)

get_upcoming_birthdays(birthdays_users)

print(upcoming_birthdays)