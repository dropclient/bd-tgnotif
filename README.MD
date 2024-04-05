### Описание:
Контейнер Docker со скриптом на Python для уведомления о предстоящих днях рождениях в Telegram.
✔️ Поддержка уведомления в группы
✔️ Поддержка уведомления в треды групп
✔️ Настройка дней уведомления помимо сегодня и завтра
### Установка:
Запуск производится в контейнере
1. `git clone https://gitverse.ru/sc/666/bd-tgnotif.git`
2. `cd bd-tgnotif`
3. Редактируем conf.json и заполняем дни рождения - birthdays.csv
3. `docker build -t bd-notif .`
4. `docker run -v ./data:/app/data --name bdnotif-container -d bd-notif`