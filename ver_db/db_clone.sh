#!/bin/bash

current_date=$(date +"%Y_%m_%d_%H:%M:%S")

USER=dump
PASSWORD=ui2TyUmEc1G12357sdf4QtGhtFI8NNWcEh

mysqldump -u $USER --password=$PASSWORD verification > /home/data/db_dump_$current_date.sql

mysql -u $USER --password=$PASSWORD -D verification -e "DELETE FROM UP;"
mysql -u $USER --password=$PASSWORD -D verification -e "DELETE FROM Users;"
mysql -u $USER --password=$PASSWORD -D verification -e "DELETE FROM Passport;"