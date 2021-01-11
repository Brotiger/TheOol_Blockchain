FROM mysql

RUN mkdir /home/cron
COPY ./db_clone.sh /home/cron/db_clone.sh

RUN apt-get update && apt-get install -y cron