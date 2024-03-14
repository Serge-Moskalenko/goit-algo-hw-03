from datetime import datetime

def get_days_from_today(date):
    try:
        today=datetime.today()
        datetime_object=datetime.strptime(date,"%Y-%m-%d")
        delta=today - datetime_object
    
        return print(delta.days)
    except:
        print("date isnt correct")


get_days_from_today("2019-02-21")