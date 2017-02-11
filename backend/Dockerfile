FROM p0bailey/docker-flask
MAINTAINER Fuyang Liu "liufu.ty@gmail.com"

# Use python3 and pip3, also update uwsgi.ini to use plugins=python3
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev uwsgi-plugin-python3 libpcre3 libpcre3-dev
RUN pip3 install uwsgi -I

COPY flask.conf /etc/nginx/sites-available/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf

# attach current dir
ADD . /var/www/app
RUN mkdir -p /var/www/app/log

RUN pip3 install -r /var/www/app/requirements.txt

RUN groupadd --gid 1000 www-app && \
    adduser --disabled-password --gecos '' --uid 1000 --gid 1000 www-app

RUN chown -R www-app:www-app /var/www/app

CMD ["/usr/bin/supervisord"]
