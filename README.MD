### Описание:
Контейнер Docker со скриптом на Python для уведомления о предстоящих днях рождениях в Telegram.  
✔️ Поддержка уведомления в группы  
✔️ Поддержка уведомления в треды групп  
✔️ Настройка дней уведомления помимо сегодня и завтра  
### Установка:
Запуск производится в контейнере
1. `git clone https://gitverse.ru/sc/666/bd-tgnotif.git` или `git clone https://github.com/dropclient/bd-tgnotif.git`
2. `cd bd-tgnotif`
3. Редактируем conf.json и заполняем дни рождения - birthdays.csv
3. `docker build -t bd-notif .`
4. `docker run -v ./data:/app/data --name bdnotif-container -d bd-notif`

### Настройка
`data/config.json`
```
   "Telegramtoken": "<token>",` - указываем токен бота в Telegram
   "Telegramchatid": "<chatid>",` - указываем ID чата куда отправлять уведомления
   "Telegramthreadid": "<threadid>",` - при необходимости указываем ID треда, если тредов нет, оставляем пустым ("")
   "WarnDays": [0,1,3,7,10,14]` - за сколько дней уведомлять  
```
`data/birthdays.csv`
Имя и день рождения через запятую, в формате: 
```
Name,Value
Имя,01.01.2001
```