### Описание:

### Установка:
Запуск производится в контейнере
1. `git clone https://gitverse.ru/sc/666/bd-tgnotif.git`
2. `cd bd-tgnotif`
3. Редактируем conf.json и заполняем дни рождения - birthdays.csv
3. `docker build -t bd-notif .`
4. `docker run -v ./data:/app/data --name bdnotif-container -d bd-notif`