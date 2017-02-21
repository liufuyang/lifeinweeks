FROM ubuntu:16.04
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# Use python3 and pip3, also update uwsgi.ini to use plugins=python3
RUN apt-get update --fix-missing
RUN apt-get install -y python3-pip python3-dev uwsgi-plugin-python3 \
    libpcre3 libpcre3-dev libpq-dev nginx supervisor
RUN pip3 install uwsgi -I

COPY config/flask.conf /etc/nginx/sites-available/
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Add SSL certificate
RUN mkdir /etc/nginx/ssl
# COPY config/example.com.crt /etc/nginx/ssl/fullchain.pem
# COPY config/example.com.key /etc/nginx/ssl/privkey.pem

# attach current dir
ADD . /var/www/app
RUN mkdir -p /var/www/app/log

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf
    
RUN pip3 install -r /var/www/app/requirements.txt

RUN groupadd --gid 1000 www-app && \
    adduser --disabled-password --gecos '' --uid 1000 --gid 1000 www-app
RUN chown -R www-app:www-app /var/www/app

# 
CMD ["/usr/bin/supervisord"]
