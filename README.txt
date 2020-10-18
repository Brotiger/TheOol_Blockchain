Для запуска сервера необходимо задать пароль для root пользователя mysql через переменную окружения MYSQL_ROOT_PASSWORD и выполнить команду docker-compose up

Для доступа к бд в контейнере с mysql необходимо создать пользователя:
CREATE user "server"@"%" IDENTIFIED BY "v9bumEc1G9c8HBDO4QtHsFI8NNWcEh";
GRANT ALL PRIVILEGES ON verification.* TO "server"@"%"