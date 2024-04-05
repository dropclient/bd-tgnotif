FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get -y install cron vim

COPY crontab /etc/cron.d/crontab

RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

COPY . .

VOLUME /app/data

CMD ["cron", "-f"]