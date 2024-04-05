"""
    Author - dropclient
    Version - 0.1
"""
import json
import datetime
import requests
import pandas as pd
import os
from datetime import datetime

curdir = os.listdir('.')
c = open('data/conf.json')
config = json.load(c)
def send_telegram(message):
    requests.packages.urllib3.disable_warnings()
    response = requests.get(f"https://api.telegram.org/bot{config['Telegramtoken']}/sendMessage?chat_id={config['Telegramchatid']}&message_thread_id={config['Telegramthreadid']}&text={message}", verify=False)
    response.raise_for_status()

current_date = datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)  # Текущая дата с нулями во времени
warn_days = config['WarnDays']  # Дни напоминания
current_year = datetime.today().year
df = pd.read_csv('data/birthdays.csv') # Читаем CSV файл
for index, row in df.iterrows(): # Получаем имя и дату рождения из каждой строки
    name = row['Name']
    birthday = row['Value']
    birthday_date = datetime.strptime(birthday, '%d.%m.%Y') # Преобразуем дату рождения в объект datetime
    birthday_date_raw = birthday_date.replace(year=current_year) 
    age = (current_date.year - birthday_date.year) - ((current_date.month, current_date.day) < (birthday_date.month, birthday_date.day)) # Вычисляем количество полных лет между сегодняшним днем и днем рождения
    days_until = birthday_date_raw - current_date
    if days_until.days in warn_days:
        if days_until.days == 0:  # Сегодня
            message = "🎂 Поздравляем, {} ({} лет) с днем рождения!".format(name, age)
        elif days_until.days == 1:  # Завтра
            message = "🎂 День рождения {} ({} лет) завтра! - {}".format(name, age, birthday_date_raw.strftime("%d.%m"))
        else:  # Остальные даты
            message = "🎂 День рождения {} ({} лет) через {} дней. - {}".format(name, age, days_until.days, birthday_date_raw.strftime("%d.%m"))
        send_telegram(message)    