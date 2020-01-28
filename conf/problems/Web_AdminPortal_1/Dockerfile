FROM php:7.3-apache

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get install -y libsqlite3-dev && docker-php-ext-install pdo_sqlite

ADD challenge/flag1.txt /flag1.txt
ADD challenge/flag2.txt /flag2.txt
ADD challenge/flag3.elf /flag3.execute_me
RUN chown root:root /flag2.txt
RUN chown root:root /flag1.txt
RUN chown root:root /flag3.execute_me
RUN chmod 444 /flag1.txt
RUN chmod 444 /flag2.txt
RUN chmod 111 /flag3.execute_me

ADD challenge/sqlite.db    /var/www/
ADD challenge/templates    /var/www/html/templates
ADD challenge/index.php    /var/www/html/
ADD challenge/login.php    /var/www/html/
ADD challenge/register.php /var/www/html/
ADD challenge/util.php     /var/www/html/
ADD challenge/index.php    /var/www/html/

WORKDIR /var/www/html
RUN chmod 440 *.php
RUN chmod 440 templates/*.html
RUN chmod 660 ../sqlite.db

RUN chown www-data:www-data /var/www
RUN chown www-data:www-data /var/www/sqlite.db
RUN chown -R root:www-data /var/www/html

EXPOSE 8001
