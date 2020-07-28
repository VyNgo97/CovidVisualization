import requests
import pandas as pd
from datetime import datetime, timedelta
from threading import Timer

files = ['time_series_covid19_confirmed_global.csv', 'time_series_covid19_deaths_global.csv', 'time_series_covid19_recovered_global.csv']
date_today = datetime.today()
next_day = date_today.replace(day=date_today.day+1, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
change_in_time = next_day - date_today
secs = change_in_time.seconds + 1

def fetch_data(listOfFiles):
    for file in files:
        URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/' + file
        data = pd.read_csv(URL)
        data.to_csv(r'/home/vy/Documents/CovidVisualization/data/' + file, index=False)

    return

# t = Timer(secs, fetch_data(files))
# t.start()

fetch_data(files)